import os

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

from src.config import TIME_SERIES_EXPERIMENT_CONFIG

if __name__ == '__main__':
    # Get config values
    experiment_config = TIME_SERIES_EXPERIMENT_CONFIG
    days_lag = experiment_config['days_lag']
    target_column_name = experiment_config['target_column_name']
    date_column_name = experiment_config['date_column_name']
    train_split_ratio = experiment_config['train_split_ratio']
    results_dir = experiment_config['results_dir']
    data_dir = experiment_config['data_dir']
    tickers = experiment_config['tickers']
    target_ticker = experiment_config['target_ticker']

    # Create an empty DataFrame to store combined data
    combined_data = pd.DataFrame()

    # Load and combine data from all tickers
    for ticker in tickers:
        data_path = os.path.join(data_dir, f"{ticker}.csv")
        df_data = pd.read_csv(data_path)
        # Prefix each column with the ticker name to distinguish between them
        df_data = df_data.add_prefix(f"{ticker}_")
        if combined_data.empty:
            combined_data = df_data
        else:
            combined_data = pd.merge(combined_data, df_data, left_index=True, right_index=True)

    # Create lag features for the combined data
    for column in combined_data.columns:
        combined_data[f'{column}_lag_{days_lag}'] = combined_data[column].shift(days_lag)

    # Remove empty values resulting from offsets
    combined_data = combined_data.dropna()

    # **Save the dates separately for later use**
    dates = combined_data[f'{target_ticker}_{date_column_name}'].values

    # **Remove date columns to avoid using them as features**
    combined_data = combined_data.drop(columns=[col for col in combined_data.columns if date_column_name in col])

    # Define the features (X) using lagged features and target variable (y) from BABA
    X_columns = [col for col in combined_data.columns if '_lag_' in col]
    X = combined_data[X_columns]
    y = combined_data[f'{target_ticker}_{target_column_name}']

    # Split the data into training and test sets
    train_size = int(len(X) * train_split_ratio)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Standardization of features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Linear regression model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predictions on the test set
    y_pred = model.predict(X_test_scaled)

    # Model validation
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')

    # Results visualization
    plt.figure(figsize=(10, 6))
    plt.plot(dates[train_size:], y_test.values, label='real values', marker='o')
    plt.plot(dates[train_size:], y_pred, label='predicted values', marker='x')
    plt.title(f'comparison of real values and predicted values: {target_ticker}')
    plt.xlabel('time')
    plt.ylabel(target_column_name)
    plt.legend()

    # Reduce the number of x-ticks and rotate them
    xticks_positions = range(0, len(dates[train_size:]), max(1, len(dates[train_size:]) // 20))
    plt.xticks(ticks=xticks_positions, labels=[dates[train_size:][i] for i in xticks_positions], rotation=90)

    # Save plot
    os.makedirs(results_dir, exist_ok=True)
    plot_path = os.path.join(results_dir, f'{target_ticker}_{target_column_name}.svg')
    plt.savefig(plot_path, format='svg', bbox_inches='tight')


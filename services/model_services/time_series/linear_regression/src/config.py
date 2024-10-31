import os

TIME_SERIES_EXPERIMENT_CONFIG = {
    'tickers': ('BABA', 'MSFT', 'NKE'),
    'target_ticker': 'BABA',
    'days_lags': [1, 2, 3, 5, 10],
    'train_split_ratio': 0.8,
    'target_column_name': 'Close',
    'date_column_name': 'Date',
    'data_dir': os.path.join('resources', 'datasets'),
    'results_dir': os.path.join('resources', 'results'),
}

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader, TensorDataset

from lstm_model import LSTMModel
from utils import create_sequences

COLUMN_TO_PREDICT = 'Close'

# model hiperparameters
input_size = 1
hidden_size = 64
output_size = 1
num_layers = 2

# experiment hiperparameters
learning_rate = 0.001
num_epochs = 100
criterion = nn.MSELoss()

if __name__ == '__main__':

    df = pd.DataFrame(data)

    # choose column to predict
    closing_prices = df[[COLUMN_TO_PREDICT]].values

    # data scaling
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(closing_prices)

    # creating training sequences
    window_size = 5  # setting the length of the prediction window
    x_train, y_train = create_sequences(scaled_data, window_size)

    # convert to tensor
    x_train = torch.tensor(x_train, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32)

    # define Dataset
    train_dataset = TensorDataset(x_train, y_train)
    train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)

    # define model and optimizer
    model = LSTMModel(input_size, hidden_size, output_size, num_layers)

    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    # model training
    for epoch in range(num_epochs):
        model.train()
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            output = model(batch_x)
            loss = criterion(output, batch_y)
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}')

    # predict last values
    model.eval()
    test_seq = torch.tensor(scaled_data[-window_size:], dtype=torch.float32).unsqueeze(0)
    predicted_price = model(test_seq).detach().numpy()

    # inverse scaling
    predicted_price = scaler.inverse_transform(predicted_price)
    print(f'predicted value: {round(predicted_price[0][0],3)}')

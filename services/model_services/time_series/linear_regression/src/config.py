import os

TIME_SERIES_EXPERIMENT_CONFIG = {
    'tickers': ('BABA', 'MSFT', 'NKE'),
    'days_lag': 1,
    'train_split_ratio': 0.8,
    'target_column_name': 'Close',
    'data_dir': os.path.join('resources', 'datasets'),
    'results_dir': os.path.join('resources', 'results'),
}

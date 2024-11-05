import os

DOWNLOAD_DATA_CONFIG = {
    'tickers': {
        'yahoo': {'BABA', 'MSFT', 'NKE'},
    },
    'time_interval': {
        'start_date': '2018-01-01',
        'end_date': '2020-01-01',
    },
    'save_dir': os.path.join('resources', 'datasets'),
}

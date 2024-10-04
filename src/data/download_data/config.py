from common import project_dir

DOWNLOAD_DATA_CONFIG = {
    'tickers': {
        'yahoo': {'BABA', 'MSFT', 'NKE'},
    },
    'time_interval': {
        'start_date': '2024-01-01',
        'end_date': '2024-02-01',
    },
    'save_dir': project_dir / 'resources' / 'datasets',
}
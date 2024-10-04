class DataDownloader:
    source_name = None

    def __init__(self):
        pass

    def download_data(self, ticker, start_date, end_date, *args, **kwargs):
        raise NotImplementedError(f'Method {self.__class__.__name__}.download_data() not implemented!')

    def save_data(self, save_dir: str, *args, **kwargs):
        raise NotImplementedError(f'Method {self.__class__.__name__}.save_data() not implemented!')

    @classmethod
    def get_source_name(cls):
        return NotImplementedError(f'Method {cls.__name__} not implemented!')

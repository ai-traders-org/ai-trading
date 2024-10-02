class DataDownloader:

    def __init__(self):
        pass

    def download_data(self, *args, **kwargs):
        raise NotImplementedError(f'Method {self.__class__.__name__}.download_data() not implemented!')

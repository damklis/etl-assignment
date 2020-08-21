import os


class DataSetDirectoryLoader:
    def __init__(self, data_dir, filename):
        self._path = self.create_data_path(
            data_dir, filename
        )
    
    @staticmethod
    def create_data_path(data_dir, filename):
        if not filename.endswith(".csv"):
            return os.path.join(data_dir, f"{filename}.csv")
        return os.path.join(data_dir, filename)

    def load_dataset(self, dataset):
        dataset.to_csv(
            path_or_buf=self._path,
            sep=";",
            index=False
        )


class DBDataSetLoader:
    def __init__(self, conn_config):
        pass

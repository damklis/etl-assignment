import pandas as pd


class DataSetExtractor:
    def __init__(self, files):
        self._files = files
        self.merger = self.FileMerger()
        
    class FileMerger:

        def concatenate(self, test_df, test_lvl_df, class_df):
            return (
                test_df.merge(
                    test_lvl_df.add_prefix("test_level_"),
                    on="test_level_id"
                ).merge(
                    class_df.add_prefix("class_"),
                    on="class_id"
                )
            )
        
    def extract_dataset(self):
        test_df, test_lvl_df, class_df = self.load_files()
        dataset = self.merger.concatenate(
            test_df, test_lvl_df, class_df
        )
        return dataset
    
    def load_files(self):
        return (pd.read_csv(**conf) for conf in self._files)
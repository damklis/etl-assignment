import pytest
import pandas as pd
from framework import (
    DataSetDirectoryLoader, DataSetTransformer, DataSetExtractor
)


@pytest.fixture
def dir_loader():
    yield DataSetDirectoryLoader(
        "test", "test"
    )


@pytest.fixture
def get_file_snippet():
    def helper(filename):
       return  pd.read_csv(
            f"./tests/resources/{filename}.csv", sep=";"
        )
    yield helper


@pytest.fixture
def db_config():
    yield {
        "user": "test", 
        "password": "test", 
        "host": "test", 
        "port": "5432", 
        "db": "test"
    }


@pytest.fixture
def merged_df(get_file_snippet):
    extractor = DataSetExtractor(["test"])
    df1 = get_file_snippet("test-snippet")
    df2 = get_file_snippet("test_level-snippet")
    df3 = get_file_snippet("class-snippet")
    yield extractor.concatenate_files(
        df1, df2, df3
    )


@pytest.fixture
def get_transformer():
    def helper(transformation):
        return DataSetTransformer(
            transformation
        )
    yield helper


@pytest.fixture
def files():
    yield[
        {
            "filepath_or_buffer": "./tests/resources/test-snippet.csv", 
            "sep": ";"
        },
        {
            "filepath_or_buffer": "./tests/resources/test_level-snippet.csv",
            "sep": ";"
        },
        {
            "filepath_or_buffer": "./tests/resources/class-snippet.csv",
            "sep": ";"
        }
    ]

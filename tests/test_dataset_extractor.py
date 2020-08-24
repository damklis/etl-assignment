import pandas as pd
import pytest
from framework import DataSetExtractor

from .fixtures import get_file_snippet, merged_df, files


def test_concatenate_files(merged_df):
    expected = 29

    result = len(merged_df.columns)

    assert expected == result


def test_load_files(files):

    extractor = DataSetExtractor(files)

    result = extractor.load_files()

    assert all(map(lambda x: isinstance(x, pd.DataFrame), result))

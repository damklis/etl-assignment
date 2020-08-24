from unittest import mock
import pytest

from .fixtures import dir_loader, get_file_snippet, db_config


@mock.patch("framework.dataset_loader.DataSetDBLoader.create_db_conn")
def test_create_db_conn(create_db_conn, db_config):

    create_db_conn(db_config)

    assert create_db_conn.called_once_with(db_config)


@pytest.mark.parametrize(
    "dir, file, expected",
    [("test", "test.csv", "test/test.csv"),
     ("test", "test", "test/test.csv")]
)
def test_create_data_path(dir, file, expected, dir_loader):
    
    result = dir_loader.create_data_path(
        dir, file
    )

    assert expected == result


@mock.patch("framework.dataset_loader.DataSetDirectoryLoader.load_dataset")
def test_load_content(load_dataset, get_file_snippet):

    dataset = get_file_snippet("test-snippet")

    load_dataset(dataset)

    assert load_dataset.called_once_with(dataset)

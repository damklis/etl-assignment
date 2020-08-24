import re
import pytest
import pandas as pd

from .fixtures import get_transformer, get_file_snippet, merged_df


def test_format_column_names(get_transformer, get_file_snippet):

    expected = [
        "test_id", "test_student_id", "class_id", "test_created_at","test_updated_at",
        "test_last_event_time", "test_overall_score", "test_status", 
        "test_institution_id", "test_authorized_at", "test_confidence_level",
        "test_speaking_score", "test_writing_score", "test_reading_score",
        "test_listening_score", "test_level_id", "test_licence_id"
    ]

    transformer = get_transformer("test_utilization")
    dataset = get_file_snippet("test-snippet")

    result = transformer.format_column_names(dataset)

    assert expected == result


def test_convert_test_dates(get_transformer, get_file_snippet):
    
    transformer = get_transformer("test_utilization")
    dataset = get_file_snippet("test-snippet")
    dataset.columns = transformer.format_column_names(
        dataset
    )

    result = transformer.convert_test_dates(dataset)

    test_created_at = str(result["test_created_at"][0])
    test_authorized_at = str(result["test_authorized_at"][0])

    pattern = r"\d{4}-\d{2}-\d{2}"

    assert re.match(pattern, test_created_at)
    assert re.match(pattern, test_authorized_at)


def test_transform_dataset_raises_error(get_transformer, merged_df):

    transformer = get_transformer("test")

    with pytest.raises(ValueError):
        transformer.transform_dataset(merged_df)


def test_test_utilization(get_transformer, merged_df):

    expected = [
        "class_id", "class_name", "class_teaching_hours", "test_id",
        "test_level_id", "test_created_at", "test_authorized_at",
        "class_test_number"
    ]

    transformer = get_transformer("test_utilization")
    merged_df.columns = transformer.format_column_names(
        merged_df
    )

    df = transformer.test_utilization(merged_df)
    result = list(df.columns)

    assert expected == result


def test_test_average_scores(get_transformer, merged_df):

    expected = [
        "class_id", "class_name", "class_teaching_hours",
        "test_created_at", "test_authorized_at", "avg_class_test_overall_score"
    ]

    transformer = get_transformer("test_average_scores")
    merged_df.columns = transformer.format_column_names(
        merged_df
    )

    df = transformer.test_average_scores(merged_df)
    result = list(df.columns)

    assert expected == result

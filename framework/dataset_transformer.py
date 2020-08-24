import pandas as pd

from .log import log


@log
class DataSetTransformer:
    def __init__(self, transformation):
        self.transformation = transformation
        
    def transform_dataset(self, df):
        self.logger.info("Transforming dataset")
        _df = df[df['authorized_at'].notnull()] 
        _df.columns = self.format_column_names(df)
        tmp_df = self.convert_test_dates(_df)
        
        if self.transformation == "test_utilization":
            return self.test_utilization(tmp_df)
        elif self.transformation == "test_average_scores":
            return self.test_average_scores(tmp_df)
        else:
            raise ValueError("Transformation unknown")
        
    def test_utilization(self, df):
        numeration = df.groupby(["class_id", "test_level_id"]).cumcount()+1
        return (
            df.assign(class_test_number=numeration)
            .filter(
                items=[
                    "class_id", "class_name","class_teaching_hours", "test_id",
                    "test_level_id", "test_created_at", "test_authorized_at", 
                    "class_test_number"
                ]
            )
        )
    
    def test_average_scores(self, df):
        tmp_df = df[df["test_status"] == "SCORING_SCORED"]
        avg_scores =  tmp_df.groupby(
            by=[
                "class_id", "class_name", "class_teaching_hours", 
                "test_created_at", "test_authorized_at"
            ]
        )["test_overall_score"].mean()
        
        return (
            pd.DataFrame(avg_scores)
            .reset_index()
            .rename(
                {'test_overall_score': 'avg_class_test_overall_score'},
                axis=1
            )
            .round(1)
        )
    
    @staticmethod
    def format_column_names(df):
        return [
            "test_" + col 
            if not col.startswith(("test_", "class_")) else col 
            for col in df
        ]
    
    @staticmethod
    def convert_test_dates(df):
        def trim_date(col):
            return pd.to_datetime(df[col]).dt.date
        
        return (
            df
            .assign(test_created_at=trim_date("test_created_at"))
            .assign(test_authorized_at=trim_date("test_authorized_at"))
        )

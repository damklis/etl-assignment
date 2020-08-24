import os


class Config:
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    DATA_DIR = os.path.join(BASE_DIR, "data")

    FILES = [
        {
            "filepath_or_buffer": os.path.join(DATA_DIR, "test.csv"), 
            "sep": ";",
            "usecols": [
                "id", "student_id", "class_id", "created_at", "updated_at", 
                "last_event_time", "overall_score", "test_status", "institution_id",
                "authorized_at", "confidence_level", "speaking_score", "writing_score",
                "reading_score", "listening_score", "test_level_id", "licence_id"
            ]
        },
        {
            "filepath_or_buffer": os.path.join(DATA_DIR, "test_level.csv"),
            "sep": ";",
            "usecols": ["id", "name", "displayName", "created_at", "updated_at"]
        },
        {
            "filepath_or_buffer": os.path.join(DATA_DIR, "class.csv"),
            "sep": ";",
            "usecols": [
                "id", "institution_id", "owner_id", "name", "created_at", "updated_at",
                "teaching_hours", "latest_test_time", "has_student_with_scored_test"
            ]
        }
    ]

    POSTGRES_CONFIG = {
        "user": "etl", 
        "password": "etl", 
        "host": "localhost", 
        "port": "5432", 
        "db": "transformations"
    }

    POSTGRES_SCHEMA = "tests"

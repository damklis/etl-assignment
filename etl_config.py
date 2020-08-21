import os


class Config:
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    FILES = [
        {
            "filepath_or_buffer": os.path.join(DATA_DIR, "test.csv"), 
            "sep": ";"
        },
        {
            "filepath_or_buffer": os.path.join(DATA_DIR, "test_level.csv"),
            "sep": ";"
        },
        {
            "filepath_or_buffer": os.path.join(DATA_DIR, "class.csv"),
            "sep": ";"
        }
    ]

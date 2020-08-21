
from etl_config import Config as cfg
from framework import (
    DataSetExtractor, DataSetTransformer,
    DataSetDirectoryLoader, ETLJob, time_func
)


@time_func
def run_etl_dir():

    extractor = DataSetExtractor(cfg.FILES)
    transformer = DataSetTransformer("test_average_scores")
    loader = DataSetDirectoryLoader(cfg.DATA_DIR, "test_average_scores")
    
    etl = ETLJob(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )

    status = etl.run()
    print(f"Job status: {status}")


if __name__ =="__main__":
    run_etl_dir()
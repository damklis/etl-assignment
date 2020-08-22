import argparse
from etl_config import Config as cfg
from framework import (
    DataSetExtractor, DataSetTransformer,
    DataSetDirectoryLoader, ETLJob, time_func
)


def parse_args():
    parser = argparse.ArgumentParser("Choose transformation")
    parser.add_argument(
        "-t", "--transformation", metavar="", help="transformation" 
    )
    return parser.parse_args()


@time_func
def run_etl_dir():

    args = parse_args()

    extractor = DataSetExtractor(cfg.FILES)
    transformer = DataSetTransformer(args.transformation)
    loader = DataSetDirectoryLoader(cfg.DATA_DIR, args.transformation)
    
    etl = ETLJob(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )

    status = etl.run()
    print(f"Job status: {status}")


if __name__ == "__main__":
    run_etl_dir()
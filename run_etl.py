import argparse
from framework.log import Logger
from etl_config import Config as cfg
from framework import (
    DataSetExtractor, DataSetTransformer, DataSetDBLoader,
    DataSetDirectoryLoader, ETLJob, time_func
)


def parse_args():
    parser = argparse.ArgumentParser("Choose transformation")
    parser.add_argument(
        "-t", "--transformation", metavar="", help="transformation" 
    )
    parser.add_argument(
        "-d", "--destination", metavar="", default="dir", help="db or dir" 
    )
    return parser.parse_args()


@time_func
def run_etl_dir():
    args = parse_args()
    logger = Logger().get_logger(
        f"ETL with {args.destination} destination"
    )

    extractor = DataSetExtractor(cfg.FILES)
    transformer = DataSetTransformer(args.transformation)
    if args.destination == "dir":
        loader = DataSetDirectoryLoader(cfg.DATA_DIR, args.transformation)
    else:
        loader = DataSetDBLoader(
            cfg.POSTGRES_SCHEMA, args.transformation, cfg.POSTGRES_CONFIG
        )

    etl = ETLJob(
        extractor=extractor, transformer=transformer, loader=loader
    )

    logger.info(f"Starting ETL Job - {args.transformation}")
    status = etl.run()
    logger.info(f"Job status - {status}")


if __name__ == "__main__":
    run_etl_dir()
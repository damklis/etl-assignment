from etl_config import Config as cfg
from framework import (
    DataSetExtractor, DataSetTransformer,
    DataSetDBLoader, ETLJob, time_func
)

from run_etl_dir import parse_args


@time_func
def run_etl_db():
    args = parse_args()

    extractor = DataSetExtractor(cfg.FILES)
    transformer = DataSetTransformer(args.transformation)
    loader = DataSetDBLoader(
        cfg.POSTGRES_SCHEMA,
        args.transformation,
        cfg.POSTGRES_CONFIG
    )
    
    etl = ETLJob(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )

    status = etl.run()
    print(f"Job status: {status}")


if __name__ == "__main__":
    run_etl_db()

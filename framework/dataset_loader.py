import os
from sqlalchemy import create_engine


class DataSetDirectoryLoader:
    def __init__(self, data_dir, filename):
        self._path = self.create_data_path(
            data_dir, filename
        )
    
    @staticmethod
    def create_data_path(data_dir, filename):
        print(f"Saving `{filename} into {data_dir}` location")
        if not filename.endswith(".csv"):
            return os.path.join(data_dir, f"{filename}.csv")
        return os.path.join(data_dir, filename)

    def load_dataset(self, dataset):
        dataset.to_csv(
            path_or_buf=self._path,
            sep=";",
            index=False
        )


class DataSetDBLoader:
    def __init__(self, schema, table, db_config):
        self._schema = schema
        self._table = table
        self._conn = self.create_db_conn(**db_config)

    @staticmethod
    def create_db_conn(user, password, host, port, db):
        try:
            url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
            engine = create_engine(url)
            conn = engine.connect()
            return conn
        except Exception as e:
            print(f"Can't connect to db, error {e}")
        
    def load_dataset(self, dataset):
        self.create_schema()
        print(f"Created schema {self._schema}")
        dataset.to_sql(
            name=self._table,
            con=self._conn,
            schema=self._schema,
            if_exists="append",
            index=False,
            chunksize=1000,
            method="multi"
        )
        print(f"Saved dataset into {self._table} table")

    def create_schema(self):
        self._conn.execute(
            f"CREATE SCHEMA IF NOT EXISTS {self._schema}"
        )

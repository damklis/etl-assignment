from time import time


from .log import log


@log
class ETLJob:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        try:
            self._execute_pipeline()
            return "SUCCESS"
        except Exception as err:
            self.logger.warning(f"Error message: {err}")
            return "FAILED"

    def _execute_pipeline(self):
        #EXTRACT
        raw_data = self.extractor.extract_dataset()
        #TRANSFORM
        dataset = self.transformer.transform_dataset(raw_data)
        #LOAD
        self.loader.load_dataset(dataset=dataset)


def time_func(function):

    def wrapper(*args, **kwargs):

        execution_start = time()
        result = function(*args, **kwargs)
        execution_end = time()

        execution_time = (execution_end - execution_start)
        print(f"Execution time: {execution_time:.2f} s")

        return result
    
    return wrapper

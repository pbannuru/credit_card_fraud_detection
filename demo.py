from credit.pipeline.pipeline import Pipeline
from credit.exception import creditException
from credit.config import configuration
from credit.logger import logging
from credit.config.configuration import *
def main():
    try:
        pipeline =Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = configuration().get_data_validation_config()
        # print(data_validation_config)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__ == "__main__":
    main()
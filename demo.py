from credit.pipeline.pipeline import Pipeline
from credit.exception import creditException
from credit.config import configuration
from credit.logger import logging
from credit.config.configuration import *
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline =Pipeline(configuration(config_file_path=config_path))
        # pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function completed")
        # data_validation_config = configuration().get_data_validation_config()
        # print(data_validation_config)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__ == "__main__":
    main()
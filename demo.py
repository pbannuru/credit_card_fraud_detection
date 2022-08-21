from credit.pipeline.pipeline import Pipeline
from credit.exception import creditException
from credit.config import configuration
from credit.logger import logging
def main():
    try:
        pipeline =Pipeline()

        pipeline.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__ == "__main__":
    main()
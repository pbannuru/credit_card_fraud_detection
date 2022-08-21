
from credit.config.configuration import Configuartion
from credit.logger import logging, get_log_file_name
from credit.exception import creditException
from credit.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from credit.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from credit.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from credit.component.data_ingestion import DataIngestion
import os, sys
import pandas as pd


class Pipeline:
   

    def __init__(self, config: Configuartion = Configuartion() ) -> None:
        try:
          
            self.config = config
        except Exception as e:
            raise creditException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise creditException(e, sys) from e

    def run_pipeline(self):
        try:
            #data_ingestion 

            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise creditException(e, sys) from e
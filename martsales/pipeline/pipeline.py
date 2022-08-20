
from martsales.config.configuration import Configuartion
from martsales.logger import logging, get_log_file_name
from martsales.exception import martsalesException
from martsales.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from martsales.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from martsales.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from martsales.component.data_ingestion import DataIngestion
import os, sys
import pandas as pd


class Pipeline:
   

    def __init__(self, config: Configuartion ) -> None:
        try:
          
            self.config = config
        except Exception as e:
            raise martsalesException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise martsalesException(e, sys) from e

    def run_pipeline(self):
        try:
            #data_ingestion 
            
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise martsalesException(e, sys) from e
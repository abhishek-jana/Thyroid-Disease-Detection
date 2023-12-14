from thyroid_detection.exception import ThyroidException
from thyroid_detection.logging import logger
from thyroid_detection.config.pipeline.training import ThyroidConfig
from thyroid_detection.component.training.data_ingesion import DataIngestion
from thyroid_detection.entity.artifact_entity import DataIngestionArtifact
import sys


class TrainingPipeline:

    def __init__(self, thyroid_detection_config: ThyroidConfig):
        self.thyroid_detection_config: ThyroidConfig = thyroid_detection_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.thyroid_detection_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise ThyroidException(e, sys)


    def start(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise ThyroidException(e, sys)
from thyroid_detection.exception import ThyroidException
import os, sys

from thyroid_detection.utils import read_yaml_file, write_yaml_file
from collections import namedtuple
from thyroid_detection.logging import logger
DataIngestionMetadataInfo = namedtuple("DataIngestionMetadataInfo", ["date", "data_file_path"])


class DataIngestionMetadata:

    def __init__(self, metadata_file_path,):
        self.metadata_file_path = metadata_file_path
    
       

    @property
    def is_metadata_file_present(self):
        return os.path.exists(self.metadata_file_path)

    def write_metadata_info(self, date: str, data_file_path: str):
        try:
            metadata_info = DataIngestionMetadataInfo(
                date=date,
                data_file_path=data_file_path
            )
            write_yaml_file(file_path=self.metadata_file_path, data=metadata_info._asdict())

        except Exception as e:
            raise ThyroidException(e, sys)

    def get_metadata_info(self) -> DataIngestionMetadataInfo:
        try:
            if not self.is_metadata_file_present:
                raise Exception("No metadata file available")
            metadata = read_yaml_file(self.metadata_file_path)
            metadata_info = DataIngestionMetadataInfo(**(metadata))
            logger.info(metadata)
            return metadata_info
        except Exception as e:
            raise ThyroidException(e, sys)
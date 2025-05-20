#updata components
import os
import urllib.request as request
import zipfile
from chicken_disease_prediction import logger
from chicken_disease_prediction.utils.common import get_size
from chicken_disease_prediction.entity.config_entity import DataIngestionConfig
from pathlib import Path

import gdown

def is_zipfile_valid(filepath):
    return zipfile.is_zipfile(filepath)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename = gdown.download(
                url=self.config.source_url,
                output=self.config.local_data_file,
                quiet=False,
                fuzzy=True
            )
            logger.info(f"{filename} downloaded successfully")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip file into the data directory
        function returns None
        """

        if zipfile.is_zipfile(self.config.local_data_file):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
                logger.info(f"Extracted all files to {self.config.unzip_dir}")
        else:
            logger.error("Downloaded file is not a valid zip file.")
            raise zipfile.BadZipFile("Downloaded file is not a valid zip file.")
            
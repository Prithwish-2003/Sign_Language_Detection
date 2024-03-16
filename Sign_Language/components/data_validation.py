import os,sys
import shutil
from Sign_Language.logger import logging
from Sign_Language.exception import CustomException
from Sign_Language.entity.config_entity import DataValidationConfig
from Sign_Language.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact)


class DataValidation:
    def __init__(self,
                 data_ingestion_artifact : DataIngestionArtifact,
                 data_validation_config : DataValidationConfig,):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config =  data_validation_config

        except Exception as e:
            raise CustomException(e,sys)
        
    def validate_all_file_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else :
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_validation(self)->DataValidationArtifact:
        logging.info("Entered initiate_data_validation method or DataValidation Class")
        try :
            status = self.validate_all_file_exist()
            data_validation_artifact=DataValidationArtifact(validation_status=status)
            logging.info("Exited initiate_Data_validation method of DataValidation class")
            logging.info(f"Data Validation artifact : {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_Zip_file_path,os.getcwd())

            return data_validation_artifact
        except Exception as e:
            raise CustomException(e,sys)
        


            

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_Zip_file_path:str
    feature_store_path:str

@dataclass
class DataValidationArtifact:
    validation_status:bool   
@dataclass
class ModelTrainerArtifact:
    trainer_model_file_path:str


@dataclass
class ModelPusherArtifacts:
    bucket_name:str
    s3_model_path:str

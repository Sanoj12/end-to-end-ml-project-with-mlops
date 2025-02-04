from dataclasses import  dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path 




###data validation

@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_dir:Path
    all_schema:dict




#######data transformation

@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_path :Path



#######model trainer 



@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name:str
    alpha:float  ###parameters-alpha ,liration,
    li_ratio:float
    target_column:str



    ###################model evaluation


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_Path: Path
    model_path: Path
    all_params:dict
    metric_file_name: Path
    target_column:str
    mlflow_url : str
    
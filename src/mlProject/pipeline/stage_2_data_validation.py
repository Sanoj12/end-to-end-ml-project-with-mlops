from mlProject import logger

from mlProject.components.data_validation import DataValidation
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.config.configuration import ConfigurationManager




STAGE_NAME = "Data Validation  Setup"


class DataValidationPipeline:

    def __init__(self):
        pass


    def main(self):
         config =ConfigurationManager()
         data_validation_config = config.get_data_validation_config()
         data_validation = DataValidation(config=data_validation_config)
         data_validation.validate_all_columns()
        


if __name__ == '__main__':
    try:
        logger.info(f"satge {STAGE_NAME} COMPLETED SUCCESFULLY" )
        obj = DataValidationPipeline()
        obj.main()

    except Exception as e:
        logger.error(f"Error in stage {STAGE_NAME} : {e}")
        raise e

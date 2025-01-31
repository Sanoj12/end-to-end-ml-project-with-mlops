from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
#from mlProject.entity.config_entity import DataIngestionConfig

from mlProject import logger


#define stage name

STAGE_NAME ="Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):

       config =ConfigurationManager()
       data_ingestion_config  = config.get_data_ingestion_config()
       data_ingestion = DataIngestion(config=data_ingestion_config)
       data_ingestion.download_file()
       data_ingestion .extract_zip_file()

    
      
if __name__ == "__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started!!")
        obj = DataIngestionPipeline()
        obj.main()

    except Exception as e:
        raise e
























    
 
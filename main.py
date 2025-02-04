from src.mlProject import logger 
from mlProject.pipeline.stage_1_data_ingestion import DataIngestionPipeline 

from mlProject.pipeline.stage_4_model_trainer import ModelTrainerPipeline






STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f"satge {STAGE_NAME} COMPLETED SUCCESFULLY" )
        obj = DataIngestionPipeline()
        obj.main()

except Exception as e:
        logger.error(f"Error in stage {STAGE_NAME} : {e}")
        raise e






# STAGE_NAME = "Model Trainer stage"

# try:
#         logger.info(f"satge {STAGE_NAME} COMPLETED SUCCESFULLY" )
#         obj = ModelTrainerPipeline()
#         obj.main()

# except Exception as e:
#         logger.error(f"Error in stage {STAGE_NAME} : {e}")
#         raise e






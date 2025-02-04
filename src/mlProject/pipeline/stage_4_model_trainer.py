

from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer



STAGE_NAME =" MODEL TRAINER SETUP"

class ModelTrainerPipeline:

    def __init__(self):
        pass


    def main(self):

        try:
             config = ConfigurationManager()
             model_trainer_config = config.get_model_trainer_config()
             model_trainer = ModelTrainer(config=model_trainer_config)
             model_trainer.train()
        
        except Exception as e:

            raise e




if __name__ == '__main__':
    try:
        logger.info(f"satge {STAGE_NAME} COMPLETED SUCCESFULLY" )
        obj = ModelTrainerPipeline()
        obj.main()

    except Exception as e:
        logger.error(f"Error in stage {STAGE_NAME} : {e}")
        raise e

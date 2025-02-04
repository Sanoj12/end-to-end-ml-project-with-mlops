from mlProject import logger
from mlProject.config.configuration import ConfigurationManager

from mlProject.components.model_evaluation import ModelEvaluation 


STAGE_NAME = "MODEL EVALUATION SETUP"


class ModelEvaluationPipeline:

    def __init__(self):
        pass


    def main(self): 

           
        try:
              config = ConfigurationManager()
              model_evaluation_config = config.get_model_evaluation_config()
              model_evaluation = ModelEvaluation(config=model_evaluation_config)
              model_evaluation.log_into_mlflow()

        except Exception as e:
               raise e




if __name__ == '__main__':
    try:
        logger.info(f"satge {STAGE_NAME} COMPLETED SUCCESFULLY" )
        obj = ModelEvaluationPipeline()
        obj.main()

    except Exception as e:
        logger.error(f"Error in stage {STAGE_NAME} : {e}")
        raise e

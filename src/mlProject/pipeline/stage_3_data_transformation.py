from mlProject import logger

from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from pathlib import Path

STAGE_NAME = "Data Transformation setup"


class DataTransformationPipeline:

    def __init__(self):
        pass


    def main(self):
        try:

            with open(Path("artifact/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]

            
            if status == "True":

                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformer_config()

                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()

            else:
                raise Exception("you data schema is not vaild")
            

        except Exception as e:
            raise e
        


if __name__ == "__main__":
    try:

        logger.info(f"stage {STAGE_NAME} started!!!")
        obj =DataTransformationPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} COMPLETED!!!")


    except Exception as e:

        raise e
        
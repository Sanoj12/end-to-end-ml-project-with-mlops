import os
from box.exceptions import BoxValueError
import yaml


from mlProject import logger

import json

import joblib

#from ensure import ensure_annotations
#from enforce import runtime_validation

from box import ConfigBox

from pathlib import Path

from typing import Any





#@ensure_annotations
def read_yaml(path_to_yaml:Path) ->ConfigBox:

    #Reads a YAML file and converts it into a ConfigBox.

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            logger.info(f"yaml file :{path_to_yaml} loaded successfully!")

    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:

        raise e



#@ensure_annotations

def create_directories(path_to_directories:list):


    for path in path_to_directories:
        os.makedirs(path ,exist_ok=True)

        logger.info(f"created directory at :{path}")






def save_json(path:Path ,data:dict):
    #DICTIONARY  -data to be saved in json file


    with open(path , "w") as f:

        json.dump(data ,f,indent=4)


        logger.info(f"json file saved at: {path}")






def load_json(path: Path) -> ConfigBox:
 
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)





def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")






def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data





def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
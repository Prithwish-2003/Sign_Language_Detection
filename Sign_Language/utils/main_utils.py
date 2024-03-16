import os.path
import sys
import yaml
import base64

from Sign_Language.exception import CustomException
from Sign_Language.logger import logging


def read_yaml_file(file_path:str) -> dict:
    try :
        with open(file_path,"rb") as yaml_file:
            logging.info("read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except  Exception as e:
        raise CustomException(e,sys)
    
def write_yaml_file(file_path:str,content:object,replace:bool=False) ->None:
    try :
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
            logging.info("successfully write yaml file")
            
    except  Exception as e:
        raise CustomException(e,sys)

def decodeImages(imgSting,fileName):
    imgData = base64.b64decode(imgSting)
    with open("./data/" + fileName,'wb') as f:
        f.write(imgData)
        f.close()
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64decode(f.read())      


import pandas as pd
import os
import mlflow.sklearn
import mlflow
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from urllib.parse import urlparse
from mlProject.utils.common import save_json
from pathlib import path 

from mlProject.entity.config_entity import ModelEvaluationConfig





class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config



    def eval_metrics(self,actual ,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2_score = r2_score(actual,pred)

        return rmse, mae , r2_score     
    



    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_Path)
        model = joblib.load(self.config.model_path)


        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_qualitites = model.predict(test_x)
 
            rmse, mae, r2_score = self.eval_metrics(test_y, predicted_qualitites)

            scores = {"rmse":rmse, "mae":mae, "r2_score":r2_score} 

            save_json(path=Path(self.config.metric_file_name),data=scores)


            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2_score", r2_score)


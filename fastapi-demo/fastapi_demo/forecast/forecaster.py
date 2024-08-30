import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
import joblib
import sys
import os
import pvlib
from pvlib.location import Location
from pvlib.irradiance import get_total_irradiance
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
import logging
from ..io.s3 import S3Client


logger = logging.getLogger(__name__)

class Forecaster(object):
    bucket = 'cfex-dev-se-settlement'

    def __init__(self) -> None:
        self.s3_client = S3Client()
        self.load_model()


    def load_model(self):
        # Define the path relative to the current notebook location
        # the PWD is like "/Users/taoxiao/Downloads/ML/generation-prediction-service/notebooks"
        logger.info(f"开始加载模型 ... 当前工作目录是 {os.getcwd()}")

        ################## load the wind power generation model
        local_path = self.s3_client.download(self.bucket, "ml/haystack_wind_generationy_prediction_15mins_model.pkl")

        logger.info('开始加载 model_haystack_wind_generation_prediction')
        model_haystack_wind_generation_prediction = joblib.load(local_path)
        logger.info('完成加载 model_haystack_wind_generation_prediction')

        ################## load the feature names
        local_path = self.s3_client.download(self.bucket, 'ml/haystack_wind_generation_prediction_15mins_feature_names.json')

        # Step 1: Read the JSON file
        # Assuming the JSON file is named 'data.json' and located in the current directory
        with open(local_path) as f:
            logger.info('开始加载 generation_prediction_model_feature_names')
            generation_prediction_model_feature_names = json.load(f)
            logger.info('完成加载 generation_prediction_model_feature_names')

        #################### Load weather api data
        local_path = self.s3_client.download(self.bucket, 'ml/haystack_wind_spreadout_15mins_20240701-20240731_weather_api_history.csv')
        logger.info('开始加载 df_weather_api')
        df_weather_api = pd.read_csv(local_path)
        logger.info("完成加载 df_weather_api")

        #################### Load Mateomatics data
        local_path = self.s3_client.download(self.bucket, 'ml/haystack_wind_spreadout_15mins_20231001-20240731_history.csv')
        logger.info('开始加载 df_meteomatics')
        df_meteomatics = pd.read_csv(local_path)
        logger.info("完成加载 df_meteomatics")

        df_meteomatics['timestamp_chicago'] = pd.to_datetime(df_meteomatics['timestamp_chicago'])

        # Define the start and end dates for the filter
        start_date = pd.Timestamp('2024-07-01T00:00:00', tz='America/Chicago')
        end_date = pd.Timestamp('2024-07-31T23:59:59', tz='America/Chicago')

        # Step 4: Apply the filter
        df_meteomatics = df_meteomatics[(df_meteomatics['timestamp_chicago'] >= start_date) & (df_meteomatics['timestamp_chicago'] <= end_date)].reset_index(drop=True)

        ################### Merge meteomatics and weather api
        df_merge = pd.concat([df_meteomatics, df_weather_api], axis=1)
        prediction = model_haystack_wind_generation_prediction.predict(
            df_merge[generation_prediction_model_feature_names]
            )
        
        logger.info(f"完成预测结果计算")
        
        self.prediction = prediction
    

    def predict(self, index: int):
        return self.prediction[index]

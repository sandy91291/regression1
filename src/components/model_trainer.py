import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso,ElasticNet
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_model
import os
from dataclasses import dataclass
import sys
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl') # Path to save the trained model
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig() # Initialize the model trainer configuration
        
        
        
    def initiate_model_trainer(self, train_arr, test_arr, preprocessor_path):
        try:
            logging.info('Model Trainer initiated')
            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1], train_arr[:, -1], test_arr[:, :-1], test_arr[:, -1]
            )
            
            logging.info('Training and Testing data split completed')
            
            models = {
                'Linear Regression': LinearRegression(),
                'Ridge': Ridge(),
                'Lasso': Lasso(),
                'ElasticNet': ElasticNet()
            }
            
            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)
            
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = max(sorted(model_report.values()))
            
            logging.info(f'Best Model: {best_model_name} with score: {best_model_score}')
            
            if best_model_score < 0.6:
                raise CustomException("No suitable model found")
            
            best_model = models[best_model_name]
            
            save_object(self.model_trainer_config.trained_model_file_path, best_model)
            save_object(preprocessor_path, preprocessor_path)  # Save the preprocessor
            
            return best_model_name, best_model_score
        
        except Exception as e:
            logging.info('Exception occurred during model training')
            raise CustomException(e, sys)
    
## this code will contain all the things related to the model training like this may include confusion matrix for classification, finding the r^2 for regression problems
import sys
import os
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', "model.pkl")

class Modeltrainer:
    def __init__(self) -> None:
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_Train, y_train, X_test, y_test = (
                 train_array[:,:-1],# remove the last column and store everything in X_Train 
                 train_array[:,-1],#the last column value will be stored in y_train
                 test_array[:,:-1],
                 test_array[:,-1],
            )
            #dictionary of models
            models = {
                "Random Forest": RandomForestRegressor(),
                "Descision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K neighbours Classifier": KNeighborsRegressor(),
                "XGBclassifier": XGBRegressor(),
                "Catboosting classifier": CatBoostRegressor(),
                "Adaboost Classifier": AdaBoostRegressor(),
            }
            model_report:dict=evaluate_models(X_train=X_Train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models)
            ##to get best model score from dictionary of models
            best_model_score= max(sorted(model_report.values()))

            ## to get best model name from dictionary of models
            best_model_name= list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model= models[best_model_name]

            if best_model_score <0.60:
                raise CustomException("No Better model found")
            logging.info("Best found model on both training and testing dataset")
            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
        except Exception as e:
            raise CustomException(e,sys)

import os
import yaml
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score
from sklearn.linear_model import ElasticNet
import joblib
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error


def eval_metrics(actual, predicted):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    return rmse, mae, r2


def train_and_evaluate(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    target = config["base"]["target_col"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dirs"]["model_dir"]
    alpha_values = np.logspace(-3, 1, 20)  # Adjust the range for alpha values
    l1_ratio_values = np.linspace(0.1, 0.9, 20)  # Adjust the range for l1_ratio values

    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    train_y = train[target]
    test_y = test[target]

    imputer = SimpleImputer(strategy='mean')
    train_x = imputer.fit_transform(train_x)
    test_x = imputer.transform(test_x)

    param_grid = {
        'alpha': alpha_values,
        'l1_ratio': l1_ratio_values
    }

    lr = ElasticNet(random_state=random_state)
    grid_search = GridSearchCV(lr, param_grid, scoring='r2', cv=10)
    grid_search.fit(train_x, train_y)

    best_alpha = grid_search.best_params_['alpha']
    best_l1_ratio = grid_search.best_params_['l1_ratio']

    print("Best alpha:", best_alpha)
    print("Best l1_ratio:", best_l1_ratio)

    lr_best = ElasticNet(alpha=best_alpha, l1_ratio=best_l1_ratio, random_state=random_state)
    lr_best.fit(train_x, train_y)

    predicted_qualities = lr_best.predict(test_x)
    r2_score = r2_score(test_y, predicted_qualities)

    print("R-squared Score (Accuracy):", r2_score)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(lr_best, model_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml", help="Path to the config file")
    args = parser.parse_args()
    train_and_evaluate(config_path=args.config)

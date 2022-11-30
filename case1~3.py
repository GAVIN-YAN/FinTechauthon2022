import csv
import math
import time
import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xgboost
import seaborn as sns
from matplotlib import pyplot
from numpy import loadtxt
from xgboost import XGBRegressor, plot_importance
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn import tree



dataset = pd.read_csv("/home/yanfeng/fate/FL_data/case1")
dataset.info()
X = dataset.values[:, 1:-1]
Y = dataset.values[:, -1]
seed = 7



test_size = 0.3
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

enumeration = 0
start = time.perf_counter()

if enumeration == 1:
    model = XGBRegressor(
        # learning_rate=0.1,  # 占比
        # max_depth=5,
        # subsample=0.8,  # 随机选择样本
        # colsample_bytree=0.8,  # 随机特征
        # reg_alpha=0,                    # L1
        # reg_lambda=1,                   # l2

        n_estimators=1000,  # 多少棵树
        objective="reg:squarederror",
        gamma=0,  # Lsplit
        seed=27,
        gpu_id=0,
        # silent=0,                   # 输出运行信息
        # min_child_weigh=1,          # 叶子结点中的最小样本数
        # verbosity=1
    )

    # 网格搜索
    parameters = {
        'max_depth': [5, 10, 15, 20],
        'learning_rate': [0.01, 0.02, 0.05, 0.1],
        'subsample': [0.8, 0.85, 0.95, 1],
        'colsample_bytree': [0.6, 0.8, 0.9, 1],
        'reg_alpha': [0, 0.25, 0.5, 1],
        'reg_lambda': [0.2, 0.4, 0.8, 1],
    }

    gsearch = GridSearchCV(model, param_grid=parameters, scoring='neg_mean_squared_error',
                           cv=KFold(n_splits=5, shuffle=True))
    gsearch.fit(X, Y)
    print("Best: %.15f using %s" % (gsearch.best_score_, gsearch.best_params_))
    # means = gsearch.cv_results_['mean_test_score']
    # params = gsearch.cv_results_['params']
    # for mean, param in zip(means,params):
    #     print("%.15f  with:   %r" % (mean, param))
else:
    model = XGBRegressor(
        learning_rate=0.02,  # 占比
        max_depth=5,
        subsample=0.8,  # 随机选择样本
        colsample_bytree=1,  # 随机特征
        reg_alpha=0,  # L1
        reg_lambda=0.4,  # l2
        n_estimators=1000,  # 多少棵树
        objective="reg:squarederror",
        gamma=0,  # Lsplit
        seed=27,
        gpu_id=-1,
        # silent=0,                   # 输出运行信息
        # min_child_weigh=1,          # 叶子结点中的最小样本数
        # verbosity=1
    )

    model.fit(X_train, Y_train,
              early_stopping_rounds=10,
              eval_metric=["rmse", "mae"],
              eval_set=[(X_train, Y_train), (X_test, Y_test)],
              verbose=True)

    eval_dict = model.evals_result()
    val0 = eval_dict['validation_0']['rmse']
    val1 = eval_dict['validation_1']['rmse']


    Y_pred = model.predict(X_test)
    # save_ytest_scatter(Y_test, Y_pred)


end = time.perf_counter()
print("final is in : %s Seconds " % (end - start))


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 07:19:51 2023

@author: anirbanroy16
"""

from sklearn.linear_model import Ridge, Lasso
#from sklearn import linear_model
import pandas as pd
import warnings
from sklearn.model_selection import  GridSearchCV

T=243.15

data = pd.read_csv ('BIGMAP_le_243K_with_r.csv')
data['x1'] = data['r']**0.5*(data['c'])**2.5
data['x2'] = data['c']**0.5*T**2

data_train = data.loc[data.r!=1,:]

# in sync with Flores et al, use data other than 100% propylene carbonate in the electrolyte to train, 
# and 100% to test. This was done to directly compare with Flores et al.


X = data_train[['c', 'x1', 'x2']]
Y = data_train['S']

# range of regularization parameters

param_grid = {
        "alpha": [
            0.00001,
            0.0001,
            0.001,
            0.01,
            0.1,
            1.0,
            2.5,
            5.0,
            10.0,
            25.0,
            50.0,
            100.0,
            250.0,
            500.0,
            1000.0,
            2500.0,
            5000.0,
            10000.0,]
    }

reg_ridge = Ridge()
reg_lasso = Lasso()

with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        gsmodel_ridge = GridSearchCV(reg_ridge, param_grid, scoring="neg_mean_squared_error", cv=5)
        gsmodel_ridge.fit(X, Y)
        
        gsmodel_lasso = GridSearchCV(reg_lasso, param_grid, scoring="neg_mean_squared_error", cv=5)
        gsmodel_lasso.fit(X, Y)

data_test = pd.read_csv ('BIGMAP_le_243K_r_eq_1.csv')
data_test['x1'] = data_test['r']**0.5*(data_test['c'])**2.5
data_test['x2'] = data_test['c']**0.5*T**2

test_matrix = data_test[['c', 'x1', 'x2']]

prediction_ridge = gsmodel_ridge.predict(test_matrix)
prediction_lasso = gsmodel_lasso.predict(test_matrix)


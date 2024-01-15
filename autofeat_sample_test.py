# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:44:04 2023

@author: anirbanroy16
"""
#%%

import pandas as pd
from autofeat import AutoFeatRegressor
from sklearn.model_selection import train_test_split




data = pd.read_csv ('BIGMAP_le_243K_with_r.csv')
data = data.loc[data.r!=1,:]

    
# --------------  HYPER-PARAMETERS FEATURE GENERATION -------------------

#how to scale data. Supported 'standard_nomean', 'standard', 'none'
SCALING_TYPE = 'standard_nomean' 

#whether to leave intercept to vary freely (True) or constrain its value to y0 = 0 (False).
FIT_INTERCEPT = False

# Autofeat hyperparameter.
# number of times features are combined to obtain ever more complex features.
# example FEATENG_STEPS = 3 with sqrt transformations will find terms like sqrt(sqrt(sqrt(x)))
FEATENG_STEPS = 5

# Autofeat hyperparameter.
# Units of predictors. Keys must match column names in dataframe. 
# Ignored predictors are assumed to be dimensionless.
UNITS = {"T": "K",
        "c": "mol/kg"}

# Autofeat hyperparameter.
# Number of iterations for filtering out generated features.
FEATSEL_RUNS = 3

# Autofeat hyperparameter.
# Set of non-linear transformations to be applied to initial predictors.
# Autofeat documents these possible transformations: ["1/", "exp", "log", "abs", "sqrt", "^2", "^3", "1+", "1-", "sin", "cos", "exp-", "2^"].
# Autofeat throws an error when using a single transformation. 
# Repeat your transformation as a workaround if you only want o use one.
#TRANSFORMATIONS = ["sqrt", "sqrt"]


# --------------  HYPER-PARAMETERS FEATURE SELECTION -------------------

# n-standard deviations criterion to choose optimal alpha from Cross Validation. 
# Higher STD_ALPHA lead to sparser solutions.
STD_ALPHA = 1 

#t-statistic rejection threshold. Coefficients with t-statistic < REJECTION_THR are rejected.
REJECTION_THR = 2 

#%%

data_train, data_test = train_test_split(data, test_size=0.1, random_state=12)

#%%

afreg = AutoFeatRegressor(verbose = 1, feateng_steps = FEATENG_STEPS,
                        units =  UNITS,featsel_runs = FEATSEL_RUNS)

data_train_x  = data_train[['r','c']]
#data_train_x = np.reshape (data_train['salt_load'], (-1,1))

data_train_y = data_train['S']

reg_train = afreg.fit_transform(data_train_x, data_train_y)

#%%

data_test = pd.read_csv ('BIGMAP_le_243K_r_eq_1.csv')
#data_test = data.loc[data.r==1,:]
data_test_x = data_test[['r','c']] 
test = afreg.transform(data_test_x)

#%%

prediction = afreg.predict(test)

#%%















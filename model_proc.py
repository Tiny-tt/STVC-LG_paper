# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:15:11 2023

@author: tt
"""

import pandas as pd
import numpy as np
from autogluon.tabular import TabularDataset, TabularPredictor

data_pm25 = pd.read_csv('./csv_data/china_pm25_2020_xev.csv')
variables_pm25 = pd.read_csv('./selection_proc/variables_pm25.csv')

data_pm25 = data_pm25.loc[:, ['pm'] + list(variables_pm25.loc[:, 'variables'])]

label = 'pm'

save_path_pm25 = 'D:/stsvc_pm25_model'
predictor_pm25 = TabularPredictor(label=label, path=save_path_pm25).fit(data_pm25, fit_weighted_ensemble=False, 
                                                              hyperparameters={'GBM': {}}, num_bag_folds=8)
fit_pm25_model_name = predictor_pm25.get_model_names()[-1]
print('done')
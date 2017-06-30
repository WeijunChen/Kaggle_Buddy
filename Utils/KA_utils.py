from __future__ import print_function, division
import gc
import time
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
from IPython.display import display
from pandas_summary import DataFrameSummary


class tick_tock:
    def __init__(self, process_name):
        self.process_name = process_name
    def __enter__(self):
        print(self.process_name + " begin ......")
        self.begin_time = time.time()
    def __exit__(self, type, value, traceback):
        end_time = time.time()
        print(self.process_name + " end ......")
        print('time lapsing {0} s \n'.format(end_time - self.begin_time))


def ka_get_NC_col_names(data):
    '''Get column names of category and numeric

    Parameters
    ----------
    data: pandas dataframe

    Return:
    ----------
    numerics_cols: numeric column names
    category_cols: category column names

    '''
    numerics_cols = data.select_dtypes(exclude=['O']).columns.tolist()
    category_cols = data.select_dtypes(include=['O']).columns.tolist()
    return numerics_cols, category_cols

def pickle_dump(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

def pickle_load(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def ka_xgb_r2_error(preds, dtrain):
    labels = dtrain.get_label()
    return 'error', r2_score(labels, preds)

def ka_is_numpy(df):
    '''Check if a object is numpy

       Parameters
       ----------
       df: any object
    '''
    return type(df) == np.ndarray
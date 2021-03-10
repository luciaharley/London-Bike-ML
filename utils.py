import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

"""
Various user-defined functions and classes needed to run the pipeline.
"""

class DummyEstimator(BaseEstimator):
    def fit(self): pass
    def score(self): pass


def split_dates(X):
    """
    Add columns for day of week, day of month, hour and month.
    """
    df = pd.DataFrame(X)
    X = df.iloc[:,0]
    X = pd.to_datetime(X, yearfirst=True)
    hour = X.dt.hour
    day_of_month = X.dt.day
    day_of_week = X.dt.dayofweek
    month = X.dt.month
    out = pd.concat([hour, day_of_month, day_of_week, month], 
                    keys=['hour','day_of_month', 'day_of_week', 'month'], axis=1)

    return out

# Test for split dates
X = pd.DataFrame({'timestamp': ['2021-03-02 00:00:00']})

target=pd.DataFrame({'hour': [0], 'day_of_month': [2], 'day_of_week': [1], 'month': [3]})

X_split =  split_dates(X) 
pd.testing.assert_frame_equal(X_split, target)
    

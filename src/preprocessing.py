import pandas as pd
import numpy as np
import re
from sklearn.base import BaseEstimator, TransformerMixin

class UniversalSizeCleaner(BaseEstimator, TransformerMixin):

    def __init__(self, column='product_size'):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        def to_oz(value):
            if pd.isna(value):
                return np.nan

            value = str(value).upper().strip()

            if any(x in value for x in ['NO TAG', '#', 'KH']):
                return np.nan

            match = re.search(r'\d+(\.\d+)?', value)
            if not match:
                return np.nan

            num = float(match.group())

            if 'LB' in value or 'POUND' in value:
                return num * 16
            elif 'OZ' in value or 'OUNCE' in value:
                return num
            else:
                return np.nan

        new_col = self.column + '_clean'
        X[new_col] = X[self.column].apply(to_oz)

        X.drop(columns=[self.column], inplace=True)

        return X


from sklearn.base import BaseEstimator, TransformerMixin

class SizeImputer(BaseEstimator, TransformerMixin):

    def __init__(self, column='product_size_clean'):
        self.column = column
        self.median_ = None

    def fit(self, X, y=None):
        self.median_ = X[self.column].median()
        return self

    def transform(self, X):
        X = X.copy()
        X[self.column] = X[self.column].fillna(self.median_)
        return X
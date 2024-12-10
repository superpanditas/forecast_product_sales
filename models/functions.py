'''Importing libraries'''
import pandas as pd
from pandas import DataFrame, Series 
from datetime import timedelta
import numpy as np
import sys 
import os

# Loading CSV
def load_dataset(path: str) -> DataFrame:
    df = pd.read_csv(path)
    return df

# reshape dataframe: From wide to long dataframe 
def wide_to_long(df: DataFrame) -> DataFrame:
    # define variables
    id_vars = ['Scode', 'Pcode', 'Price']
    value_var = ['Wk'+str(i) for i in range(0,104)]
    var_name = 'weekly'
    value_name = 'units'

    rename_columns = ['store', 'item', 'price', 'weekly', 'units']
    df = df.melt(id_vars=id_vars,
                value_vars=value_var,
                var_name=var_name,
                value_name=value_name)

    df.columns = rename_columns
    return df

# assign real dates: map weekly columns to real dates
def map_dates(weekly):
    init_week = pd.to_datetime('2023-01-07')
    week_num = int(weekly[2:])
    return init_week + timedelta(weeks=week_num)

def hello_world():
    print('Hello world!')
import ast
import pandas as pd

def df_final_styling(df, col_name):
    sdf = df
    new_col = ['$ '+str(round(val, 2)) for val in df[col_name]]
    sdf[col_name] = new_col
    return sdf


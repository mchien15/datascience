import os
import pandas as pd
dir = os.listdir('data/players')
for file in dir:
    a = file.split('.')[0]
    path_csv='data/players/' +file
    path_parquet='data/players/' +a+'.parquet'
    dr=pd.read_csv(path_csv)
    dr=dr.drop(columns=['xAG.1','PrgC.1','PrgP.1'])
    dr.to_parquet(path_parquet)

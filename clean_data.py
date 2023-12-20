import os
import pandas as pd
dir = os.listdir('data/players')
for file in dir:
    a = file.split('.')[0]
    path_csv='data/players/' +file
    path_parquet='data/players/' +a+'.parquet'
    dr=pd.read_csv(path_csv)

    dict_ = {
        'Cmp%' : 'CmpPct',
        'Cmp.1': 'Cmp1',
        'Cmp.2': 'Cmp2',
        'Cmp.3': 'Cmp3',
        'Att.1': 'Att1',
        'Att.2': 'Att2',
        'Att.3': 'Att3',
        'Cmp%.1': 'CmpPct1',
        'Cmp%.2': 'CmpPct2',
        'Cmp%.3': 'CmpPct3',
        'TO.1': 'TO1',
        'Tkl+Int': 'TklPlusInt',
        'Def Pen': 'DefPen',
        'Succ%': 'SuccPct',
        'Tkld%': 'TkldPct',
    }

    dr.rename(columns=dict_, inplace=True)
    dr=dr.drop(columns=['xAG.1','PrgC.1','PrgP.1'])
    dr.to_parquet(path_parquet)

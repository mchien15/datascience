import pandas as pd
import hashlib
from collections import Counter
from unidecode import unidecode

def process_dataframe(df):
    pd.set_option('display.max_columns', None)
    
    percentage_columns = ['Cmp%', 'Cmp%.1', 'Cmp%.2', 'Cmp%.3', 'DribTackled%', 'SuccPress%', 'Succ%', 'Rec%']
    to_delete_columns = ['Round', 'Venue', 'Result', 'Opponent', 'Start']
    
    df = df.fillna(0)

    df = df.drop(to_delete_columns, axis=1)
    df['Pos'] = df['Pos'].apply(lambda x: x.split(','))
    
    for col in percentage_columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col].str.rstrip('%'), errors='coerce') / 100
    
    numeric_columns = df.select_dtypes(include='number').columns.difference(['Name', 'Squad', 'Min'] + percentage_columns)
    
    df = df.drop('Date', axis=1)
    
    grouped_df_min_and_pos = df.groupby(['Name', 'Squad']).agg({
        'Pos': lambda x: list([item for sublist in x for item in sublist]),
        'Min': 'sum',
    }).reset_index()
    
    grouped_df_min_and_pos['Pos'] = grouped_df_min_and_pos['Pos'].apply(lambda x: [item[0] for item in Counter(x).most_common(3)])

    df = df.merge(grouped_df_min_and_pos, on=['Name', 'Squad'], how='left')
    df = df.drop(['Pos_x'], axis=1)
    df = df.rename(columns={'Pos_y': 'Pos'})
    
    test = df.groupby(['Name', 'Squad', 'Min_y']).agg({
        'Min_x': 'sum',
        # 'Pos': lambda x: set([item for sublist in x for item in sublist]),
        'Pos': 'first',
        **{col: 'sum' for col in numeric_columns},
        **{col: 'mean' for col in percentage_columns}
    }).reset_index()
    
    processed_df = test.drop(['Min_x'], axis=1)
    processed_df = processed_df.rename(columns={'Min_y': 'Min'})

    processed_df = processed_df[processed_df['Min'] >= 500]
    
    for col in numeric_columns:
        processed_df[col] = processed_df[col] / processed_df['Min'] * 90

    #apply unidecode to remove all the accent in the name
    processed_df['Name'] = processed_df['Name'].apply(lambda x: unidecode(x))

    #make hashing of each player by name and squad and add it as the first column
    processed_df.insert(0, 'player_id', processed_df['Name'].astype(str) + processed_df['Squad'].astype(str))
    processed_df['player_id'] = processed_df['player_id'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
    
    return processed_df

#argparse to input the path of the folder contains csv file, process all the file in that folder, concatenate them and save it as a csv file
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    
    import os
    files = os.listdir(args.path)
    df = pd.DataFrame()
    for file in files:
        df = df._append(pd.read_csv(os.path.join(args.path, file)))
    processed_df = process_dataframe(df)
    processed_df.to_csv(args.output, index=False)
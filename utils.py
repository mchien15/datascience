import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from soccerplots.radar_chart import Radar
import ast

stats_to_compare = {'FW': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'PassProg', 'AttPen', 'KP', 'PPA', 'Succ%', 'CPA', 'TacklesAtt3rd', 'Press'],
                    'WB': ['CrsPA', 'xA', 'SCA', 'PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Succ%', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'RB': ['CrsPA', 'xA', 'SCA', 'PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Succ%', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'LB': ['CrsPA', 'xA', 'SCA', 'PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Succ%', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'CB': ['PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Cmp%.3', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'DM': ['PassAtt', 'Cmp%', 'PassProg', 'PassFinThird', 'KP', 'ProgCarries', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'CM': ['npxG', 'xA', 'SCA', 'Sh', 'PassAtt', 'Cmp%', 'PassProg', 'PassFinThird', 'KP', 'ProgCarries', 'Succ%', 'CPA', 'Int', 'TklW', 'Blocks', 'TacklesMid3rd'],
                    'AM': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'PassAtt', 'Cmp%', 'PassProg', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'AttPen', 'TacklesAtt3rd', 'Press'],
                    'LM': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press'],
                    'RM': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press'],
                    'RW': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press'],
                    'LW': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press']}

@st.cache_data
def load_data():
    df = pd.read_csv('all_processed.csv')

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    numerical_cols = numerical_cols[numerical_cols != 'Min']

    scaler = StandardScaler()
    scaled_df = df.copy()
    scaled_df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    vector_embeddings = scaled_df[numerical_cols].values

    similarity_matrix = cosine_similarity(vector_embeddings)

    similarity_df = pd.DataFrame(similarity_matrix, index=scaled_df['Name'], columns=scaled_df['Name'])

    return df, scaled_df, similarity_df

def get_similar_players_cosine(df, similarity_df, player_name, top_n=10):
    similarity_scores = similarity_df[player_name]

    most_similar_players = similarity_scores.sort_values(ascending=False).head(top_n + 1)

    most_similar_players = most_similar_players[most_similar_players.index != player_name]

    similar_players_df = pd.DataFrame(most_similar_players).join(df.set_index('Name')[['Pos', 'Squad']])

    similar_players_df.reset_index(inplace=True)  # Reset the index

    similar_players_df.columns = ['Name', 'Similarity', 'Position', 'Squad']  # Add 'Name' column

    similar_players_df.sort_values(by='Similarity', ascending=False, inplace=True)  # Sort by similarity scores

    similar_players_df.reset_index(drop=True, inplace=True)  # Reindex from 0 to top_n

    similar_players_df.index += 1  # Reindex from 1 to top_n

    return similar_players_df

def get_similar_players_knn(df, player_name, top_n=10):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    numerical_cols = numerical_cols[numerical_cols != 'Min']

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    knn = NearestNeighbors(n_neighbors=top_n + 1, metric='euclidean')
    knn.fit(df[numerical_cols])

    player_index = df[df['Name'] == player_name].index[0]
    _, indices = knn.kneighbors(df.iloc[player_index][numerical_cols].values.reshape(1, -1))

    similar_players_df = df.iloc[indices[0][1:top_n+1]][['Name', 'Pos', 'Squad']]

    similar_players_df.reset_index(drop=True, inplace=True)

    similar_players_df.index += 1

    similar_players_df.columns = ['Name', 'Position', 'Squad']

    return similar_players_df

def compare_players(df, player1, player2):
    positions_set = ast.literal_eval(df[df['Name'] == player1]['Pos'].values[0])
    params = list(positions_set)[0]

    if params not in stats_to_compare:
        print(f"Position '{params}' is not available for comparison.")
        return None

    value1 = df[df['Name'] == player1][stats_to_compare[params]].values
    value2 = df[df['Name'] == player2][stats_to_compare[params]].values

    values = [value1[0], value2[0]]

    #get the range of values for each column in cols
    ranges = []
    for col in stats_to_compare[params]:
        ranges.append([df[col].min(), df[col].max()])

    title = dict(
        title_name=player1 + ' - ' + params,
        title_color='#B6282F',
        subtitle_name=df[df['Name'] == player1]['Squad'].values[0],
        subtitle_color='#B6282F',
        title_name_2=player2 + ' - ' + params,
        title_color_2='#344D94',
        subtitle_name_2=df[df['Name'] == player2]['Squad'].values[0],
        subtitle_color_2='#344D94',
        title_fontsize=18,
        subtitle_fontsize=15,
    )

    radar = Radar()

    fig, ax = radar.plot_radar(ranges=ranges, params=stats_to_compare[params], values=values, 
                            radar_color=['#B6282F', '#344D94'], 
                            title=title,
                            compare=True)

    return fig
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

@st.cache_data
def load_data():
    df = pd.read_csv('all_processed.csv')

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    vector_embeddings = df[numerical_cols].values

    similarity_matrix = cosine_similarity(vector_embeddings)

    similarity_df = pd.DataFrame(similarity_matrix, index=df['Name'], columns=df['Name'])

    return df, similarity_df

def get_similar_players_cosine(df, similarity_df, player_name, top_n=10):
    similarity_scores = similarity_df[player_name]

    most_similar_players = similarity_scores.sort_values(ascending=False).head(top_n + 1)

    most_similar_players = most_similar_players[most_similar_players.index != player_name]

    similar_players_df = pd.DataFrame(most_similar_players).join(df.set_index('Name')[['Pos', 'Squad']])

    similar_players_df.columns = ['Similarity', 'Position', 'Squad']

    return similar_players_df

def get_similar_players_knn(df, player_name, top_n=10):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    knn = NearestNeighbors(n_neighbors=top_n + 1, metric='euclidean')
    knn.fit(df[numerical_cols])

    player_index = df[df['Name'] == player_name].index[0]
    _, indices = knn.kneighbors(df.iloc[player_index][numerical_cols].values.reshape(1, -1))

    similar_players_df = df.iloc[indices[0][1:]][['Name', 'Pos', 'Squad']]
    similar_players_df.columns = ['Name', 'Position', 'Squad']

    return similar_players_df


st.title("Player Similarity (2020/2021 Season)")

df, similarity_df = load_data()

player_name = st.selectbox('Select a player', df['Name'].unique())

top_n = st.slider('Select number of similar players to display', min_value=1, max_value=50, value=10)

if st.button('Get Similar Players'):
    similar_players_cosine = get_similar_players_cosine(df, similarity_df, player_name, top_n)
    st.write("Similar Players (Cosine Similarity):")
    st.write(similar_players_cosine)

    similar_players_knn = get_similar_players_knn(df, player_name, top_n)
    st.write("Similar Players (KNN):")
    st.write(similar_players_knn)


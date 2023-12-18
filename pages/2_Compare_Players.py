import streamlit as st
import streamlit_nested_layout
from utils import load_data, compare_players

st.set_page_config(layout="centered")

st.set_option('deprecation.showPyplotGlobalUse', False)

df, scaled_df, similarity_df = load_data()

player_name_1 = st.sidebar.selectbox('Select a player', scaled_df['Name'].unique(), index=scaled_df['Name'].unique().tolist().index('Alvaro Morata'))

player_name_2 = st.sidebar.selectbox('Select another player', scaled_df['Name'].unique(), index=scaled_df['Name'].unique().tolist().index('Romelu Lukaku'))

st.markdown("<h1 style='text-align: center; color: black'>Radar chart for players comparison</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: grey;'>All units in per 90</h2>", unsafe_allow_html=True)

position_list = df[df['Name'] == player_name_1]['Pos'].values[0] + df[df['Name'] == player_name_2]['Pos'].values[0]

position_list = list(dict.fromkeys(position_list))

position = st.selectbox('Select a position to compare', position_list, index=0)

fig = compare_players(df, player_name_1, player_name_2, pos=position)
st.pyplot(fig)

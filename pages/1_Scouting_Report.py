import streamlit as st
import streamlit_nested_layout
from utils import load_data, get_similar_players_cosine, plot_percentiles, compare_players

st.set_page_config(layout="wide")

st.set_option('deprecation.showPyplotGlobalUse', False)

df, scaled_df, similarity_df = load_data()

player_name = st.sidebar.selectbox('Select a player', scaled_df['Name'].unique(), index=scaled_df['Name'].unique().tolist().index('Harry Kane'))

top_n = st.sidebar.slider('Select number of similar players to display', min_value=1, max_value=10, value=10)

position = str(df[df['Name'] == player_name]['Pos'].values[0][0])

squad = str(df[df['Name'] == player_name]['Squad'].values[0])

st.header('')

st.markdown("<h1 style='text-align: center; color: black'>Scouting Report and Similar Players Finder</h1>", unsafe_allow_html=True)

st.header('')

st.markdown(f"<h2 style='text-align: center; color: black;'>{player_name}</h2>", unsafe_allow_html=True)

st.markdown(f"<h3 style='text-align: center; color: grey;'>{str(df[df['Name'] == player_name]['Pos'].values[0])} - {squad}</h2>", unsafe_allow_html=True)

st.header('')

outer_cols = st.columns([30,30], gap='large')

similar_players_cosine = get_similar_players_cosine(scaled_df, similarity_df, player_name, top_n)

def on_more_click(show_more, idx):
    show_more[idx] = True

def on_less_click(show_more, idx):
    show_more[idx] = False

if "show_more" not in st.session_state:
    st.session_state["show_more"] = dict.fromkeys(range(top_n), False)
show_more = st.session_state["show_more"]

similar_players_cosine = get_similar_players_cosine(scaled_df, similarity_df, player_name, top_n)

with outer_cols[0]:
    st.plotly_chart(plot_percentiles(df, player_name, width_size=1000))

with outer_cols[1]:
    st.markdown("**Similar Players (Cosine Similarity):**")

    colms = st.columns([1, 3, 3, 5, 3, 3])
    fields = ["", 'Name', 'Position', 'Squad', 'Similarity Score', '']
    for col, field_name in zip(colms, fields):
            # header
        col.write(field_name)

    for i, name in enumerate(similar_players_cosine['Name']):
        col1, col2, col3, col4, col5, col6 = st.columns([1, 3, 3, 5, 3, 3])

        col1.write(i + 1)
        col2.write(name)
        col3.write(str(similar_players_cosine[similar_players_cosine['Name'] == name]['Position'].values[0]))
        col4.write(str(similar_players_cosine[similar_players_cosine['Name'] == name]['Squad'].values[0]))
        col5.write(f"{similar_players_cosine[similar_players_cosine['Name'] == name]['Similarity'].values[0]:.3f}")

        placeholder = col6.empty()

        if show_more[i]:
            placeholder.button(
                "less", key=str(i) + "_", on_click=on_less_click, args=[show_more, i]
            )

            st.write("Radar chart for comparison")
            fig = compare_players(df, player_name, name)
            st.pyplot(fig)
        else:
            placeholder.button(
                "Compare",
                key=i,
                on_click=on_more_click,
                args=[show_more, i],
                type="primary",
            )
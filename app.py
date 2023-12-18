import streamlit as st
import streamlit_nested_layout
from utils import load_data, get_similar_players_cosine, plot_percentiles, compare_players

st.set_page_config(layout="wide")

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Player Similarity")

outer_cols = st.columns([30,30], gap='large')

df, scaled_df, similarity_df = load_data()

player_name = st.sidebar.selectbox('Select a player', scaled_df['Name'].unique(), index=scaled_df['Name'].unique().tolist().index('Harry Kane'))

top_n = st.sidebar.slider('Select number of similar players to display', min_value=1, max_value=10, value=10)

similar_players_cosine = get_similar_players_cosine(scaled_df, similarity_df, player_name, top_n)
# similar_players_knn = get_similar_players_knn(df, player_name, top_n)

def on_more_click(show_more, idx):
    show_more[idx] = True

def on_less_click(show_more, idx):
    show_more[idx] = False

if "show_more" not in st.session_state:
    st.session_state["show_more"] = dict.fromkeys(range(top_n), False)
show_more = st.session_state["show_more"]

similar_players_cosine = get_similar_players_cosine(scaled_df, similarity_df, player_name, top_n)

with outer_cols[0]:
    st.plotly_chart(plot_percentiles(df, player_name))

with outer_cols[1]:
    st.write("Similar Players (Cosine Similarity):")

    colms = st.columns(6)
    fields = ["", 'Name', 'Position', 'Squad', 'Similarity Score', '']
    for col, field_name in zip(colms, fields):
            # header
        col.write(field_name)

    for i, name in enumerate(similar_players_cosine['Name']):
        col1, col2, col3, col4, col5, col6 = st.columns(6)

        col1.write(i + 1)
        col2.write(name)
        col3.write(str(similar_players_cosine[similar_players_cosine['Name'] == name]['Position'].values[0]))
        col4.write(similar_players_cosine[similar_players_cosine['Name'] == name]['Squad'].values[0])
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
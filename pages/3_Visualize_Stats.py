import streamlit as st
import streamlit_nested_layout
from utils import load_data, plot_violin_and_scatter
from features_meaning import dict_metric

st.set_page_config(layout="wide")

st.set_option('deprecation.showPyplotGlobalUse', False)

df, scaled_df, similarity_df = load_data()

#only get the first Pos of the Pos column list
df['Pos'] = df['Pos'].apply(lambda x: x[0])

list_metric = dict_metric.keys()

search_key_1, search_key_2 = 'Gls', 'xG'
index_1, index_2 = None, None
 
# iterate through the dictionary to find the index of the search key
for i, key in enumerate(dict_metric.keys()):
    if key == search_key_1:
        index_1 = i
        break

for i, key in enumerate(dict_metric.keys()):
    if key == search_key_2:
        index_2 = i
        break

st.markdown("<h1 style='text-align: center; color: black'>Scatter plot for metrics comparison</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: grey;'>All units in per 90</h2>", unsafe_allow_html=True)

metric_1 = st.sidebar.selectbox('Select a metric', list_metric, index=index_1, format_func=lambda x: f'{x} - {dict_metric[x]}')

metric_2 = st.sidebar.selectbox('Select another metric', list_metric, index=index_2, format_func=lambda x: f'{x} - {dict_metric[x]}')

st.plotly_chart(plot_violin_and_scatter(df, metric_1, metric_2), use_container_width=True)
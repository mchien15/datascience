import streamlit as st

st.set_page_config(
    page_title="Football Data Analyst",
    page_icon=":soccer:",
    layout="wide",

)
img_path = 'imgs/the_pitch.jpeg'

st.write("# Welcome to the app! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ## This is a Football Data Analyst app built specifically for football scouts 📊 and people who love the beautiful game ⚽.  
    ### **👈 Select a demo from the sidebar** to see some examples of what this app can do!
    """
)

st.image(img_path, use_column_width=True)
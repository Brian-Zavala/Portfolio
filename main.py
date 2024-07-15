import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Brian Zavala")
    content = """Hello I am Brian!
     I am a software programmer and I'm currently pursuing my B.S in computer science at 
     Southern New Hampshire University. I am self-taught, driven, and extremely motivated to
     create projects and pursue my passion in back and front-end development. Please contact me 
    if you are interested in my work, thank you!
    """
    st.info(content)
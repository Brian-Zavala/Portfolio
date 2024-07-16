import streamlit as st

st.set_page_config(page_title="Brian's Portfolio", page_icon=":🐍:",
                   layout="wide", initial_sidebar_state="expanded",
                   menu_items=None)

page_bg_img = """
<style>
[data-testid="stApp"] {
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHdm7VHUGd-YFHg0OY1FzRcmi_j-cLi1t4sg&s");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local; }
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=375)

with col2:
    st.title("*Brian Zavala*")
    content = """
    ***Hello I am Brian! I am a software programmer and I'm currently pursuing my 
    B.S in computer science at Southern New Hampshire University. I am 
    self-taught, driven, and extremely motivated to create projects and pursue 
    my passion in back and front-end development. Please feel free to contact me 
    if you are interested in my work, thank you!***
    """
    st.write(content)

    col_image2 = (["https://cdn.dribbble.com/users/926537/screenshots/4502924/media/18181eb39eec9784db256e246954adba.gif","https://threadwaiting.com/wp-content/uploads/2018/01/TechnicalFeaturesofPython.gif"])
    st.image(col_image2, width=255)

    content2 = """⬇️***scroll***⬇️ ***Python Apps*** ⬇️***scroll***⬇️
     """

    st.write(content2)

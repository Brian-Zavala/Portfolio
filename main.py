import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="Brian's Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
page_style = """
<style>
    /* Main container styling */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        background-size: cover;
        background-attachment: fixed;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.9);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Header styling */
    h1 {
        background: linear-gradient(120deg, #60a5fa, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }

    /* Content containers */
    [data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem auto;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* Column container styling */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* Image container */
    [data-testid="stImage"] {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        display: block;
        margin: 0 auto;
    }

    [data-testid="stImage"] img {
        margin: 0 auto;
        display: block;
    }

    [data-testid="stImage"]:hover {
        transform: translateY(-5px);
    }

    /* Text styling */
    p {
        color: #e2e8f0 !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
        text-align: center !important;
        max-width: 800px;
        margin: 1rem auto !important;
    }

    /* Link styling */
    a {
        color: #60a5fa !important;
        text-decoration: none !important;
        transition: color 0.3s ease;
    }

    a:hover {
        color: #3b82f6 !important;
    }

    /* Skills section styling */
    .skill-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 0.5rem auto;
        width: 100%;
        text-align: center;
    }

    /* Project card styling */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem auto;
        width: 90%;
        text-align: center;
    }

    /* List styling */
    ul {
        list-style-position: inside;
        padding-left: 0;
        text-align: center;
    }

    li {
        margin: 0.5rem 0;
    }

    /* Container width control */
    .content-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #60a5fa;'>Navigation</h2>", unsafe_allow_html=True)
    selected_page = st.radio(
        "",
        ["Home", "Skills", "Projects", "Contact"],
        label_visibility="collapsed"
    )

# Main Content
if selected_page == "Home":
    # Header Section
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.image("images/photo.png", use_column_width=True)

    with col2:
        st.markdown("<h1>Brian Zavala</h1>", unsafe_allow_html=True)
        st.markdown("""
        <p style='font-size: 1.4rem; color: #94a3b8 !important;'>
            Software Developer & Computer Science Student
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p>
        Hello! I am Brian, a passionate software programmer currently pursuing my 
        B.S in Computer Science at Southern New Hampshire University. As a 
        self-taught developer, I bring a unique blend of academic knowledge and 
        practical experience to my work.
        
        My focus spans both back-end and front-end development, allowing me to 
        create comprehensive solutions that address real-world challenges.
        </p>
        """, unsafe_allow_html=True)

elif selected_page == "Skills":
    st.markdown("<h1>Technical Skills</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='skill-container'>
            <h3 style='color: #60a5fa;'>Frontend Development</h3>
            <ul style='color: #e2e8f0;'>
                <li>HTML5 & CSS3</li>
                <li>Responsive Design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='skill-container'>
            <h3 style='color: #60a5fa;'>Backend Development</h3>
            <ul style='color: #e2e8f0;'>
                <li>Python</li>
                <li>SQL</li>
                <li>Pandas</li>
                <li>Matplotlib</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='skill-container'>
            <h3 style='color: #60a5fa;'>Tools & Technologies</h3>
            <ul style='color: #e2e8f0;'>
                <li>Git & GitHub</li>
                <li>Streamlit/Django/Flask</li>
                <li>Python Modules/Libraries</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif selected_page == "Projects":
    st.markdown("<h1>Featured Projects</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='project-card'>
            <h3 style='color: #60a5fa;'>Project 1</h3>
            <p>Description of your first project. Highlight the key features,
            technologies used, and your role in development.</p>
            <a href='#'>View Project →</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='project-card'>
            <h3 style='color: #60a5fa;'>Project 2</h3>
            <p>Description of your second project. Share the challenges you overcame
            and the impact of your solution.</p>
            <a href='#'>View Project →</a>
        </div>
        """, unsafe_allow_html=True)

elif selected_page == "Contact":
    st.markdown("<h1>Get In Touch</h1>", unsafe_allow_html=True)

    # Create a container for the contact section
    contact_container = st.container()

    with contact_container:
        # Using columns to center the content
        col, = st.columns(1)

        with col:
            st.markdown("""
            <div style='background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 10px; text-align: center;'>
                <p style='color: #e2e8f0; font-size: 1.rem; margin-bottom: 2rem;'>
                    I'm always interested in new opportunities and collaborations. 
                    Feel free to reach out through any of the following channels:
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Adding contact buttons with Streamlit
            st.write("")  # Spacing
            st.markdown("#### 📧 Email")
            st.markdown("[brian.zavala25@proton.me](mailto:brian.zavala25@proton.me)")

            st.write("")  # Spacing
            st.markdown("#### 💼 LinkedIn")
            st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/brian-zavala-361239328?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BXZ6tE6FiTqCxdBm9obN0BA%3D%3D)")

            st.write("")  # Spacing
            st.markdown("#### 🐱 GitHub")
            st.markdown("[GitHub Profile](https://github.com/Brian-Zavala)")
import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="Brian's Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items ={
        'Get Help': None,
        'Report a bug': None,
        'About': None})

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Layout fixes for responsive containers
st.markdown("""
    <style>
    /* Reset container behaviors */
    .element-container, .stMarkdown, .css-1r6slb0 {
        width: 100% !important;
        max-width: 100% !important;
        padding: 0 !important;
    }
    
    /* Column flex container */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 calc(33.333% - 1rem) !important;
        min-width: 280px !important;
    }
    
    /* Responsive grid system */
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 1rem !important;
        justify-content: center !important;
    }

    /* Container reset on larger screens */
    @media (min-width: 768px) {
        .element-container {
            width: auto !important;
            max-width: none !important;
        }
        
        [data-testid="column"] {
            flex-basis: calc(33.333% - 1rem) !important;
        }
    }

    /* Card styling with flex properties */
    div[data-testid="stVerticalBlock"] > div {
        display: flex !important;
    }

   
    /* Ensure text containers maintain width */
    .text-container {
       * Fix for nested columns */
    [data-testid="stHorizontalBlock"] [data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
    } width: 100% !important;
        box-sizing: border-box !important;
        padding: 1rem !important;
    }

    /* Reset for specific Streamlit elements */
    .stButton, .stDownloadButton {
        width: auto !important;
        min-width: 200px !important;
    }

    /
    </style>
""", unsafe_allow_html=True)


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

    # First add the CSS and HTML for the particles
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] > div {
            background: #1a1a1a;
            position: relative;
            overflow: hidden;
        }

        section[data-testid="stSidebar"] > div::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            right: -50%;
            bottom: -50%;
            pointer-events: none;  /* Allow clicks to pass through */
            background: 
                radial-gradient(circle at 30% 30%, rgba(96, 165, 250, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 70% 60%, rgba(96, 165, 250, 0.1) 0%, transparent 50%),
                linear-gradient(
                    45deg,
                    transparent 0%,
                    rgba(96, 165, 250, 0.1) 25%,
                    transparent 50%,
                    rgba(96, 165, 250, 0.1) 75%,
                    transparent 100%
                ),
                repeating-linear-gradient(
                    60deg,
                    transparent 0%,
                    transparent 2%,
                    rgba(96, 165, 250, 0.1) 2.5%,
                    transparent 3%
                ),
                repeating-linear-gradient(
                    120deg,
                    transparent 0%,
                    transparent 1.5%,
                    rgba(96, 165, 250, 0.1) 2%,
                    transparent 2.5%
                );
            animation: electricFlow 8s linear infinite,
                      pulsate 4s ease-in-out infinite;
            z-index: 1;
        }

        section[data-testid="stSidebar"] > div::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;  /* Allow clicks to pass through */
            background: 
                radial-gradient(circle at 50% var(--y, 50%), 
                    rgba(96, 165, 250, 0.3) 0%,
                    transparent 40%);
            animation: electric-glow 3s ease-in-out infinite alternate;
            z-index: 2;
        }

        @keyframes electricFlow {
            0% {
                transform: translate(0, 0) rotate(0deg);
            }
            100% {
                transform: translate(-20%, -20%) rotate(1deg);
            }
        }

        @keyframes pulsate {
            0%, 100% {
                opacity: 0.5;
            }
            50% {
                opacity: 1;
            }
        }

        @keyframes electric-glow {
            0% {
                --y: 0%;
                filter: brightness(1);
            }
            100% {
                --y: 100%;
                filter: brightness(1.5);
            }
        }

        /* Ensure radio buttons are clickable */
        section[data-testid="stSidebar"] [data-testid="stRadio"] {
            position: relative;
            z-index: 3;  /* Increased z-index */
        }

        /* Style radio buttons and maintain functionality */
        section[data-testid="stSidebar"] [role="radiogroup"] label {
            position: relative;
            z-index: 3;  /* Increased z-index */
            text-shadow: 0 0 10px rgba(96, 165, 250, 0.5);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
            text-shadow: 0 0 15px rgba(96, 165, 250, 0.8);
            color: #60a5fa;
        }

        /* Ensure the title is visible */
        section[data-testid="stSidebar"] [data-testid="stMarkdown"] {
            position: relative;
            z-index: 3;  /* Increased z-index */
        }
        </style>
    """, unsafe_allow_html=True)


    st.markdown("<h2 style='text-align: center;"
                "color: #60a5fa;'>Navigation</h2>", unsafe_allow_html=True)

    # Add CSS to create padding
    st.markdown("""
        <style>
        div[data-testid="stRadio"] {
            padding-left: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

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
            <h3 style='color: #60a5fa;'>A.I Web Scraper & Analyzer</h3>
            <p>
            The Groq AI Web Scraper & Analyzer is a sophisticated web application that combines advanced AI processing with data visualization capabilities.
Key Technical Components:

AI Integration: Groq API for advanced language processing and analysis
Web Scraping:

Selenium for automated content extraction
BeautifulSoup4 for HTML parsing


Frontend: Streamlit for interactive dashboard
Visualization:

Plotly Express for dynamic data charts
WordCloud for text analysis representation


Async Processing: AsyncGroq client for efficient API communication

Technical Achievements:

Implemented parallel web scraping with anti-blocking measures
Built real-time AI content analysis system
Created interactive visualization dashboard
Developed asynchronous data processing pipeline
Designed dynamic content categorization

The application showcases expertise in:

AI API integration
Web scraping automation
Natural Language Processing
Data visualization
Asynchronous programming
Error handling and retry mechanisms

This platform effectively combines web scraping capabilities with AI-powered analysis, providing users with intelligent insights from web content while maintaining performance through efficient data processing and modern visualization techniques.
            </p>
            <a href='https://github.com/Brian-Zavala/A.I-Web-Scraper'>View Project →</a>
        </div>
        """, unsafe_allow_html=True)

        with col1:
            st.markdown("""
            <div class='project-card'>
                <h3 style='color: #60a5fa;'>LifeSync</h3>
                <p>
        The LifeSync Task Manager is a full-stack productivity application built with modern web technologies. At its core, it uses Streamlit for the frontend interface while leveraging MongoDB Atlas as its database backend. The application integrates interactive data visualization through Plotly Express and Pandas for data analysis and representation.
        
        Key Technical Components:
        
        Backend: MongoDB Atlas with PyMongo client for secure data persistence
        Frontend: Streamlit for responsive UI and interactive components
        Data Visualization: Plotly Express for dynamic charts and analytics
        Data Processing: Pandas for efficient data manipulation and analysis
        Technical Achievements:
        
        Implemented secure user authentication and data management
        Created an efficient task tracking and categorization system
        Developed real-time data visualization and analytics
        Built a scalable reward and progress tracking system
        Integrated error handling and data validation
        The application demonstrates proficiency in:
        
        Database design and management
        Full-stack web development
        Data visualization and analysis
        User experience design
        Secure application architecture
                </p>
                <a href='https://github.com/Brian-Zavala/LifeSync'>View Project →</a>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='project-card'>
            <h3 style='color: #60a5fa;'>Simple Bank</h3>
            <p>
            The Modern Banking Dashboard is a comprehensive financial analytics platform that leverages real-time data processing and secure transaction handling.
Key Technical Components:

Frontend: Streamlit for responsive financial dashboard
Backend: Plaid API for secure bank integration
Database: SQLite for local transaction storage
Visualization:

Plotly for interactive financial charts
Matplotlib for statistical analysis
Seaborn for trend visualization



Technical Achievements:

Implemented secure bank account integration
Built real-time transaction monitoring
Created predictive spending analysis
Developed automated expense categorization
Designed interactive budget tracking

The application demonstrates expertise in:

Financial API integration
Secure data handling
Statistical analysis
Data visualization
Pattern recognition
Predictive modeling

This platform combines secure financial data handling with advanced analytics to provide users with comprehensive insights into their spending patterns and financial health, while maintaining strict security standards and data privacy.
</p>
            <a href='https://github.com/Brian-Zavala/Simple-Bank'>View Project →</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='project-card'>
            <h3 style='color: #60a5fa;'>NASA API Explorer</h3>
            <p>
            The NASA Space Explorer is an interactive web application combining multiple NASA APIs with modern visualization techniques.
Key Technical Components:

Frontend: Streamlit for the main interface and interactive dashboard
NASA APIs: Integration with APOD, NEO, Earth imagery, and Mars rover data
Data Visualization: Plotly for interactive charts and space object tracking
Image Processing: PIL and OpenCV for image enhancement and analysis
Maps: Folium for interactive Earth observation mapping

Technical Achievements:

Built a multi-API synchronization system
Implemented real-time space object visualization
Created dynamic Earth observation mapping
Developed interactive Mars rover photo galleries
Integrated astronomy picture archival system

The application showcases expertise in:

API integration and management
Data visualization and mapping
Image processing and enhancement
Interactive dashboard design
Real-time data streaming

This application effectively combines astronomical data, satellite imagery, and space exploration information into an engaging educational platform, demonstrating proficiency in complex API handling and data visualization.
</p>
            <a href='https://github.com/Brian-Zavala/NASA'>View Project →</a>
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
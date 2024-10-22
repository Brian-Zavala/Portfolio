import streamlit as st


st.set_page_config(
    page_title="Brian's Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded")

from css import sidebar_css, main_page_css, fix_general_styles


hide_menu = """
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

main_page_css()

fix_general_styles()

# Sidebar Navigation
with st.sidebar:

    sidebar_css()

    st.markdown("<h2 style='text-align: center;"
                "color: #60a5fa;'>Navigation</h2>", unsafe_allow_html=True)

    # Add padding
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
    col1, col2 = st.columns([1, 1.5], gap="large")

    with col1:
        st.image("images/photo.png", use_column_width=True)

    with col2:
        st.markdown("""
    <div class="home-header">
        <h1>Brian Zavala</h1>
        <h3>Python Portfolio</h3>
        <p style='font-size: 1.4rem; color: #94a3b8 !important;'>
            Software Developer & Computer Science Student
        </p>
    </div>
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
                <li>Interactive UI Components</li>
                <li>Custom Web Components</li>
                <li>Bootstrap/Tailwind CSS</li>
                <li>Dynamic Styling</li>
                <li>Web Accessibility Standards</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='skill-container'>
            <h3 style='color: #60a5fa;'>Backend Development</h3>
            <ul style='color: #e2e8f0;'>
                <li>Python</li>
                <li>SQL (SQLite, PostgreSQL)</li>
                <li>MongoDB/NoSQL</li>
                <li>RESTful APIs</li>
                <li>API Integration & Development</li>
                <li>Pandas & NumPy</li>
                <li>Data Processing & Analysis</li>
                <li>Matplotlib & Plotly</li>
                <li>Seaborn & Visualization</li>
                <li>Async/Await Programming</li>
                <li>Database Design & Management</li>
                <li>Error Handling & Logging</li>
                <li>Security Implementation</li>
                <li>Performance Optimization</li>
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
                <li>Web Scraping (Selenium, BeautifulSoup4)</li>
                <li>AI Integration (Groq API)</li>
                <li>Version Control</li>
                <li>Cloud Platforms (MongoDB Atlas)</li>
                <li>Data Visualization Tools</li>
                <li>IDE & Development Tools</li>
                <li>Virtual Environments</li>
                <li>Package Management</li>
                <li>Testing & Debugging</li>
                <li>Documentation Tools</li>
                <li>Project Management Tools</li>
                <li>Deployment & Hosting</li>
                <li>Environment Configuration</li>
                <li>CI/CD Pipelines</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif selected_page == "Projects":
    st.markdown("<h1>Featured Projects</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

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
        
        Backend: MongoDB Atlas with PyMongo client for secure data persistence
        Key Technical Components:
        
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

    st.markdown("""
    <div class="contact-section">
        <div style='background: rgba(255, 255, 255, 0.05); border-radius: 10px;'>
            <p>
                I'm always interested in new opportunities and collaborations. 
                Feel free to reach out through any of the following channels:
            </p>
        </div>
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
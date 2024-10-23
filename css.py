import streamlit as st

def sidebar_css():
    st.markdown("""
        <style>
                /* Adjust sidebar width */
        [data-testid="stSidebar"][aria-expanded="true"] {
            min-width: 200px !important;
            max-width: 200px !important;
        }

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
            pointer-events: none;
            background: 
                /* Geometric squares */
                linear-gradient(rgba(96, 165, 250, 0.03) 0%, rgba(96, 165, 250, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(96, 165, 250, 0.03) 0%, rgba(96, 165, 250, 0.03) 1px, transparent 1px),
                /* Electric gradients */
                radial-gradient(circle at 30% 30%, rgba(96, 165, 250, 0.07) 0%, transparent 60%),
                radial-gradient(circle at 70% 60%, rgba(96, 165, 250, 0.07) 0%, transparent 60%),
                linear-gradient(
                    45deg,
                    transparent 0%,
                    rgba(96, 165, 250, 0.08) 25%,
                    transparent 50%,
                    rgba(96, 165, 250, 0.08) 75%,
                    transparent 100%
                );
            background-size: 20px 20px, 20px 20px, 100% 100%, 100% 100%, 200% 200%;
            animation: electricFlow 12s linear infinite;
            transform-origin: center center;
            will-change: transform;
            z-index: 1;
        }

        section[data-testid="stSidebar"] > div::after {
            content: '';
            position: absolute;
            inset: 0;
            pointer-events: none;
            background: 
                radial-gradient(
                    circle at 50% var(--y, 50%), 
                    rgba(96, 165, 250, 0.2) 0%,
                    transparent 70%
                ),
                /* Additional subtle squares */
                linear-gradient(45deg, rgba(96, 165, 250, 0.02) 1px, transparent 1px),
                linear-gradient(-45deg, rgba(96, 165, 250, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 30px 30px, 30px 30px;
            animation: electric-glow 6s ease-in-out infinite;
            will-change: opacity, filter;
            z-index: 2;
        }



        /* Enhanced Radio buttons and labels */
        section[data-testid="stSidebar"] [data-testid="stRadio"] {
            position: relative;
            z-index: 3;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            padding: 8px;
            backdrop-filter: blur(4px);
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label {
            position: relative;
            z-index: 3;
            text-shadow: 0 0 8px rgba(96, 165, 250, 0.3);
            transition: all 0.3s ease-out;
            padding: 8px 12px;
            border-radius: 6px;
            background: transparent;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
            text-shadow: 0 0 12px rgba(96, 165, 250, 0.6);
            color: #60a5fa;
            transform: translateX(4px);
            background: rgba(96, 165, 250, 0.1);
        }


        </style>
    """, unsafe_allow_html=True)

def main_page_css():
    st.markdown("""
<style>
/* Modern Gradient Background with Animation */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(45deg, #0f172a, #1e293b, #1e293b, #0f172a);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    min-height: 100vh;
    position: relative;
    margin: 0 !important;
    padding: 0 !important;

}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Particle Effect Overlay */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
        linear-gradient(rgba(96, 165, 250, 0.05) 0%, rgba(96, 165, 250, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(96, 165, 250, 0.05) 0%, rgba(96, 165, 250, 0.05) 1px, transparent 1px);
    background-size: 100px 100px, 100px 100px, 120px 120px, 150px 150px;
    animation: particleFloat 20s linear infinite;
    pointer-events: none;
}

@keyframes particleFloat {
    0% { background-position: 0 0; }
    100% { background-position: 100px 100px; }
}

/* Container for all home page content */
.home-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

/* Header section styling */
.home-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.home-header h1 {
    margin-bottom: 0.5rem;
}

.home-header h3 {
    margin-bottom: 1rem;
}

/* Introduction text container */
.intro-container {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 2rem;
    margin: 2rem 0;
}

/* Introduction text styling */
.intro-text {
    color: #e2e8f0;
    font-size: 1.1rem;
    line-height: 1.8;
    letter-spacing: 0.01em;
    white-space: normal;
    word-wrap: break-word;
    text-align: left;
    max-width: 65ch; /* Optimal line length for readability */
    margin: 0 auto;
}

.intro-text p {
    margin-bottom: 1.5rem;
    padding: 0;
}

.intro-text p:last-child {
    margin-bottom: 0;
}
/* Paragraph Spacing */
.intro-text p + p {
    margin-top: 1.5rem !important;
}


/* Modern Card Design */
.project-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0px;
    width: 100%;
    height: 100%;
    border-radius: 16px;
    background: linear-gradient(45deg, transparent, rgba(96, 165, 250, 0.1), transparent);
    transform: translateX(-1500%);
    transform: rotate(0deg);
    transition: transform 0.88s;
}

.project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    border-color: rgba(96, 165, 250, 0.2);
}

.project-card:hover::before {
    transform: translateY(-106.3%);
}

/* Enhanced Skill Container */
.skill-container {
    background: rgba(255, 255, 255, 0.02);
    border-radius: 20px;
    padding: 2rem;
    height: 100%;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.skill-container::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100px;
    height: 100px;
    background: radial-gradient(circle, rgba(96, 165, 250, 0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s;
}

.skill-container:hover::after {
    opacity: 1;
}

/* Modern Typography */
h1 {
    font-size: calc(32px + 1.5vw) !important;
    font-weight: 800 !important;
    background: linear-gradient(120deg, #60a5fa, #3b82f6, #60a5fa);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShine 3s linear infinite;
    text-align: center !important;
    }

h4 {
display: flex;
flex-grow: 1;
}

@keyframes textShine {
    to { background-position: 200% center; }
}

/* Enhanced List Items */
li {
    position: relative;
    padding: 0.6rem 0;
    padding-left: 1.5rem;
    transition: all 0.3s ease;
}

li::before {
    content: '▹';
    position: absolute;
    left: 0;
    color: #60a5fa;
    opacity: 0.8;
    transform: translateX(0);
    transition: all 0.3s ease;
}

li:hover {
    transform: translateX(8px);
    color: #60a5fa !important;
}

li:hover::before {
    opacity: 1;
    transform: translateX(-5px);
}

/* Modern Contact Section */
.contact-section {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 3rem;
    border: 1px solid rgba(255, 255, 255, 0.05);
    position: relative;
    overflow: hidden;
}

.contact-section::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(96, 165, 250, 0.1) 0%, transparent 50%);
    animation: rotateBG 15s linear infinite;
    pointer-events: none;
}

@keyframes rotateBG {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Enhanced Link Styling */
a {
    color: #60a5fa !important;
    text-decoration: none !important;
    position: relative;
    padding: 0.2rem 0;
    transition: all 0.3s ease;
}

a::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #60a5fa, transparent);
    transform: scaleX(0);
    transform-origin: center;
    transition: transform 0.4s ease;
}

a:hover::before {
    transform: scaleX(1);
}

/* Profile Image Enhancement */
[data-testid="stImage"] img {
    border-radius: 24px;
    transition: all 0.4s ease;
    border: 2px solid rgba(255, 255, 255, 0.1);
    filter: brightness(0.95) contrast(1.1);
}

[data-testid="stImage"] img:hover {
    transform: scale(1.02);
    border-color: rgba(96, 165, 250, 0.3);
    filter: brightness(1.05) contrast(1.1);
    box-shadow: 0 8px 32px rgba(96, 165, 250, 0.2);
}

/* Responsive Design Improvements */
@media (max-width: 768px) {
    .project-card, .skill-container {
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    h1 {
        font-size: calc(24px + 1.5vw) !important;
    }
        .home-content {
        padding: 1rem;
    }
    
    .intro-container {
        padding: 1.5rem;
    }
    
    .intro-text {
        font-size: 1rem;
        line-height: 1.6;
    }
    .contact-section {
        padding: 2rem;
    }
    
    li {
        padding: 0.4rem 0;
        padding-left: 1.2rem;
    }
}
</style>
""", unsafe_allow_html=True)


def fix_general_styles():
    st.markdown("""
    <style>
        /* Remove top margin and padding */
    .main > .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    /* Remove header padding/margin if present */
    header[data-testid="stHeader"] {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    /* Fix for any default Streamlit spacing */
    .stApp {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
        /* Remove padding from main container */
    [data-testid="stAppViewContainer"] > section:first-child {
        padding-top: 0 !important;
    }

    /* Target the first block in the main content area */
    [data-testid="stVerticalBlock"] > div:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    /* Fix for Python Portfolio subtitle */
    h3 {
        font-size: calc(18px + 0.8vw) !important;
        padding: 0 0.5rem !important;
        width: 100% !important;
        text-align: center !important;
        margin: 0 auto !important;
    }

    /* Prevent horizontal scrolling globally */
    [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        position: relative !important;
    }

    /* Fix vertical blocks alignment */
    [data-testid="stVerticalBlock"] {
        max-width: 100% !important;
        overflow: hidden !important;
        margin-left: 1rem auto !important;
        box-sizing: border-box !important;
    }

    /* Improve column layout */
    [data-testid="column"] {
        align-items: center !important;
        justify-content: flex-start !important;
        padding: 1rem !important;
        box-sizing: border-box !important;
    }

    /* Fix text container width */
    .text-container {
        width: 100% !important;
        max-width: 100% !important;
        padding: 0 1rem !important;
        box-sizing: border-box !important;
        
    }

    /* Contact page specific fixes */
    .contact-section {
        width: 100% !important;
        max-width: 800px !important;
        margin: 0 auto !important;
        padding: 1rem !important;
        box-sizing: border-box !important;
        overflow-x: hidden !important;
    }

    .contact-section > div {
        width: 100% !important;
        padding: 1rem !important;
        margin: 0 auto !important;
        box-sizing: border-box !important;
    }

    /* Home page specific fixes */
    .home-header {
        width: 100% !important;
        text-align: center !important;
        margin: 0 auto !important;
        padding: 0 !important;
    }

    .home-header h3 {
        color: #60A5FA !important;
        margin: 0.5rem auto !important;
    }


    
    /* Enable scrolling on mobile */
[   data-testid="stAppViewContainer"] {
    overflow-x: hidden !important;
    overflow-y: auto !important;
    width: 100vw !important;
    max-width: 100vw !important;
    position: relative !important;
    min-height: 100vh !important;
    height: auto !important;
}

/* Fix main content area scrolling */
.   main {
    overflow-y: auto !important;
    height: auto !important;
    min-height: 100vh !important;
    padding-bottom: 2rem !important;
}

/* Ensure vertical blocks don't restrict scrolling */
[   data-testid="stVerticalBlock"] {
    height: auto !important;
    min-height: auto !important;
    overflow: visible !important;
}

/* Mobile-specific fixes */
@media (max-width: 768px) (min-width: 769px) {
    [data-testid="stAppViewContainer"] {
        position: static !important;
    }
    /* Remove margin from first element in main content */
    .element-container:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    .stApp {
        margin: 0 !important;
        overflow: auto !important;
        height: auto !important;
    }
    
    [data-testid="stVerticalBlock"] {
        margin-bottom: 1rem !important;
    }
    
    /* Ensure project cards are fully scrollable */
    .project-card {
        height: auto !important;
        overflow: visible !important;
        margin-bottom: 1.5rem !important;
    }
    
    /* Fix content container on mobile */
    .content-container {
        height: auto !important;
        overflow: visible !important;
        padding-bottom: 2rem !important;
    }
}

/* Ensure sidebar doesn't affect main content scrolling */
[data-testid="stSidebar"] {
    height: 100vh !important;
    position: fixed !important;
    overflow-y: auto !important;
}

/* Fix for any fixed position elements */
.stApp > header {
    position: absolute !important;
}
   /* Basic scroll fixes */
    [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        overflow-y: auto !important;
    }

    .main .block-container {
        overflow-y: auto !important;
        height: auto !important;
        padding-bottom: 3rem;
    }

    /* Project page specific fixes */
    [data-testid="stVerticalBlock"] {
        height: auto !important;
        min-height: auto !important;
        overflow: visible !important;
    }

    .project-card {
        height: auto !important;
        overflow: visible !important;
        margin-bottom: 1.5rem !important;
    }

    /* Fix desktop scrolling */
    @media (min-width: 768px) {
        .stApp {
            overflow: auto !important;
            height: auto !important;
        }

        [data-testid="stHorizontalBlock"] {
            height: auto !important;
            overflow: visible !important;
        }

        [data-testid="column"] {
            height: auto !important;
            overflow: visible !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

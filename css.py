import streamlit as st

def sidebar_css():
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
            pointer-events: none;
            background: 
                radial-gradient(circle at 30% 30%, rgba(96, 165, 250, 0.05) 0%, transparent 60%),
                radial-gradient(circle at 70% 60%, rgba(96, 165, 250, 0.05) 0%, transparent 60%),
                linear-gradient(
                    45deg,
                    transparent 0%,
                    rgba(96, 165, 250, 0.05) 25%,
                    transparent 50%,
                    rgba(96, 165, 250, 0.05) 75%,
                    transparent 100%
                );
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
            background: radial-gradient(
                circle at 50% var(--y, 50%), 
                rgba(96, 165, 250, 0.15) 0%,
                transparent 70%
            );
            animation: electric-glow 6s ease-in-out infinite;
            will-change: opacity, filter;
            z-index: 2;
        }

        @keyframes electricFlow {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 0.5;
            }
            50% {
                opacity: 0.7;
            }
            100% {
                transform: translateY(-15%) rotate(1deg);
                opacity: 0.5;
            }
        }

        @keyframes electric-glow {
            0% {
                --y: 10%;
                opacity: 0.5;
                filter: brightness(1);
            }
            50% {
                opacity: 0.7;
                filter: brightness(1.2);
            }
            100% {
                --y: 90%;
                opacity: 0.5;
                filter: brightness(1);
            }
        }

        /* Radio buttons and labels */
        section[data-testid="stSidebar"] [data-testid="stRadio"] {
            position: relative;
            z-index: 3;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label {
            position: relative;
            z-index: 3;
            text-shadow: 0 0 8px rgba(96, 165, 250, 0.3);
            transition: all 0.2s ease-out;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
            text-shadow: 0 0 12px rgba(96, 165, 250, 0.6);
            color: #60a5fa;
            transform: translateX(2px);
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdown"] {
            position: relative;
            z-index: 3;
        }
        </style>
    """, unsafe_allow_html=True)

def main_page_css():
    st.markdown("""
<style>
/* Main container styling */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    background-size: cover;
    background-attachment: fixed;
}

/* Base container and layout */
[data-testid="stVerticalBlock"] {
    width: 100% !important;
    padding: 2rem !important;
    margin: 1rem auto !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Column styles */
[data-testid="column"] {
    width: 100% !important;
    padding: 0.5rem !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
}

/* Horizontal block behavior */
[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
}

/* Card and container styles */
.project-card, .skill-container {
    width: 100% !important;
    padding: 1.5rem !important;
    margin: 0.5rem 0 !important;
    box-sizing: border-box !important;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    text-align: center;
}

.project-card {
    width: 90%;
    border-radius: 10px;
    margin: 1rem auto;
}

/* Typography */
p {
    color: #e2e8f0 !important;
    font-size: calc(14px + 0.5vw) !important;
    line-height: 1.7 !important;
    padding: 0 0.5rem !important;
    text-align: center !important;
    max-width: 800px;
    margin: 1rem auto !important;
    word-wrap: break-word !important;
}

h1 {
    background: linear-gradient(120deg, #60a5fa, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: calc(24px + 1.5vw) !important;
    font-weight: 700 !important;
    padding: 0 0.5rem !important;
    margin-bottom: 1rem !important;
    text-align: center !important;
}

h3 {
    font-size: calc(18px + 0.8vw) !important;
    padding: 0 0.5rem !important;
}

/* List styling */
ul {
    list-style-position: inside;
    padding-left: 0;
    text-align: center;
}

li {
    margin: 0.5rem 0;
    font-size: calc(14px + 0.5vw) !important;
    line-height: 1.6 !important;
    padding: 0 0.5rem !important;
    word-wrap: break-word !important;
}

/* Image handling */
[data-testid="stImage"] {
    max-width: 100% !important;
    height: auto !important;
    margin: 1rem auto !important;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
    display: block;
}

[data-testid="stImage"] img {
    margin: 0 auto;
    display: block;
}

[data-testid="stImage"]:hover {
    transform: translateY(-5px);
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

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.9);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    width: auto !important;
    padding: 0.5rem !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"] {
    padding: 0.5rem !important;
}

/* Container width control */
.content-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}


/* Desktop styles */
@media (min-width: 768px) {
    /* Column behavior */
    [data-testid="column"] {
        width: auto !important;
        flex: 1 1 0 !important;
    }
    
    /* Horizontal block behavior */
    [data-testid="stHorizontalBlock"] {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }
    
    /* Card spacing */
    .project-card, .skill-container {
        margin: 1rem !important;
    }
    
    /* Typography padding */
    p, li {
        padding: 0 1rem !important;
    }
    
    /* Image sizing */
    [data-testid="stImage"] {
        max-width: 100% !important;
    }
}
</style>
""", unsafe_allow_html=True)


def fix_general_styles():
    st.markdown("""
    <style>
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
        margin: 0 auto !important;
        padding: 1rem !important;
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
        max-width: 800px !important;
        margin: 0 auto !important;
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

    /* Mobile-specific adjustments */
    @media (max-width: 768px) {
        [data-testid="stVerticalBlock"] {
            padding: 0.5rem !important;
        }

        .contact-section {
            padding: 0.5rem !important;
        }

        [data-testid="column"] {
            padding: 0.5rem !important;
        }
    }
    
    /* Enable scrolling on mobile */
[data-testid="stAppViewContainer"] {
    overflow-x: hidden !important;
    overflow-y: auto !important;
    width: 100vw !important;
    max-width: 100vw !important;
    position: relative !important;
    min-height: 100vh !important;
    height: auto !important;
}

/* Fix main content area scrolling */
.main {
    overflow-y: auto !important;
    height: auto !important;
    min-height: 100vh !important;
    padding-bottom: 2rem !important;
}

/* Ensure vertical blocks don't restrict scrolling */
[data-testid="stVerticalBlock"] {
    height: auto !important;
    min-height: auto !important;
    overflow: visible !important;
}

/* Mobile-specific fixes */
@media (max-width: 768px) {
    [data-testid="stAppViewContainer"] {
        position: static !important;
    }
    
    .stApp {
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

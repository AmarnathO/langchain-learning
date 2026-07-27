import streamlit as st

def inject_custom_css():
    """Injects high-quality premium CSS styling into the Streamlit app."""
    st.markdown(
        """
        <style>
        /* General background and fonts */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        /* Gradient header card */
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2.5rem;
            border-radius: 16px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        .header-title {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }
        
        .header-subtitle {
            font-size: 1.1rem;
            font-weight: 300;
            opacity: 0.9;
        }
        
        /* Custom card styling */
        .info-card {
            background-color: #f8fafc;
            border-left: 5px solid #764ba2;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        }
        
        /* Button overrides */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 0.6rem 2rem !important;
            border-radius: 50px !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(118, 75, 162, 0.3) !important;
            transition: all 0.3s ease !important;
            width: 100%;
        }
        
        div.stButton > button:first-child:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(118, 75, 162, 0.4) !important;
        }
        
        /* Style markdown tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            border-radius: 8px;
            overflow: hidden;
        }
        
        th {
            background-color: #764ba2;
            color: white;
            text-align: left;
            padding: 12px;
        }
        
        td {
            padding: 12px;
            border-bottom: 1px solid #e2e8f0;
        }
        
        tr:nth-child(even) {
            background-color: #f8fafc;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def render_header():
    """Renders the top beautiful hero header banner."""
    st.markdown(
        """
        <div class="header-container">
            <div class="header-title">🌍 AI Travel Planner</div>
            <div class="header-subtitle">Tailored city attractions, best cuisines, and restaurants powered by LangChain</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_sidebar():
    """Renders static guide tips and information in the sidebar."""
    with st.sidebar:
        st.markdown("### 💡 Quick Tips")
        st.markdown(
            """
            * **Language Selection**: You can type French, Spanish, German, Hindi, or any language you want the table to be generated in.
            * **Detailed Output**: The AI plans attractions, local food specialties, and details on prices.
            * **Fictional Cities**: Entering fictional cities will result in a clean validation notice.
            """
        )
        st.divider()
        st.markdown("Powered by **LangChain & OpenRouter**")

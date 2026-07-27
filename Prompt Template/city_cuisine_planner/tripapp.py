import streamlit as st

# Set page configurations
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

import sys
import os
# Add the project directory to sys.path so modules can be imported correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from backend.travel_service import TravelService
    from frontend.ui_components import inject_custom_css, render_header, render_sidebar
except ModuleNotFoundError:
    # Fallback for IDE editor warnings when opened as root
    from .backend.travel_service import TravelService
    from .frontend.ui_components import inject_custom_css, render_header, render_sidebar

# Inject styles
inject_custom_css()

# Render visual components
render_header()
render_sidebar()

# Instantiate Travel backend service
@st.cache_resource
def get_travel_service():
    return TravelService()

try:
    travel_service = get_travel_service()
except Exception as e:
    st.error(f"Failed to initialize Travel Service. Please check your .env configurations. Error: {e}")
    st.stop()

# Section 1: Input controls
st.subheader("📍 Where to go?")

col1, col2, col3 = st.columns(3)
with col1:
    city = st.text_input("Enter Destination City", placeholder="e.g. Paris, Tokyo, Mumbai")
with col2:
    country = st.text_input("Enter Country Name", placeholder="e.g. France, Japan, India")
with col3:
    language = st.text_input("Input your preferred language", value="English")

submit = st.button("Generate Plan ✨", use_container_width=True)

st.markdown("---")

# Section 2: Results
st.subheader("🗺️ Your Travel Itinerary & Gastronomy Guide")

if submit:
    if not city or not country or not language:
        st.warning("⚠️ Please fill in all the input fields before generating.")
    else:
        with st.spinner("🚀 Analyzing your trip... This may take a moment..."):
            try:
                result = travel_service.generate_plan(
                    city=city, 
                    country=country, 
                    language=language
                )
                
                # Beautiful output presentation
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>🗺️ Plan for {city.title()}, {country.title()}</h3>
                        <p>Here is your curated list of places to visit and local cuisines in <b>{language}</b>.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.markdown(result)
                st.success("🎉 Plan Generated Successfully!")
            except Exception as ex:
                st.error(f"An error occurred while generating the plan: {ex}")
else:
    st.info("👆 Enter details above and click **Generate Plan** to plan your itinerary.")


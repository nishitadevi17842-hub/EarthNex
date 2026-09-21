import streamlit as st

from src.prediction.risk_predictor import RiskPredictor
from src.camera.image_analysis import analyze_terrain_image
from src.fusion import fuse_risk
from src.alerts.alert_system import generate_alert
from src.mapping.risk_map import create_risk_map

from streamlit_folium import st_folium


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EarthNex",
    page_icon="🌍",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🌍 EarthNex")

st.subheader(
    "AI Landslide Risk Monitoring System"
)

st.write(
    "From Risk Detection to Safer Decisions"
)

st.divider()


# --------------------------------------------------
# INFORMATION
# --------------------------------------------------

st.info(
    "EarthNex combines environmental data and "
    "camera-based analysis to estimate observed "
    "landslide risk."
)


# --------------------------------------------------
# LOAD AI MODEL
# --------------------------------------------------

predictor = RiskPredictor()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🌧️ Environmental Data")

rainfall = st.sidebar.slider(
    "Rainfall (mm)",
    0,
    300,
    120
)

soil_moisture = st.sidebar.slider(
    "Soil Moisture",
    0.0,
    1.0,
    0.70
)

slope = st.sidebar.slider(
    "Slope Angle (°)",
    0,
    60,
    35
)

elevation = st.sidebar.slider(
    "Elevation (m)",
    0,
    3000,
    850
)

geology_score = st.sidebar.slider(
    "Geological Risk Score",
    0.0,
    1.0,
    0.60
)

historical_landslides = st.sidebar.slider(
    "Historical Landslide Count",
    0,
    15,
    4
)


# --------------------------------------------------
# LOCATION
# --------------------------------------------------

st.sidebar.divider()

st.sidebar.subheader("📍 Monitoring Location")

latitude = st.sidebar.number_input(
    "Latitude",
    value=19.9975
)

longitude = st.sidebar.number_input(
    "Longitude",
    value=73.7898
)


# --------------------------------------------------
# ENVIRONMENTAL AI PREDICTION
# --------------------------------------------------

environmental_data = {

    "rainfall_mm":
        rainfall,

    "soil_moisture":
        soil_moisture,

    "slope_degree":
        slope,

    "elevation_m":
        elevation,

    "geology_score":
        geology_score,

    "historical_landslide_count":
        historical_landslides
}


environment_result = predictor.predict(
    environmental_data
)


# --------------------------------------------------
# ENVIRONMENTAL RESULT
# --------------------------------------------------

st.header("🤖 AI Risk Analysis")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Environmental Risk",
        environment_result["risk_level"]
    )

with col2:

    st.metric(
        "Risk Score",
        f"{environment_result['risk_score']:.2f}"
    )

with col3:

    if environment_result["demo_mode"]:

        st.metric(
            "Model",
            "Demo"
        )

    else:

        st.metric(
            "Model",
            "Trained"
        )


# --------------------------------------------------
# CAMERA ANALYSIS
# --------------------------------------------------

st.divider()

st.header("📷 Camera-Based Terrain Analysis")

uploaded_image = st.file_uploader(

    "Upload a terrain image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


visual_result = None


if uploaded_image:

    image_path = "uploaded_terrain.jpg"

    with open(
        image_path,
        "wb"
    ) as file:

        file.write(
            uploaded_image.getbuffer()
        )

    st.image(
        uploaded_image,
        caption="Terrain Image",
        use_container_width=True
    )

    visual_result = analyze_terrain_image(
        image_path
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Visual Score",
            f"{visual_result['visual_score']:.2f}"
        )

    with col2:

        st.write(
            "**Visual Indication:**"
        )

        st.write(
            visual_result["indication"]
        )


# --------------------------------------------------
# MULTIMODAL RISK FUSION
# --------------------------------------------------

st.divider()

st.header("🧠 Combined AI Assessment")

combined_result = fuse_risk(

    environment_result,

    visual_result
)


combined_score = combined_result[
    "combined_score"
]

combined_level = combined_result[
    "risk_level"
]


col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Final Risk Level",
        combined_level
    )

with col2:

    st.metric(
        "Combined Risk Score",
        f"{combined_score:.2f}"
    )


st.progress(
    min(
        max(
            combined_score,
            0.0
        ),
        1.0
    )
)


# --------------------------------------------------
# ALERT SYSTEM
# --------------------------------------------------

st.divider()

st.header("🚨 Risk Alert")

alert = generate_alert(
    combined_level,
    "Current Monitoring Location"
)


if combined_level == "High":

    st.error(
        f"🔴 {alert['message']}"
    )

elif combined_level == "Medium":

    st.warning(
        f"🟡 {alert['message']}"
    )

else:

    st.success(
        f"🟢 {alert['message']}"
    )


# --------------------------------------------------
# RISK MAP
# --------------------------------------------------

st.divider()

st.header("🗺️ Dynamic Risk Map")

risk_map = create_risk_map(

    latitude,

    longitude,

    combined_level
)


st_folium(
    risk_map,
    width=1200,
    height=500
)


# --------------------------------------------------
# SYSTEM SUMMARY
# --------------------------------------------------

st.divider()

st.header("📊 EarthNex System Summary")

summary_col1, summary_col2 = st.columns(2)


with summary_col1:

    st.write(
        "### Environmental Inputs"
    )

    st.write(
        f"🌧️ Rainfall: {rainfall} mm"
    )

    st.write(
        f"💧 Soil Moisture: {soil_moisture:.2f}"
    )

    st.write(
        f"⛰️ Slope: {slope}°"
    )

    st.write(
        f"📍 Elevation: {elevation} m"
    )

    st.write(
        f"🪨 Geological Score: {geology_score:.2f}"
    )

    st.write(
        f"📚 Historical Landslides: "
        f"{historical_landslides}"
    )


with summary_col2:

    st.write(
        "### AI Output"
    )

    st.write(
        f"Risk Level: **{combined_level}**"
    )

    st.write(
        f"Risk Score: **{combined_score:.2f}**"
    )

    st.write(
        "📷 Camera Analysis: "
        + (
            "Available"
            if visual_result
            else "Not provided"
        )
    )

    st.write(
        "🗺️ Risk Map: Available"
    )

    st.write(
        "🚨 Alert System: Active"
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🌍 EarthNex | AI Landslide Risk Monitoring System"
)

st.caption(
    "Prototype system — predictions should not "
    "replace official geological assessments or "
    "emergency warnings."
)

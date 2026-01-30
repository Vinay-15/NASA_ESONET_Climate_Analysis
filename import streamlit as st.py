import streamlit as st
import pandas as pd
import numpy as np
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="NASA Disaster & Climate ML Project", layout="wide")

# -----------------------------
# Helper Functions (API)
# -----------------------------
@st.cache_data
def load_eonet_data():
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    params = {"limit": 200}
    response = requests.get(url, params=params)
    data = response.json()["events"]

    rows = []
    for e in data:
        if e["geometry"]:
            geo = e["geometry"][-1]
            rows.append({
                "id": e["id"],
                "title": e["title"],
                "category": e["categories"][0]["title"],
                "date": geo["date"],
                "longitude": geo["coordinates"][0],
                "latitude": geo["coordinates"][1]
            })
    return pd.DataFrame(rows)


@st.cache_data
def load_power_data(df):
    climate_rows = []

    for _, row in df.iterrows():
        date = row["date"][:10].replace("-", "")
        url = "https://power.larc.nasa.gov/api/temporal/daily/point"
        params = {
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "start": date,
            "end": date,
            "parameters": "T2M,RH2M,WS2M,PRECTOT",
            "format": "JSON"
        }

        r = requests.get(url, params=params)
        if r.status_code == 200:
            js = r.json()["properties"]["parameter"]
            climate_rows.append({
                **row.to_dict(),
                "temp": list(js.get("T2M", {}).values())[0],
                "humidity": list(js.get("RH2M", {}).values())[0],
                "wind": list(js.get("WS2M", {}).values())[0],
                "precip": list(js.get("PRECTOT", {}).values())[0]
            })

    return pd.DataFrame(climate_rows)

# -----------------------------
# Load Data
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Introduction", "Data Prep / EDA", "Visualizations", "Models (Coming Soon)", "Conclusions"]
)

@st.cache_data
def load_combined():
    eonet = load_eonet_data()
    combined = load_power_data(eonet.sample(50, random_state=42))
    combined["date"] = pd.to_datetime(combined["date"])
    combined.dropna(inplace=True)
    return combined

df = load_combined()

# -----------------------------
# INTRODUCTION TAB
# -----------------------------
if page == "Introduction":
    st.title("Natural Disasters and Climate Conditions")

    st.image("images/intro_image.png", use_column_width=True)

    st.write("""
    Natural disasters such as wildfires, storms, and floods pose serious risks to human life,
    infrastructure, ecosystems, and economies. Understanding the environmental conditions
    associated with these events is critical for preparedness, mitigation, and response planning.
    
    Climate variables like temperature, wind speed, humidity, and precipitation play an
    important role in both triggering and intensifying natural disasters. By examining
    disaster events together with local climate data, patterns may emerge that help explain
    why certain events occur when and where they do.
    
    This project combines real-time disaster event data from NASA with global climate
    observations to explore relationships between environmental conditions and disaster types.
    The goal is to use data-driven methods to uncover patterns, group similar events,
    and eventually build predictive models that support disaster risk assessment.
    """)

    st.subheader("Research Questions")
    questions = [
        "Do certain disaster types occur under specific climate conditions?",
        "How does wind speed vary across disaster categories?",
        "Are wildfires associated with lower humidity levels?",
        "Can climate variables cluster disaster events?",
        "Which variables are most influential in differentiating disaster types?",
        "Do storms show higher precipitation than other events?",
        "Are extreme temperatures linked to specific disasters?",
        "Can disasters be predicted using climate features?",
        "Which regions experience the most climate-sensitive disasters?",
        "How do climate trends change over time for disasters?"
    ]
    for q in questions:
        st.write("- ", q)

# -----------------------------
# DATA PREP / EDA TAB
# -----------------------------
elif page == "Data Prep / EDA":
    st.title("Data Preparation & Exploratory Analysis")

    st.subheader("Raw & Cleaned Data Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Overview")
    st.write(df.describe())

    st.subheader("Missing Values Check")
    st.write(df.isna().sum())

    st.subheader("Event Category Distribution")
    fig = px.bar(df, x="category", title="Disaster Categories")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# VISUALIZATIONS TAB
# -----------------------------
elif page == "Visualizations":
    st.title("Exploratory Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Temperature Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df["temp"], bins=20, ax=ax)
        ax.set_title("Temperature Distribution")
        st.pyplot(fig)

    with col2:
        st.subheader("Wind Speed vs Temperature")
        fig = px.scatter(
            df,
            x="temp",
            y="wind",
            color="category",
            title="Wind Speed vs Temperature by Disaster Type"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df[["temp", "humidity", "wind", "precip"]].corr(), annot=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Geographic Distribution of Events")
    fig = px.scatter_geo(
        df,
        lat="latitude",
        lon="longitude",
        color="category",
        title="Global Disaster Locations"
    )
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# MODELS TAB (PLACEHOLDER)
# -----------------------------
elif page == "Models (Coming Soon)":
    st.title("Machine Learning Models")

    st.write("""
    This section will include:
    - PCA for dimensionality reduction
    - Clustering to group disaster events
    - Association Rule Mining
    - Supervised models (Naive Bayes, Decision Trees, SVMs)
    
    Each model will have:
    - Overview
    - Data used
    - Code links
    - Results & interpretation
    """)

# -----------------------------
# CONCLUSIONS TAB
# -----------------------------
elif page == "Conclusions":
    st.title("Conclusions")

    st.write("""
    Climate conditions vary significantly across different natural disaster types.
    The exploratory analysis shows meaningful differences in temperature, wind speed,
    humidity, and precipitation among events such as wildfires and storms.
    
    These findings suggest that climate variables can provide valuable signals for
    understanding and categorizing natural disasters. As the project progresses,
    machine learning models will further quantify these relationships and assess
    predictive capabilities.
    
    Insights from this project can support disaster preparedness, environmental
    monitoring, and data-driven decision-making for climate resilience.
    """)


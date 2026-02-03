import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="ECONet",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#2E86C1; font-size:3em;">
        🌍 Disasters by the Numbers: Climate Patterns Behind Catastrophes
    </h1>
    <p style="text-align:center; font-size:1.2em;">
    </p>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Introduction",
    "Data Collection",
    "Exploratory Analysis",
    "Models",
    "Results & Discussion",
    "Conclusion"
])

# --------------------------------------------------
# INTRODUCTION
# --------------------------------------------------
with tab1:
    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("📌 Project Overview")

        st.info("""
                Natural disasters such as **wildfires, floods, storms, and volcanic eruptions** cause devastating environmental damage, economic disruption, and loss of human life across the world. Every year, communities face the consequences of these events, from destroyed ecosystems and infrastructure to long-term social and economic impacts.
                
                Climate conditions play a critical role in shaping the **occurrence, intensity, and spread** of natural disasters. Factors like **temperature, humidity, wind speed, and precipitation** directly influence how disasters form, evolve, and escalate. For example, low humidity and strong winds can intensify wildfires, while heavy rainfall and wind patterns can drive severe storms and flooding.
                
                This project aims to better understand these relationships by exploring how **local climate conditions** align with **real-world disaster events**. By integrating real-time disaster data from **NASA EONET** with climate observations from the **NASA POWER** API, the project connects where and when disasters occur with the environmental conditions surrounding them. This combined analysis helps uncover patterns that can support improved disaster awareness, risk assessment, and data-driven decision-making.


        """)

        st.subheader("🎯 Project Objectives")
        st.write("""
        - Analyze climate conditions surrounding natural disasters  
        - Identify patterns across disaster categories  
        - Explore whether climate variables can distinguish disaster types  
        - Build a foundation for predictive modeling  
        """)

        st.subheader("Research Questions")
        st.write("""
            - Do certain disaster types occur under specific climate conditions?,
            - How does wind speed vary across disaster categories?,
            - Are wildfires associated with lower humidity levels?,
            - Can climate variables cluster disaster events?,
            - Which variables are most influential in differentiating disaster types?,
            - Do storms show higher precipitation than other events?,
            - Are extreme temperatures linked to specific disasters?,
            - Can disasters be predicted using climate features?,
            - Which regions experience the most climate-sensitive disasters?,
            -How do climate trends change over time for disasters?
        """)
    

        st.subheader("GitHub Repository Link:")
        st.info("https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis")

    with col2:
        st.image(
            "https://www.reuters.com/resizer/v2/https%3A%2F%2Farchive-images.prod.global.a201836.reutersmedia.net%2F2021%2F12%2F07%2F2021-12-07T130031Z_42684_MRPRC2C4R9KTCWP_RTRMADP_0_GLOBAL-POY-2021.JPG?auth=08fffc6dfb9e8c1cad4ae17f3e8aee1f09fb18075510aec24fb4500a7cd3f51d&width=1920&quality=80",
            use_container_width=True
        )
        st.image(
            "https://www.reuters.com/resizer/v2/https%3A%2F%2Farchive-images.prod.global.a201836.reutersmedia.net%2F2021%2F12%2F07%2F2021-12-07T130031Z_42684_MRPRC2GTO9GD138_RTRMADP_0_USA-WEATHER-WILDFIRES.JPG?auth=90ba6bdbd2d19fafa06efea3f1d6076e8a7f7031df00e132f3edd5a4f2d52e10&width=1920&quality=80",
            use_container_width=True
        )
        st.image(
            "https://www.reuters.com/resizer/v2/https%3A%2F%2Farchive-images.prod.global.a201836.reutersmedia.net%2F2021%2F12%2F07%2F2021-12-07T130031Z_42684_MRPRC2PNO9S1QIM_RTRMADP_0_GLOBAL-POY-2021.JPG?auth=def6273d8c8cd9337566099c07f291496ca2b452883fedda19b78dabc0c5f2e7&width=1920&quality=80",
            use_container_width=True
        )

#https://www.reuters.com/news/picture/pictures-of-the-year-natural-disasters-idUSRTXJ1RBU/

# --------------------------------------------------
# DATA COLLECTION
# --------------------------------------------------
with tab2:
    st.header("🛰️ Data Collection & Preparation")

    def vizo_block(image, title, description):
        with st.container():
            col1, col2 = st.columns([2, 0.5])
            with col1:
                st.image(image, use_container_width=True)
            with col2:
                st.subheader(title)
                st.write(description)
        st.markdown("---")

    st.info("""
    ### 1. NASA EONET (Earth Observatory Natural Event Tracker)

    NASA EONET provides **near real-time information** on natural disaster events
    occurring worldwide.

    **Information collected:**
    - Event type (Wildfire, Storm, Flood, etc.)
    - Event date
    - Geographic coordinates (latitude & longitude)
    - Event category
    """)

    st.info("""
    ### 2. NASA POWER Climate Data

    Climate conditions near each disaster location were retrieved using the
    **NASA POWER API**, which provides daily meteorological observations.

    **Climate variables used:**
    - **Temperature (T2M)**
    - **Relative Humidity (RH2M)**
    - **Wind Speed (WS2M)**
    - **Precipitation (PRECTOT)**
    """)

    st.info("""
    ### 3. Data Preparation Steps

    - **Filtered valid disaster events with geographic coordinates:**  
    Only events that included both latitude and longitude were kept. This ensured that every disaster could be accurately linked to local climate conditions.

    - **Matched each event with same-day climate data:**  
    For each disaster event, climate variables were retrieved for the same date and location using the NASA POWER API. This helped capture the environmental conditions present at the time of the event.

    - **Removed missing or inconsistent values:**  
    Events with incomplete, missing, or unrealistic climate measurements were removed to maintain data reliability and avoid misleading patterns.

    - **Converted dates to standard datetime format:**  
    All event dates were converted into a consistent datetime format, allowing for proper time-based analysis and visualizations.

    - **Created a unified dataset for analysis:**  
    Disaster event data and climate data were merged into a single, structured dataset, making it easier to perform exploratory analysis and apply machine learning techniques.
    """)

    vizo_block(
        "images/EONET.png",
        "NASA EONET (Earth Observatory Natural Event Tracker) Data",
        "This dataset includes information on natural disasters such as wildfires, storms, and floods, along with their geographic coordinates and event dates."
    )

    vizo_block(
        "images/NASAPwer.png",
        "NASA POWER Climate Data",
        "This dataset provides daily meteorological observations including temperature, humidity, wind speed, and precipitation for locations worldwide."
    )


# --------------------------------------------------
# EDA & VISUALIZATIONS
# --------------------------------------------------
with tab3:
    st.header("📊 Exploratory Data Analysis")

    st.write("""
    Exploratory Data Analysis (EDA) was conducted to understand
    the distribution of climate variables and their relationship
    with different disaster categories.
    """)

    def viz_block(image, title, description):
        with st.container():
            col1, col2 = st.columns([1.3, 2])
            with col1:
                st.image(image, use_container_width=True)
            with col2:
                st.subheader(title)
                st.write(description)
        st.markdown("---")

    viz_block(
        "images/temp_dist.png",
        "Temperature Distribution Across Disaster Events",
        "This plot shows how temperature values are distributed for all recorded disaster events. Most disasters occur within a moderate to high temperature range, with a noticeable concentration around warmer values. This suggests that many recorded events especially wildfires tend to happen under elevated temperature conditions. A small number of low temperature events are also present, likely associated with ice related events"
    )

    viz_block(
        "images/wind_speed.png",
        "Relationship Between Wind Speed and Temperature",
        "This scatter plot explores how wind speed varies with temperature across different disaster categories. While there is no strong linear relationship, higher wind speeds tend to appear more frequently at moderate to high temperatures. This pattern is particularly important for disasters like wildfires and storms, where wind can significantly influence spread and severity."
    )

    viz_block(
        "images/voilin.png",
        "Temperature Variation by Disaster Category",
        "This violin plot compares temperature distributions across disaster types. Wildfires generally occur across a wide range of temperatures, often skewed toward higher values. Volcanic events show a narrower temperature range, while sea and lake ice events are concentrated at very low temperatures. This visualization highlights how different disasters are associated with distinct temperature conditions."
    )

    viz_block(
        "images/correlation.png",
        "Correlation Between Climate Variables",
        "The correlation heatmap shows relationships among temperature, humidity, wind speed, and precipitation. Temperature and humidity exhibit a moderate negative correlation, meaning higher temperatures often coincide with lower humidity. Precipitation shows weak correlations with other variables, suggesting it behaves more independently. These relationships help explain how certain combinations of climate factors contribute to different disaster types."
    )
    viz_block(
        "images/precip.png",
        "Precipitation Distribution Across Disaster Events",
        "This histogram displays the distribution of precipitation values across all disaster events. Most events occur under low precipitation conditions, with a long tail representing heavy rainfall events. This indicates that while extreme precipitation is less common, it plays a critical role in certain disasters such as floods and severe storms."
    )

    viz_block(
        "images/humi.png",
        "Humidity Levels by Disaster Type",
        "This box plot compares humidity levels across disaster categories. Wildfires tend to occur under lower humidity conditions, which aligns with known fire behavior. In contrast, volcanic and ice-related events show higher humidity levels. The variation within each category highlights how humidity influences disaster likelihood differently depending on event types."
    )

    viz_block(
        "images/dist_disaster.png",
        "Distribution of Disaster Categories",
        "This bar chart shows the frequency of different disaster types in the dataset. Wildfires dominate the dataset, while volcanic and ice-related events appear far less frequently. This imbalance reflects both the global prevalence of wildfires and the reporting focus of the data sources."
    )

    viz_block(
        "images/boxplot.png",
        "Precipitation by Disaster Type",
        "This box plot illustrates how precipitation levels differ across disaster categories. Wildfires are associated with minimal precipitation, while other disaster types show wider variability. This reinforces the idea that low precipitation is a key condition for fire related disasters, whereas storms and floods require heavier rainfall."
    )
    viz_block(
        "images/disaster_month.png",
        "Seasonal Distribution of Disasters",
        "This histogram shows how disaster events are distributed throughout the year. There is a clear increase in events during certain months, indicating seasonal patterns. Peaks during warmer months align with wildfire activity, while other events occur more evenly or during specific seasons."
    )

    viz_block(
        "images/wind.png",
        "Wind Speed Distribution",
        "This plot shows the distribution of wind speed values across all disaster events. Most events occur at low to moderate wind speeds, with fewer cases of extreme wind. However, even moderate winds can significantly impact disasters like wildfires and storms, making wind speed an important contributing factor."
    )

# --------------------------------------------------
# MODELS
# --------------------------------------------------
with tab4:
    st.header("🤖 Machine Learning Models (Upcomimg)")
    if False:
        st.info("""
        The prepared dataset allows for the application of several
        machine learning techniques to identify patterns and make predictions.
        """)

        st.subheader("Models Considered")
        st.write("""
        - **K-Means Clustering:** Group disasters based on climate similarity  
        - **Principal Component Analysis (PCA):** Reduce dimensionality  
        - **Decision Trees:** Identify important climate thresholds  
        - **Naive Bayes:** Probabilistic classification of disaster types  
        - **Support Vector Machines (SVM):** Disaster category classification  
        """)

        st.info("""
        These models help explore whether climate conditions
        can meaningfully distinguish between different disaster categories.
        """)

# --------------------------------------------------
# RESULTS
# --------------------------------------------------
with tab5:
    st.header("📈 Results & Discussion")
    if False:
        st.write("""
        The exploratory analysis revealed several key patterns
        linking climate variables to disaster occurrences.
        """)    
        st.info("""
        Key observations from the exploratory analysis include:
        """)

        st.write("""
        - Wildfires frequently occur under **high temperature and low humidity** conditions  
        - Storm events are associated with **higher wind speed and precipitation**  
        - Flood events show strong links to **extreme rainfall patterns**  
        - Climate variables exhibit distinct distributions across disaster categories  
        """)

        st.info("""
        These findings align with known physical processes and
        validate the usefulness of climate data in disaster analysis.
        """)

# --------------------------------------------------
# CONCLUSION
# --------------------------------------------------
with tab6:
    st.header("✅ Conclusion & Future Work")
    if False:
        st.write("""
        This project demonstrates how integrating **real-time disaster data**
        with **climate observations** can provide valuable insights into
        the environmental conditions associated with natural disasters.
        """)

        st.subheader("Key Takeaways")
        st.write("""
        - Climate variables strongly influence disaster behavior  
        - Data integration enables deeper environmental understanding  
        - Exploratory analysis supports future predictive modeling  
        """)

        st.subheader("Future Enhancements")
        st.write("""
        - Incorporate historical climate trends  
        - Apply advanced ensemble learning models  
        - Perform regional risk assessment  
        - Develop early-warning predictive systems  
        """)

    st.success("🌱 Data-driven climate analysis can support disaster preparedness and mitigation.")

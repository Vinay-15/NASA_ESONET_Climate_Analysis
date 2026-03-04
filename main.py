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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Introduction",
    "Data Collection",
    "Exploratory Analysis",
    "PCA Analysis",
    "Clustering Analysis",
    "ARM Analysis",
    "Models",
    "Results & Discussion",
    "Conclusion"])

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

    def viza_block(image, title, description):
        with st.container():
            col1, col2 = st.columns([1.5, 1.0])
            with col1:
                st.image(image, use_container_width=True)
            with col2:
                st.subheader(title)
                st.write(description)
        st.markdown("---")

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
with tab7:
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
with tab8:
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
with tab9:
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




























with tab4:

    st.header("📉 Principal Component Analysis (PCA)")

    # ----------------------------
    # PCA Description
    # ----------------------------
    st.subheader("🔍 What is PCA?")


    st.info("""
    Principal Component Analysis (PCA) is a dimensionality reduction technique
    that transforms a dataset with many correlated variables into a smaller
    set of new uncorrelated variables called principal components.

    Each principal component represents a linear combination of the original
    variables and captures as much variance (information) as possible.
    The first component explains the most variance, the second explains the next
    most, and so on.

    PCA helps simplify complex datasets, reduce noise, visualize high-dimensional
    data, and identify the most influential variables while retaining most of
    the original information.
    """)



    # ----------------------------
    # Dataset Used
    # ----------------------------
    st.subheader("📂 Dataset Used for PCA")

    st.info("""
    PCA was applied to the cleaned climate-disaster dataset that combines
    NASA EONET disaster records with NASA POWER climate observations.

    Only numerical variables were used, as PCA requires quantitative data.
    All categorical labels and text fields were removed before analysis.
    
    **Variables Used:**
    - Temperature  
    - Humidity  
    - Wind Speed  
    - Precipitation  
    - Latitude  
    - Longitude  
    - Month  
    """)

    st.info("The dataset was standardized using StandardScaler before applying PCA.")

    # ----------------------------
    # Normalization
    # ----------------------------
    st.subheader("⚙️ Data Normalization")

    st.info("""
    Before applying PCA, the data was normalized using StandardScaler so that
    each variable has a mean of 0 and a standard deviation of 1.

    This step is essential because PCA is sensitive to scale.
    Without normalization, variables with larger values would dominate
    the principal components.
    """)

    # ----------------------------
    # PCA 2D
    # ----------------------------
    st.subheader("📊 PCA with 2 Components (2D)")


    viz_block(
    "images/pca_2d.png",
    "PCA with 2 Components (2D)",
    """
    PCA was first performed using two principal components.

    The explained variance ratios were:

    - PC1: 59.18%  
    - PC2: 25.96%  

    Together, these two components retain approximately **85.15%** of the
    original dataset information.

    This indicates that most of the important patterns in the data can be
    represented in just two dimensions.
    """)


    # ----------------------------
    # PCA 3D
    # ----------------------------
    st.subheader("📈 PCA with 3 Components (3D)")


    viz_block(
        "images/pca_3d.png",
        "PCA with 3 Components (3D)",
        """
    PCA was next performed using three principal components.

    The explained variance ratios were:

    - PC1: 59.18%  
    - PC2: 25.96%  
    - PC3: 8.88%  

    Together, these components retain approximately **94.03%** of the
    original information.

    Adding the third component significantly improves information retention
    while still maintaining a low-dimensional structure.
    """)

    # ----------------------------
    # Variance Retention
    # ----------------------------
    st.subheader("📐 Variance Retention Analysis")


    viz_block(
    "images/pca_variance.png",
    "ariance Retention Analysis",
    """
    The cumulative variance plot shows how much information is retained
    as more principal components are added.

    From the plot, at least **4 components** are required to retain
    **95% or more** of the total variance.

    This means the original dataset can be reduced from 7 variables
    to 4 principal components while preserving nearly all information.
    """)

    # ----------------------------
    # Eigenvalues
    # ----------------------------
    st.subheader("🔢 Eigenvalues")

    st.info("""
    Eigenvalues represent the amount of variance captured by each
    principal component.

    The top three eigenvalues obtained from PCA were:

    - PC1: 4.17  
    - PC2: 1.83  
    - PC3: 0.63  

    These values confirm that the first principal component dominates
    the dataset, capturing most of the variability.
    """)

    # ----------------------------
    # Interpretation
    # ----------------------------
    st.subheader("🧠 Interpretation of PCA Results")

    st.info("""
    The PCA results show that climate variables related to temperature,
    humidity, wind speed, precipitation, and geographic location
    are strongly correlated.

    A small number of components can summarize most of the dataset,
    indicating that disaster-related climate conditions share
    common underlying patterns.

    The dominance of the first component suggests that overall
    climate intensity (temperature, humidity, and moisture levels)
    plays a major role in distinguishing disaster events.

    These reduced dimensions were later used for clustering and
    modeling to improve computational efficiency and visualization.
    """)
















# --------------------------------------------------
# CLUSTERING ANALYSIS
# --------------------------------------------------
with tab5:

    st.header("🧩 Clustering Analysis")

    # ----------------------------
    # Overview
    # ----------------------------
    st.subheader("🔍 Overview of Clustering Methods")

    st.info("""
    Clustering is an unsupervised machine learning technique used to
    group similar data points together based on their characteristics.

    In this project, three major clustering approaches were applied:

    - K-Means (Partition-Based Clustering)
    - Hierarchical Clustering
    - DBSCAN (Density-Based Clustering)

    These methods help identify natural groupings of disaster events
    based on climate and geographic features.
    
    ### Clustering Methods Used:

    - **K-Means:** Divides data into K clusters by minimizing within-cluster variance.
    - **Hierarchical:** Builds clusters step-by-step using distance relationships.
    - **DBSCAN:** Groups dense regions and detects noise points.
    """)

    # ----------------------------
    # Data Preparation
    # ----------------------------
    st.subheader("⚙️ Data Preparation")

    st.info("""
    Before applying clustering algorithms, the dataset was prepared
    using the following steps:

    - Removed categorical labels and text fields
    - Retained only numerical variables
    - Applied StandardScaler for normalization
    - Reduced dimensionality using PCA (3 components)

    PCA-reduced data was used for clustering to improve visualization
    and computational efficiency.
    
    ### Features Used After Processing:
    - PC1
    - PC2
    - PC3
    """)

    st.info("All clustering was performed on standardized and PCA-reduced data.")

    # ----------------------------
    # Silhouette Method
    # ----------------------------
    st.subheader("📐 Silhouette Method for Optimal K")
    viz_block(
        "images/silhouette.png",
        "Silhouette Method for Optimal K",
        """
    The Silhouette Method was used to evaluate different values of K
    for K-Means clustering.

    The silhouette score measures how well each data point fits within
    its assigned cluster compared to other clusters.

    Higher scores indicate better-defined clusters.
    """
    )


    st.write("""
    The Silhouette Method was used to evaluate different values of K
    for K-Means clustering.

    The silhouette score measures how well each data point fits within
    its assigned cluster compared to other clusters.

    Higher scores indicate better-defined clusters.
    """)

    st.write("""
    The highest silhouette score occurs at **K = 2**, but K = 3, 4, and 5
    were selected for further analysis to explore more detailed
    cluster structures.
    """)

    # ----------------------------
    # KMeans Results
    # ----------------------------
    st.subheader("📊 K-Means Clustering Results")

    st.image(
        "images/kmeans_345.png",
        use_container_width=True
    )

    st.write("""
    K-Means clustering was applied using K = 3, 4, and 5 clusters.

    These values were selected based on silhouette scores and visual
    interpretability.""")
    st.info("""
    ### As K increases:
    - Clusters become more detailed
    - Groups become smaller
    - Interpretability may decrease
    """)

    st.info("""
    ### Observations:

    - K = 3: Produces broad, well-separated clusters
    - K = 4: Reveals subgroups within major clusters
    - K = 5: Produces finer segmentation with some overlap
    """)

    # ----------------------------
    # Hierarchical Clustering
    # ----------------------------
    st.subheader("🌳 Hierarchical Clustering")

    vizo_block(
        "images/dendrogram.png",
        "",
        """
        Hierarchical clustering was performed using Ward's linkage method.

        This method builds a tree-like structure called a dendrogram,
        showing how clusters merge at different distances.

        Each horizontal line represents a cluster merge.
        Higher merges indicate more dissimilar groups.
        """)

    st.write("""
    By cutting the dendrogram at different heights, multiple
    cluster structures can be obtained.

    The dendrogram suggests approximately 3–5 major clusters,
    which aligns with the K-Means results.
    """)

    # ----------------------------
    # DBSCAN
    # ----------------------------
    st.subheader("🌐 DBSCAN Clustering")



    viz_block(
        "images/dbscan.png",
        "DBSCAN Clustering",
        """
    DBSCAN is a density-based clustering algorithm that groups points
    in dense regions and identifies outliers as noise.

    Unlike K-Means, DBSCAN does not require specifying the number of clusters.
    

    In this analysis:

    - Dense regions formed meaningful clusters
    - Sparse points were classified as noise
    - Some extreme disaster events were identified as outliers
    """)

    # ----------------------------
    # Comparison
    # ----------------------------
    st.subheader("📊 Comparison of Clustering Methods")

    st.write("""
    Each clustering method provides a different perspective
    on the dataset.
    """)

    st.markdown("""
    | Method       | Strengths                          | Limitations                     |
    |--------------|-----------------------------------|---------------------------------|
    | K-Means      | Simple, efficient, interpretable  | Requires K selection            |
    | Hierarchical | Visual structure, flexible        | Computationally expensive       |
    | DBSCAN       | Finds noise, no K required         | Sensitive to parameters         |
    """)

    # ----------------------------
    # Interpretation
    # ----------------------------
    st.subheader("🧠 Interpretation of Results")

    st.info("""
    The clustering results indicate that disaster events can be grouped
    based on similarities in climate and geographic conditions.

    Major clusters appear to reflect:

    - Hot, dry, low-precipitation environments (wildfire-prone)
    - High-moisture, high-wind environments (storm/flood-prone)
    - Cold or extreme regions (ice-related events)

    The dominance of temperature and humidity in PCA is reflected
    in the cluster structures.
    """)

    # ----------------------------
    # Conclusions
    # ----------------------------
    st.subheader("✅ Clustering Conclusions")

    st.info("""
    Clustering analysis demonstrates that climate variables
    can meaningfully separate disaster events into distinct groups.

    K-Means provided the most interpretable clusters,
    Hierarchical clustering confirmed cluster structure,
    and DBSCAN highlighted extreme and unusual events.

    These results support the use of unsupervised learning
    for disaster pattern discovery and risk analysis.
    """)
















# --------------------------------------------------
# ASSOCIATION RULE MINING (ARM)
# --------------------------------------------------
with tab6:

    st.header("🔗 Association Rule Mining (ARM) Analysis")

    # ----------------------------
    # Overview
    # ----------------------------
    st.subheader("🔍 Overview of Association Rule Mining")

    st.info("""
    Association Rule Mining is used to discover hidden relationships
    between variables in large datasets.

    In this project, ARM was applied to identify frequent
    combinations of climate conditions that occur together
    during disaster events.
    
    ### ARM Techniques Used:

    - Apriori Algorithm
    - Frequent Itemset Mining
    - Rule Generation
    """)

    # ----------------------------
    # Data Preparation
    # ----------------------------
    st.subheader("⚙️ Data Preparation for ARM")

    st.info("""
    Before applying ARM, continuous climate variables were converted
    into categorical levels.

    Each variable was divided into three categories:
    - Low
    - Medium
    - High

    The categorical data was then converted into
    one-hot encoded format.
    
    ### Variables Used:
    - Temperature Category
    - Humidity Category
    - Wind Speed Category
    - Precipitation Category
    """)

    st.info("ARM was applied on one-hot encoded climate categories.")

    # ----------------------------
    # Support vs Confidence
    # ----------------------------
    st.subheader("📊 Support vs Confidence Analysis")

    viza_block(
        "images/support_vs_confidence.png",
        "Support vs Confidence Analysis",
        """
    This scatter plot shows the relationship between
    support and confidence for generated rules.

    - Support measures how frequently a rule appears
    - Confidence measures how reliable the rule is

    Rules with high confidence and moderate support
    are considered most useful.
    """)

    st.write("""
    Most rules show moderate support and high confidence,
    indicating stable climate relationships.
    """)

    # ----------------------------
    # Association Network
    # ----------------------------
    st.subheader("🌐 Association Rule Network")


    viza_block(
        "images/arm_network.png",
        "Association Rule Network",
        """
    The association network visualizes relationships
    between climate categories.

    - Nodes represent climate conditions
    - Edges represent strong association rules

    This helps identify dominant interaction patterns
    between variables.
    """)


    st.write("""
    Humidity and precipitation appear as central nodes,
    indicating their strong influence in disaster conditions.
    """)

    # ----------------------------
    # Rule Evaluation Metrics
    # ----------------------------
    st.subheader("📐 Rule Evaluation Metrics")

    st.info("""
    Each generated rule was evaluated using multiple metrics:

    - Support
    - Confidence
    - Lift
    - Leverage
    - Conviction
    
    ### Interpretation of Metrics:

    - Support: Frequency of rule occurrence
    - Confidence: Strength of implication
    - Lift > 1: Positive dependency
    - Leverage: Difference from random chance
    - Conviction: Directional dependency
    """)

    # ----------------------------
    # Key Findings
    # ----------------------------
    st.subheader("🧠 Key Findings from ARM")

    st.info("""
    The ARM analysis revealed strong dependencies
    among climate variables.
    
    ### Major Observations:

    - High humidity is frequently linked with low temperature
    - Low wind speed often occurs with low precipitation
    - Medium precipitation is associated with moderate temperature
    - Certain multi-variable patterns show very high confidence
    """)

    # ----------------------------
    # Comparison with Other Methods
    # ----------------------------
    st.subheader("📊 Comparison with PCA and Clustering")

    st.info("""
    ARM complements PCA and clustering by providing
    interpretable rule-based relationships.
    """)

    st.markdown("""
    | Method     | Purpose                         | Output Type        |
    |------------|---------------------------------|--------------------|
    | PCA        | Dimensionality Reduction        | Components         |
    | Clustering | Group Similar Events            | Clusters           |
    | ARM        | Discover Hidden Associations    | Rules              |
    """)

    # ----------------------------
    # Conclusions
    # ----------------------------
    st.subheader("✅ ARM Conclusions")

    st.info("""
    Association Rule Mining successfully identified
    meaningful relationships among climate variables.

    The results show that disasters are influenced
    by recurring combinations of weather conditions.

    ARM improves interpretability by translating
    numerical patterns into understandable rules.
    """)

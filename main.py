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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs([
    "Introduction",
    "Data Collection",
    "Exploratory Analysis",
    "PCA Analysis",
    "Clustering Analysis",
    "ARM Analysis",
    "Naive Bayes",
    "Decision Tree",
    "Regression",
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
        Natural disasters such as **wildfires, floods, storms, and volcanic eruptions** have far-reaching consequences that extend beyond immediate destruction. These events not only damage ecosystems and infrastructure but also disrupt economies, displace communities, and result in significant loss of human life. As the frequency and severity of such disasters continue to rise globally, understanding their underlying causes and patterns has become increasingly important for both preparedness and mitigation efforts.

        A key factor influencing natural disasters is the surrounding **climate environment**. Variables such as **temperature, humidity, wind speed, and precipitation** play a crucial role in determining how disasters originate, evolve, and intensify. For instance, prolonged periods of high temperatures combined with low humidity can create ideal conditions for wildfires, while excessive rainfall and strong wind systems can contribute to severe storms and flooding. These environmental conditions often act as catalysts that amplify the scale and impact of disasters.

        Despite the known relationship between climate and disasters, there is often a gap in effectively connecting **real-time disaster events** with the **specific climate conditions** that surround them. This project seeks to bridge that gap by integrating data from **NASA EONET**, which tracks natural disaster events globally, with climate data from the **NASA POWER API**, which provides detailed atmospheric and environmental measurements. By combining these two powerful data sources, the project enables a more comprehensive view of how environmental factors correlate with disaster occurrences.

        Through this integrated analysis, the project aims to uncover meaningful patterns and insights that can enhance **disaster awareness, risk assessment, and decision-making**. By understanding how local climate conditions align with real-world events, stakeholders such as researchers, policymakers, and emergency response teams can make more informed decisions. Ultimately, this work contributes to building more resilient communities and improving strategies for anticipating and responding to natural disasters in a changing climate.
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

    vizo_block(
        "images/cleandata.png",
        "Cleaned Dataset Sample",
        "This image shows the cleaned data used for PCA analysis"
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


# --------------------------------------------------
# RESULTS
# --------------------------------------------------
with tab11:
    st.header("📈 Results & Discussion")
 
    # ----------------------------
    # Project Summary
    # ----------------------------
    st.subheader("🔍 Project Summary")
 
    st.info("""
    This project set out to explore whether climate and geographic variables could meaningfully 
    predict and classify natural disaster events, specifically wildfire severity. The analysis 
    followed a complete data science lifecycle: collecting data from NASA EONET and NASA POWER 
    APIs, cleaning and merging the datasets, performing exploratory data analysis, applying 
    unsupervised learning techniques (PCA, clustering, and association rule mining), and finally 
    building and comparing seven supervised classification models across three algorithm families. 
    The target variable — wildfire severity — was engineered from a composite risk score combining 
    temperature, humidity, and wind speed, then binned into three balanced classes (Low, Moderate, 
    and High Severity with 50 samples each). The prediction features were latitude, longitude, 
    month, and precipitation, chosen specifically because they are independent of the label 
    construction and represent genuinely useful information for severity prediction. All models 
    were trained on the same 70/30 stratified split (105 training, 45 testing) to ensure a fair 
    and consistent comparison across every method.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Key Results Overview
    # ----------------------------
    st.subheader("📊 Key Results Across All Analyses")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info("""
        **Unsupervised Learning Results**
 
        **PCA** revealed that the first two principal components capture approximately 85% of 
        the total variance in the climate-disaster dataset, and three components capture over 
        94%. This indicates that the seven original variables share substantial redundancy and 
        can be effectively summarized in a lower-dimensional space. Temperature and humidity 
        emerged as the dominant contributors to the first principal component, confirming their 
        central role in characterizing disaster environments. **K-Means clustering** with K=3 
        produced the most interpretable groupings, separating events into hot-dry (wildfire-prone), 
        high-moisture (storm/flood-prone), and cold/extreme clusters. The silhouette analysis 
        confirmed K=2 as the optimal partition, but K=3 through K=5 revealed meaningful sub-structures. 
        **Hierarchical clustering** validated the K-Means results through its dendrogram, which 
        showed natural merge points consistent with 3-5 clusters. **DBSCAN** successfully identified 
        outlier events that did not fit any major cluster pattern, highlighting extreme or unusual 
        disaster conditions. **Association Rule Mining** uncovered strong co-occurrence patterns, 
        such as the frequent pairing of high humidity with low temperature and the association 
        between low wind speed and low precipitation, providing interpretable rules that complement 
        the numerical outputs of PCA and clustering.
        """)
 
    with col2:
        st.info("""
        **Supervised Learning Results**
 
        Seven classification models were evaluated for predicting wildfire severity from geographic 
        and precipitation features. **Logistic Regression** achieved the highest accuracy at 
        **97.8%**, correctly classifying 44 out of 45 test samples with near-perfect precision and 
        recall across all three severity classes. **Gaussian Naive Bayes** performed second best at 
        **88.9%**, leveraging its assumption of normally distributed features to effectively model 
        the continuous climate data. **Bernoulli NB** (77.8%) and **Multinomial NB** (75.6%) 
        achieved moderate accuracies, with their lower performance attributable to information loss 
        during binarization and scaling respectively. **Decision Trees** produced the lowest 
        accuracies, ranging from **64.4% to 71.1%** across three configurations with different 
        criteria, depths, and constraints. All three trees selected latitude as the root node, 
        confirming geographic location as the single most discriminative feature for severity 
        prediction. The feature importance analysis from the best Decision Tree showed that latitude 
        and longitude together account for over 83% of predictive power, with month contributing 
        roughly 10% and precipitation only about 2%. In the binary classification comparison 
        between Logistic Regression and Multinomial NB on adjacent severity classes (Low vs 
        Moderate), MNB slightly outperformed LR (73.3% vs 70.0%), suggesting probabilistic 
        models handle overlapping class distributions marginally better.
        """)
 
    st.markdown("---")
 
    # ----------------------------
    # Discussion: What Worked
    # ----------------------------
    st.subheader("✅ What Worked Well")
 
    st.info("""
    Several aspects of this project produced strong and meaningful results that validate the 
    overall approach. The **composite risk score** for label engineering proved to be an effective 
    solution to the class imbalance problem — with 149 wildfires and only 1 volcanic event, 
    direct category classification was impossible, but creating severity levels from temperature, 
    humidity, and wind speed produced three balanced classes that allowed all models to learn 
    meaningful patterns. The **feature independence design** — using latitude, longitude, month, 
    and precipitation as predictors while excluding the variables used to create the label — 
    successfully prevented data leakage and ensured that model accuracies reflect genuine 
    predictive relationships rather than circular logic. The **stratified train/test split** 
    maintained equal class proportions in both sets, giving every model the same fair chance 
    at learning and being evaluated. **Logistic Regression's exceptional 97.8% accuracy** 
    demonstrates that the relationship between geographic/seasonal features and wildfire severity 
    is approximately linear, making it amenable to simple yet powerful linear models. The 
    **consistency of latitude as the root node** across all three Decision Trees provides strong 
    evidence that geographic position is the most important single factor in wildfire severity, 
    a finding that is both statistically robust and physically interpretable. The **progression 
    from unsupervised to supervised learning** allowed each stage to inform the next: PCA 
    identified the most important variables, clustering revealed natural groupings, ARM 
    discovered co-occurrence patterns, and classification models quantified predictive power.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Discussion: Limitations
    # ----------------------------
    st.subheader("⚠️ Limitations and Considerations")
 
    st.info("""
    While the results are promising, several limitations should be acknowledged when interpreting 
    the findings. The **dataset size of 150 samples** is relatively small for machine learning, 
    which means model performance estimates may have higher variance than those from larger 
    datasets, and some models (particularly Decision Trees) may not have enough data to learn 
    robust splitting rules. The **class imbalance in the original data** (149 wildfires, 1 volcano) 
    required engineering a new target variable, which means the severity classification is a 
    proxy rather than a ground-truth measurement of actual wildfire damage or impact. The 
    **composite risk score weights** (0.4 for temperature, 0.35 for humidity, 0.25 for wind) 
    were chosen based on domain knowledge but are not empirically optimized — different weights 
    could produce different severity distributions and potentially different model rankings. 
    **Logistic Regression's 97.8% accuracy** is notably higher than other models, which could 
    indicate that the linear relationship between features and severity is partially an artifact 
    of how the severity label was constructed from quantile binning of continuous variables. The 
    **four prediction features** (latitude, longitude, month, precipitation) represent a limited 
    subset of factors that influence wildfire severity in reality — additional features like 
    vegetation type, soil moisture, elevation, and human activity could improve predictions. 
    The **NASA EONET data** reflects reported events rather than all events, potentially 
    introducing reporting bias toward larger, more visible, or more geographically accessible 
    disasters. Finally, the **temporal scope** of the data is limited to recent events, and 
    patterns may shift as climate change alters the relationships between geographic location, 
    seasonal timing, and disaster severity over time.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Discussion: Research Questions
    # ----------------------------
    st.subheader("🔬 Answering the Research Questions")
 
    st.info("""
    **Q: Can climate variables distinguish disaster types?**  
    Yes. PCA showed that temperature and humidity are the dominant factors differentiating 
    disaster events, and clustering successfully separated events into climate-based groups. 
    However, the dataset's wildfire dominance (99%) limited direct multi-category comparison.
 
    **Q: Are wildfires associated with lower humidity levels?**  
    Yes. Exploratory analysis confirmed that wildfires occur under significantly lower humidity 
    conditions compared to other disaster types, consistent with established fire science.
 
    **Q: Can disasters be predicted using climate features?**  
    Yes. Logistic Regression achieved 97.8% accuracy predicting wildfire severity from just 
    four features (latitude, longitude, month, precipitation), demonstrating strong predictive 
    power for severity classification.
 
    **Q: Which variables are most influential?**  
    Geographic location (latitude and longitude) dominates prediction, accounting for over 83% 
    of feature importance in Decision Trees. Month contributes approximately 10%, while 
    precipitation adds only about 2%.
 
    **Q: Which regions experience the most climate-sensitive disasters?**  
    The strong latitude dependence in all models suggests that tropical and subtropical regions 
    (lower latitudes) experience different severity patterns than temperate and boreal regions 
    (higher latitudes), with geographic position being the primary determinant of fire risk level.
 
    **Q: How do climate trends change over time for disasters?**  
    Monthly analysis showed clear seasonal patterns, with wildfire activity peaking during warmer 
    months. The month feature contributed to model accuracy, confirming that temporal patterns 
    play a meaningful (though secondary) role in severity prediction.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Final Comparison Visual
    # ----------------------------
    st.subheader("📊 Final Model Performance Summary")
 
    st.image("images/all_models_comparison.png",
             caption="Complete Accuracy Comparison Across All Seven Models",
             use_container_width=True)
 
    st.markdown("""
    | Rank | Model                          | Family              | Accuracy | Key Strength                          |
    |------|--------------------------------|---------------------|----------|---------------------------------------|
    | 1    | Logistic Regression            | Logistic Regression | 97.8%    | Near-perfect multi-class accuracy     |
    | 2    | Gaussian NB                    | Naive Bayes         | 88.9%    | Best probabilistic model              |
    | 3    | Bernoulli NB                   | Naive Bayes         | 77.8%    | Works with binary features            |
    | 4    | Multinomial NB                 | Naive Bayes         | 75.6%    | Best on binary classification task    |
    | 5    | Decision Tree 1 (Gini, d=4)    | Decision Tree       | 71.1%    | Most interpretable visual model       |
    | 6    | Decision Tree 2 (Entropy, d=5) | Decision Tree       | 66.7%    | Demonstrates overfitting effect       |
    | 7    | Decision Tree 3 (Gini, d=3)    | Decision Tree       | 64.4%    | Most robust / least overfit           |
    """)
 
 
# --------------------------------------------------
# CONCLUSION
# --------------------------------------------------
with tab12:
 
    st.header("✅ Conclusion & Future Work")
 
    # ----------------------------
    # Project Conclusion
    # ----------------------------
    st.subheader("📝 Project Conclusion")
 
    st.info("""
    This project successfully demonstrated that **climate and geographic variables can meaningfully 
    predict wildfire severity** through a comprehensive data science pipeline integrating real-time 
    disaster data from NASA EONET with climate observations from NASA POWER. Beginning with data 
    collection and cleaning, through exploratory analysis, unsupervised learning (PCA, clustering, 
    and association rule mining), and finally supervised classification, every stage of the analysis 
    contributed unique insights into the relationship between environmental conditions and disaster 
    behavior. The unsupervised methods revealed that climate variables are highly correlated and 
    can be reduced to a small number of meaningful dimensions, that disaster events naturally 
    cluster into groups based on climate similarity, and that specific combinations of climate 
    conditions frequently co-occur. The supervised models showed that wildfire severity can be 
    predicted with up to **97.8% accuracy** using only four features — latitude, longitude, month, 
    and precipitation — with Logistic Regression emerging as the best-performing model across all 
    seven algorithms tested. The consistent finding across all models that **geographic location 
    (latitude and longitude) is the dominant predictor** of wildfire severity provides a robust, 
    physically interpretable result that aligns with established fire science: a fire's location 
    determines its surrounding vegetation, climate zone, seasonal patterns, and moisture availability, 
    all of which directly influence fire behavior and intensity.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Key Takeaways
    # ----------------------------
    st.subheader("🎯 Key Takeaways")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info("""
        **Data & Methodology Takeaways**
 
        1. **Integrating multiple NASA data sources** (EONET + POWER) creates a richer dataset 
           than either source alone, enabling climate-disaster correlation analysis that would 
           not be possible with event data or climate data in isolation.
 
        2. **Feature engineering is critical** — the composite risk score approach transformed 
           an imbalanced single-class dataset into a balanced three-class problem suitable for 
           supervised learning, while carefully separating label-construction variables from 
           prediction features to prevent data leakage.
 
        3. **The data science lifecycle is iterative** — insights from PCA (which variables 
           matter most) informed clustering (how events group), which informed classification 
           (can we predict severity), creating a coherent analytical narrative.
 
        4. **Data preprocessing choices significantly impact results** — the same features 
           produced accuracies ranging from 64.4% to 97.8% depending on the model and scaling 
           method, highlighting that algorithm selection and data preparation are equally important.
        """)
 
    with col2:
        st.info("""
        **Scientific & Practical Takeaways**
 
        1. **Geographic location is the strongest predictor** of wildfire severity, accounting 
           for over 83% of feature importance. This suggests that region-specific fire management 
           strategies are more effective than universal approaches.
 
        2. **Climate variables are highly interconnected** — PCA showed that temperature, humidity, 
           and wind speed share substantial variance, and ARM revealed frequent co-occurrence 
           patterns like high humidity with low temperature.
 
        3. **Simple models can outperform complex ones** — Logistic Regression (a linear model) 
           dramatically outperformed Decision Trees (nonlinear models), demonstrating that model 
           complexity should match data complexity.
 
        4. **Wildfire severity is predictable** — achieving 97.8% accuracy with just four 
           features suggests that practical early-warning systems based on location and basic 
           climate data are feasible and could support emergency response planning.
        """)
 
    st.markdown("---")
 
    # ----------------------------
    # Future Work
    # ----------------------------
    st.subheader("🚀 Future Enhancements")
 
    st.info("""
    While this project established a strong foundation for climate-based disaster analysis, 
    several enhancements could extend and strengthen the work in meaningful ways. First, 
    **expanding the dataset** by collecting data over longer time periods and including more 
    disaster categories (floods, storms, earthquakes) would increase sample size and enable 
    true multi-category classification rather than severity-based proxy labels. Second, 
    **incorporating additional features** such as vegetation index (NDVI), elevation, soil 
    moisture, population density, and proximity to water bodies could capture factors that 
    latitude and longitude only approximate, potentially improving prediction accuracy even 
    further. Third, **applying ensemble methods** like Random Forests, Gradient Boosting 
    (XGBoost), and Support Vector Machines would test whether non-linear models can close 
    the gap with Logistic Regression or surpass it on larger datasets. Fourth, **temporal 
    modeling** using time-series approaches could capture how climate conditions evolve in the 
    days and weeks leading up to a disaster, rather than just using same-day measurements. 
    Fifth, **developing a real-time prediction dashboard** that ingests live NASA EONET and 
    POWER data and outputs severity predictions could provide actionable intelligence for 
    emergency response teams. Sixth, **regional risk mapping** using the trained models could 
    generate geographic visualizations of fire risk at different times of year, supporting 
    proactive resource allocation. Finally, **cross-validation and bootstrapping** would 
    provide more robust accuracy estimates and confidence intervals for model performance, 
    addressing the limitation of the relatively small 150-sample dataset.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Final Statement
    # ----------------------------
    st.success("""
    🌱 **This project demonstrates that data-driven climate analysis — combining real-time 
    disaster tracking with environmental observations and machine learning — can provide 
    powerful tools for understanding, predicting, and ultimately mitigating the impact of 
    natural disasters. By bridging the gap between climate science and disaster response, 
    this work contributes to building more resilient communities in a changing world.**
    """)
 
    st.markdown("---")
 
    st.subheader("📎 Resources & Links")
 
    st.markdown("""
    - **GitHub Repository:** [NASA EONET Climate Analysis](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis)
    - **NASA EONET API:** [https://eonet.gsfc.nasa.gov/api/v3/events](https://eonet.gsfc.nasa.gov/api/v3/events)
    - **NASA POWER API:** [https://power.larc.nasa.gov/api/temporal/daily/point](https://power.larc.nasa.gov/api/temporal/daily/point)
    - **Scikit-Learn Documentation:** [https://scikit-learn.org](https://scikit-learn.org)
    """)
 



























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
    The dataset used for PCA was collected from NASA EONET and NASA POWER APIs
    and cleaned as described in the Data Collection tab.

    Below are links and previews of the datasets used for PCA.
    """)


    # Link to datasets (change paths if needed)
    st.markdown("**EONET URL** https://eonet.gsfc.nasa.gov/api/v3/events")
    st.markdown("**Power URL:** https://power.larc.nasa.gov/api/temporal/daily/point")

    # Screenshots / previews
    vizo_block(
        "images/NASAPwer.png",
        "Raw Dataset Sample",
        ""
    )

    vizo_block(
        "images/cleandata.png",
        "Cleaned Dataset Sample",
        "This image shows the cleaned data used for PCA analysis"
    )


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


    # ----------------------------
    # StandardScaler and PCA Code
    # ----------------------------
    st.subheader("⚙️ Data Scaling and PCA Implementation")

    st.info("""
    The cleaned dataset was standardized using Scikit-Learn's StandardScaler.
    Principal Component Analysis was then applied using the PCA module.

    Below is the Python code used for scaling and PCA.
    """)

    st.code("""
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    import pandas as pd

    # Select numerical features
    features = df[["temp","humidity","wind","precip","latitude","longitude","month"]]

    # Standardize
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)

    # PCA (2D)
    pca_2 = PCA(n_components=2)
    pca_2d = pca_2.fit_transform(scaled_data)

    # PCA (3D)
    pca_3 = PCA(n_components=3)
    pca_3d = pca_3.fit_transform(scaled_data)

    # Eigenvalues
    eigenvalues = pca_2.explained_variance_
    print(eigenvalues)
    """)

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


    st.info("""
    The following outputs show the explained variance ratios and
    eigenvalues generated from PCA.
    """)

    # Output screenshots
    st.image("images/95variance.png",
            caption="Explained Variance Ratios")

    st.image("images/top3eigen.png",
            caption="Top Eigenvalues from PCA")

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
    # Clustering Code
    # ----------------------------
    st.subheader("💻 Clustering Implementation Code")

    st.info("""
    Below is the Python code used for K-Means, Hierarchical,
    and DBSCAN clustering.
    """)

    # GitHub / Notebook Link (update this!)
    st.markdown("📌 [View Full Clustering Code on GitHub](notebooks/clustering.ipynb)")

    st.code("""
    from sklearn.cluster import KMeans, DBSCAN
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.metrics import silhouette_score
    from scipy.cluster.hierarchy import dendrogram, linkage
    import pandas as pd

    # Standardize
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    # Silhouette Analysis
    scores = []
    for k in range(2,7):
        km = KMeans(n_clusters=k)
        labels = km.fit_predict(pca_data)
        scores.append(silhouette_score(pca_data, labels))

    # KMeans
    kmeans = KMeans(n_clusters=3)
    k_labels = kmeans.fit_predict(pca_data)
    centroids = kmeans.cluster_centers_

    # Hierarchical
    Z = linkage(pca_data, method='ward')

    # DBSCAN
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    db_labels = dbscan.fit_predict(pca_data)
    """)

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


    st.info("""
    The Apriori algorithm identifies frequent itemsets
    by exploiting the property that all subsets of a
    frequent itemset must also be frequent.

    Rules are generated from frequent itemsets using
    support, confidence, and lift.
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
    # ARM Code
    # ----------------------------
    st.subheader("💻 ARM Implementation Code")

    st.info("Apriori was implemented using mlxtend.")

    # GitHub Link
    st.markdown("📌 [View ARM Code on GitHub](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis/blob/main/NASA_climate_analysis-2.ipynb)")

    st.code("""
    from mlxtend.frequent_patterns import apriori, association_rules
    import pandas as pd

    # Apriori
    freq = apriori(df, min_support=0.05, use_colnames=True)

    # Generate Rules
    rules = association_rules(freq,
                            metric="confidence",
                            min_threshold=0.6)

    # Sort rules
    top_support = rules.sort_values('support', ascending=False).head(15)
    top_conf = rules.sort_values('confidence', ascending=False).head(15)
    top_lift = rules.sort_values('lift', ascending=False).head(15)
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










# Naive Bayes

with tab7:
 
    st.header("📊 Naive Bayes Classification")
 
    # ----------------------------
    # (a) Overview
    # ----------------------------
    st.subheader("🔍 Overview: What is Naive Bayes?")
 
    st.info("""
    **Naive Bayes (NB)** is a family of probabilistic classifiers based on 
    **Bayes' Theorem** with the "naive" assumption that all features are 
    **conditionally independent** given the class label. Despite this simplifying 
    assumption, NB classifiers perform remarkably well in many real-world 
    applications, especially when the dataset is relatively small or the 
    dimensionality is high.
 
    Naive Bayes is commonly used for **text classification** (spam filtering, 
    sentiment analysis), **medical diagnosis**, **weather prediction**, and 
    any scenario where fast, probabilistic classification is needed. It works 
    well as a baseline model and is computationally efficient for both 
    training and prediction.
    """)
 
    st.markdown("---")
 
    st.subheader("📌 Naive Bayes Flavors: Compare & Contrast")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info("""
        **🔵 Multinomial Naive Bayes (MNB)**
        
        Designed for **discrete count data** — features represent frequencies 
        or counts (e.g., word counts in text). Works with non-negative values.
        
        - **Best for:** Text classification, document categorization
        - **Assumption:** Features follow a multinomial distribution
        - **Data type:** Non-negative integers or scaled values [0, 1]
        - **In this project:** Climate features were scaled to [0, 1] using 
          MinMaxScaler before applying MNB
        """)
 
        st.info("""
        **🟢 Gaussian Naive Bayes (GNB)**
        
        Assumes features follow a **normal (Gaussian) distribution**. Each 
        class models features with their own mean and variance.
        
        - **Best for:** Continuous numerical data
        - **Assumption:** Features are normally distributed within each class
        - **Data type:** Continuous values (standardized recommended)
        - **In this project:** Features were standardized using StandardScaler 
          (mean=0, std=1) before applying GNB
        """)
 
    with col2:
        st.info("""
        **🟠 Bernoulli Naive Bayes (BNB)**
        
        Designed for **binary/boolean features** — each feature is either 
        present (1) or absent (0).
        
        - **Best for:** Binary feature data, document classification with 
          word presence/absence
        - **Assumption:** Features follow a Bernoulli (binary) distribution
        - **Data type:** Binary values (0 or 1)
        - **In this project:** Each feature was binarized at its median value — 
          values above median = 1, below = 0
        """)
 
        st.info("""
        **🟡 Categorical Naive Bayes (CNB)**
        
        Designed for **categorical features** where each feature takes on 
        a discrete set of categories (not ordered).
        
        - **Best for:** Survey data, categorical attributes
        - **Assumption:** Features are categorically distributed
        - **Data type:** Discrete category labels
        - **Note:** Not used in this project since our features are 
          continuous climate measurements, not categorical
        """)
 
    st.markdown("---")
 
    st.markdown("""
    | NB Variant     | Feature Type         | Distribution Assumed | Scaling Needed        |
    |----------------|----------------------|----------------------|-----------------------|
    | Multinomial    | Counts / Frequencies | Multinomial          | MinMaxScaler [0, 1]   |
    | Gaussian       | Continuous           | Normal (Gaussian)    | StandardScaler        |
    | Bernoulli      | Binary (0/1)         | Bernoulli            | Binarize at threshold |
    | Categorical    | Discrete categories  | Categorical          | None                  |
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (b) Data Preparation
    # ----------------------------
    st.subheader("⚙️ Data Preparation")
 
    st.info("""
    **Creating the Target Label — Wildfire Severity**
 
    Since the dataset is dominated by wildfire events (149 out of 150), a direct 
    category classification was not meaningful. Instead, a **composite fire risk 
    score** was created from multiple climate variables:
 
    ```
    risk_score = temp × 0.4 + (100 − humidity) × 0.35 + wind × 0.25
    ```
 
    This score was then binned into **three balanced severity classes** using quantile 
    binning: **Low Severity**, **Moderate Severity**, and **High Severity** (50 samples each).
 
    **Features used for prediction** (independent of the label):
    - Latitude, Longitude, Month, Precipitation
 
    Temperature, humidity, and wind speed were excluded from features since they 
    were used to construct the severity label.
    """)
 
    st.info("""
    **Train/Test Split**
 
    The data was split into **70% training** (105 samples) and **30% testing** (45 samples) 
    using stratified sampling to ensure equal class representation in both sets.
 
    Training and testing sets are **disjoint** — no data point appears in both sets. 
    This is essential to get an honest evaluation of model performance. If training 
    data leaked into the test set, accuracy would be artificially inflated.
    """)
 

    viza_block(
    "images/nb_train_test_sample.png",
    "Training and Testing Set Samples (Disjoint)",
    """
    """)
 
    st.info("""
    **Different preprocessing for each NB flavor:**
    - **Multinomial NB:** MinMaxScaler → all values in [0, 1]
    - **Gaussian NB:** StandardScaler → mean=0, std=1
    - **Bernoulli NB:** Each feature binarized at its median → 0 or 1
    """)

 
    st.markdown("📌 [View Data Preparation Code on GitHub](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis/blob/main/NASA_climate_analysis-2.ipynb)")
 
    st.markdown("---")
 
    # ----------------------------
    # (c) Code
    # ----------------------------
    st.subheader("💻 Model Implementation Code")
 
    st.info("All three Naive Bayes models were implemented using **Scikit-Learn**.")
 
    st.code("""
    from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
    
    features = ["latitude", "longitude", "month", "precip"]
    X = combined_df[features]
    y = combined_df["severity_encoded"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y)
    
    # --- Multinomial NB ---
    scaler_mm = MinMaxScaler()
    X_train_mn = scaler_mm.fit_transform(X_train)
    X_test_mn  = scaler_mm.transform(X_test)
    mnb = MultinomialNB()
    mnb.fit(X_train_mn, y_train)
    
    # --- Gaussian NB ---
    scaler_ss = StandardScaler()
    X_train_g = scaler_ss.fit_transform(X_train)
    X_test_g  = scaler_ss.transform(X_test)
    gnb = GaussianNB()
    gnb.fit(X_train_g, y_train)
    
    # --- Bernoulli NB ---
    X_train_bn = X_train.copy()
    for col in features:
        median_val = X_train[col].median()
        X_train_bn[col] = (X_train[col] >= median_val).astype(int)
    bnb = BernoulliNB()
    bnb.fit(X_train_bn, y_train)
        """, language="python")
 
    st.markdown("📌 [View Full Code on GitHub](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis/blob/main/NASA_climate_analysis-2.ipynb)")
 
    st.markdown("---")
 
    # ----------------------------
    # (d) Results
    # ----------------------------
    st.subheader("📈 Results")
 
    # --- Multinomial NB ---
    st.markdown("### 🔵 Multinomial Naive Bayes")
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/cm_multinomial_nb.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "75.6%")
        st.write("""
        Multinomial NB achieved **75.6% accuracy**. It performed best on 
        **Low Severity** events (100% recall) but struggled with 
        **Moderate Severity**, misclassifying 6 out of 15 samples. 
        This is expected since MNB is designed for count-based data 
        and our scaled continuous features don't perfectly fit its assumptions.
        """)
 
    st.markdown("---")
 
    # --- Gaussian NB ---
    st.markdown("### 🟢 Gaussian Naive Bayes")
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/cm_gaussian_nb.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "88.9%")
        st.write("""
        Gaussian NB achieved the **highest accuracy at 88.9%**. It correctly 
        classified all Low Severity events and performed strongly across all 
        classes. Only 5 out of 45 test samples were misclassified. GNB's 
        assumption of normally distributed features aligned well with the 
        continuous climate data in this project.
        """)
 
    st.markdown("---")
 
    # --- Bernoulli NB ---
    st.markdown("### 🟠 Bernoulli Naive Bayes")
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/cm_bernoulli_nb.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "77.8%")
        st.write("""
        Bernoulli NB achieved **77.8% accuracy**. Like MNB, it correctly 
        identified all Low Severity events but had difficulty distinguishing 
        Moderate from High Severity. The binarization step (converting values 
        to 0/1) loses granular information, which limits the model's ability 
        to capture fine differences between severity levels.
        """)
 
    st.markdown("---")
 
    # --- Comparison ---
    st.markdown("### 📊 Naive Bayes Model Comparison")
 

    viza_block(
        "images/nb_comparison.png",
        "Accuracy Comparison Across All Three NB Models",
        """
    """)

 
    st.markdown("""
    | Model            | Accuracy | Best At                        | Weakness                          |
    |------------------|----------|--------------------------------|-----------------------------------|
    | Multinomial NB   | 75.6%    | Low Severity (100% recall)     | Moderate Severity confusion       |
    | Gaussian NB      | 88.9%    | All classes (balanced)         | Minor High Severity misses        |
    | Bernoulli NB     | 77.8%    | Low Severity (100% recall)     | Information loss from binarization|
    """)
 
    st.info("""
    **Why Gaussian NB performed best:**
    
    Gaussian NB assumes features follow a normal distribution, which is a 
    reasonable assumption for continuous climate measurements like latitude, 
    longitude, precipitation, and month. The other two models required 
    transformations (scaling to [0,1] or binarizing) that reduced the 
    information available to the classifier.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (e) Conclusions
    # ----------------------------
    st.subheader("✅ Conclusions")
 
    st.info("""
    **Key Findings from Naive Bayes Analysis:**
 
    1. **Gaussian NB is the best-performing NB model** for this dataset, achieving 
       88.9% accuracy in predicting wildfire severity from geographic and 
       precipitation features alone.
 
    2. **Geographic location and precipitation are meaningful predictors** of 
       wildfire severity. The models successfully learned that certain latitudes, 
       longitudes, seasons, and rainfall patterns are associated with different 
       fire risk levels.
 
    3. **Low Severity wildfires are the easiest to classify** — all three models 
       achieved 100% recall for this class, suggesting these events have distinct 
       geographic and precipitation signatures.
 
    4. **Moderate Severity is hardest to distinguish** from other classes, which 
       makes sense since it represents the middle ground between extremes.
 
    5. **Choosing the right NB variant matters.** The same data produced accuracies 
       ranging from 75.6% to 88.9% depending on the assumptions made about 
       feature distributions. This highlights the importance of matching the 
       model to the data characteristics.
    """)
 
    st.success("""
    **Prediction Insight:** Using only latitude, longitude, month, and 
    precipitation, we can predict wildfire severity with up to 88.9% accuracy. 
    This suggests that geographic and seasonal patterns play a significant role 
    in determining how severe a wildfire event becomes.
    """)












# decision tree

with tab8:
 
    st.header("🌳 Decision Tree Classification")
 
    # ----------------------------
    # (a) Overview
    # ----------------------------
    st.subheader("🔍 Overview: What are Decision Trees?")
 
    st.info("""
    A **Decision Tree (DT)** is a supervised machine learning algorithm that learns 
    to classify data by splitting it into branches based on feature values, forming 
    a tree-like structure of decisions. At the top of the tree is the **root node**, 
    which represents the first and most important feature split. From the root, the 
    data flows down through **internal nodes** (additional decision points) until it 
    reaches **leaf nodes**, which represent the final predicted class. Each split in 
    the tree is chosen to best separate the data into groups that are as pure as 
    possible, meaning each group ideally contains only one class. Decision Trees are 
    popular because they are easy to visualize, interpret, and explain to non-technical 
    audiences. They can handle both numerical and categorical data without requiring 
    extensive preprocessing like scaling or normalization. Decision Trees are widely 
    used in medical diagnosis, fraud detection, customer segmentation, and environmental 
    risk classification. However, they can be prone to **overfitting** if the tree grows 
    too deep, which is why hyperparameters like `max_depth` and `min_samples_leaf` are 
    used to control tree complexity. In this project, Decision Trees were used to classify 
    wildfire severity levels based on geographic and precipitation features.
    """)
 
    st.markdown("---")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info("""
        **📏 Gini Impurity**
 
        Gini Impurity is one of the two main criteria used by Decision Trees to evaluate 
        the quality of a split at each node. It measures how often a randomly chosen element 
        from a set would be incorrectly classified if it were labeled randomly according to 
        the distribution of labels in that set. A Gini value of **0** means the node is 
        perfectly pure — all samples belong to one class. A higher Gini value means the node 
        contains a more mixed population of classes. The formula for Gini Impurity is:
 
        `Gini = 1 - Σ(pᵢ)²`
 
        where `pᵢ` is the proportion of samples belonging to class `i`. For example, if a 
        node contains 50% class A and 50% class B, the Gini is `1 - (0.5² + 0.5²) = 0.5`, 
        which is the maximum impurity for a binary split. If the node is 100% class A, the 
        Gini is `1 - (1.0²) = 0.0`, which is perfectly pure. The Decision Tree algorithm 
        tries every possible feature and threshold combination at each node, calculates the 
        Gini for each resulting child node, and picks the split that produces the lowest 
        weighted average Gini across the children.
        """)
 
    with col2:
        st.info("""
        **📐 Entropy & Information Gain**
 
        Entropy is the second main criterion for evaluating splits in Decision Trees, 
        borrowed from information theory. It measures the amount of disorder or uncertainty 
        in a set of labels. A node where all samples belong to one class has **entropy = 0** 
        (no uncertainty), while a node with an equal mix of classes has the highest entropy. 
        The formula for Entropy is:
 
        `Entropy = -Σ pᵢ × log₂(pᵢ)`
 
        **Information Gain** is the reduction in entropy achieved by splitting the data on a 
        particular feature. It is calculated as the entropy of the parent node minus the 
        weighted average entropy of the child nodes after the split. The feature and threshold 
        that produce the **highest Information Gain** are selected for the split. For example, 
        if a parent node has entropy 1.0 and splitting on latitude produces children with 
        weighted entropy 0.6, the Information Gain is 0.4. Higher Information Gain means the 
        split does a better job of separating the classes. Both Gini and Entropy generally 
        produce similar trees, but Entropy can sometimes create slightly more balanced splits 
        because it penalizes impurity more aggressively.
        """)
 
    st.markdown("---")
 
    st.subheader("📌 Gini vs Entropy — Small Example")
 
    st.info("""
    **Example: Splitting 10 wildfire events by latitude**
 
    Suppose we have 10 events: 5 High Severity and 5 Low Severity. We consider splitting 
    at latitude = 30°.
 
    **Left child (latitude ≤ 30°):** 4 High, 1 Low → 5 samples  
    **Right child (latitude > 30°):** 1 High, 4 Low → 5 samples
 
    **Gini Calculation:**
    - Left Gini = 1 - (4/5)² - (1/5)² = 1 - 0.64 - 0.04 = **0.32**
    - Right Gini = 1 - (1/5)² - (4/5)² = 1 - 0.04 - 0.64 = **0.32**
    - Weighted Gini = (5/10 × 0.32) + (5/10 × 0.32) = **0.32**
 
    **Entropy & Information Gain Calculation:**
    - Parent Entropy = -0.5 × log₂(0.5) - 0.5 × log₂(0.5) = **1.0**
    - Left Entropy = -4/5 × log₂(4/5) - 1/5 × log₂(1/5) = **0.722**
    - Right Entropy = -1/5 × log₂(1/5) - 4/5 × log₂(4/5) = **0.722**
    - Weighted Child Entropy = (5/10 × 0.722) + (5/10 × 0.722) = **0.722**
    - **Information Gain = 1.0 - 0.722 = 0.278**
 
    The positive Information Gain of 0.278 tells us this split reduces uncertainty by 
    about 28%, making it a useful division of the data.
    """)
 
    st.markdown("---")
 
    st.subheader("♾️ Why Infinite Trees Are Possible")
 
    st.info("""
    It is generally possible to create an **infinite number of different decision trees** 
    from the same dataset because there are countless ways to configure the tree structure. 
    First, at every node the algorithm can choose from any feature and any threshold value 
    to split on, and since continuous features like latitude or precipitation have infinitely 
    many possible split points, the number of candidate trees is unbounded. Second, the 
    **order** in which features are selected matters — choosing latitude first versus longitude 
    first produces entirely different tree structures even if both achieve similar accuracy. 
    Third, hyperparameters like `max_depth`, `min_samples_split`, `min_samples_leaf`, and 
    `random_state` all change which branches are grown and which are pruned, leading to 
    different final trees. Fourth, using different splitting criteria (Gini vs Entropy) can 
    produce different split decisions at each node. Fifth, random subsampling of training 
    data or features (as in Random Forests) generates yet more tree variations. Even small 
    changes to the random seed can cause the algorithm to break ties differently when two 
    features produce equally good splits, resulting in a completely different tree. This is 
    why in this project we deliberately built three trees with different configurations — to 
    demonstrate how the same data can produce structurally different models with different 
    root nodes, depths, and accuracy levels.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (b) Data Preparation
    # ----------------------------
    st.subheader("⚙️ Data Preparation")
 
    st.info("""
    The data preparation for Decision Trees followed the same pipeline established in the 
    Naive Bayes section, ensuring a fair and consistent comparison across all models. The 
    target variable is **wildfire severity** (Low, Moderate, High), created from a composite 
    risk score combining temperature, humidity, and wind speed. The features used for 
    prediction are **latitude, longitude, month, and precipitation** — these are independent 
    of the variables used to construct the label, preventing data leakage. One of the 
    advantages of Decision Trees is that they do **not require feature scaling** or 
    normalization, unlike Naive Bayes models which needed MinMaxScaler, StandardScaler, or 
    binarization. The raw feature values are used directly, and the tree algorithm finds 
    optimal split thresholds on the original scale. The dataset was split into **70% training** 
    (105 samples) and **30% testing** (45 samples) using stratified sampling to maintain 
    equal class proportions. The training and testing sets are completely **disjoint** — no 
    sample appears in both sets. This disjoint property is critical because if the model saw 
    test data during training, accuracy would be artificially inflated and the model would 
    not generalize to new unseen data. Stratification ensures that each severity class has 
    equal representation in both sets (35 training, 15 testing per class), preventing the 
    model from being biased toward the majority class.
    """)
 
    st.image("images/dt_train_test_sample.png",
             caption="Training and Testing Set Samples — Same Disjoint Split as Naive Bayes",
             use_container_width=True)
 
    st.markdown("📌 [View Data Preparation Code on GitHub](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis/blob/main/NASA_climate_analysis-2.ipynb)")
 
    st.markdown("---")
 
    # ----------------------------
    # (c) Code
    # ----------------------------
    st.subheader("💻 Decision Tree Implementation Code")
 
    st.info("""
    Three different Decision Tree classifiers were built using **Scikit-Learn's 
    DecisionTreeClassifier**. Each tree was configured with different hyperparameters 
    to produce structurally different models with different root nodes, depths, and 
    accuracy levels. Tree 1 uses the Gini criterion with a maximum depth of 4, Tree 2 
    uses the Entropy criterion with a maximum depth of 5, and Tree 3 uses Gini with a 
    shallower depth of 3 and a minimum leaf size of 5. Different random seeds were also 
    used to encourage different tie-breaking behavior during training. The trees were 
    visualized using Scikit-Learn's `plot_tree` function, which shows every split decision, 
    the Gini or Entropy value at each node, the number of samples, and the predicted class. 
    Feature importance was extracted from the best-performing tree to understand which 
    geographic and climate variables contribute most to severity prediction. The code also 
    generates confusion matrices for each tree to evaluate classification performance 
    across all three severity levels.
    """)
 
    st.code("""
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
    
    features = ["latitude", "longitude", "month", "precip"]
    # X_train, X_test, y_train, y_test already created from stratified split
    
    # Tree 1: Gini criterion, max_depth=4
    dt1 = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
    dt1.fit(X_train, y_train)
    y_pred_dt1 = dt1.predict(X_test)
    acc_dt1 = accuracy_score(y_test, y_pred_dt1)
    
    # Tree 2: Entropy criterion, max_depth=5
    dt2 = DecisionTreeClassifier(criterion="entropy", max_depth=5, random_state=42)
    dt2.fit(X_train, y_train)
    y_pred_dt2 = dt2.predict(X_test)
    acc_dt2 = accuracy_score(y_test, y_pred_dt2)
    
    # Tree 3: Gini, max_depth=3, min_samples_leaf=5, different seed
    dt3 = DecisionTreeClassifier(criterion="gini", max_depth=3, 
                                min_samples_leaf=5, random_state=99)
    dt3.fit(X_train[features[::-1]], y_train)  # reversed feature order
    y_pred_dt3 = dt3.predict(X_test[features[::-1]])
    acc_dt3 = accuracy_score(y_test, y_pred_dt3)
    
    # Visualize trees
    plot_tree(dt1, feature_names=features, class_names=le.classes_,
          filled=True, rounded=True)
    """, language="python")
 
    st.markdown("📌 [View Full Decision Tree Code on GitHub](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis/blob/main/NASA_climate_analysis-2.ipynb)")
 
    st.markdown("---")
 
    # ----------------------------
    # (d) Results
    # ----------------------------
    st.subheader("📈 Results")
 
    # --- Tree 1 ---
    st.markdown("### 🟣 Decision Tree 1 — Gini, max_depth=4")
 
    st.image("images/dt1_tree.png",
             caption="Decision Tree 1 — Full Tree Visualization (Gini, depth=4)",
             use_container_width=True)
 
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/dt1_cm.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "71.1%")
        st.write("""
        Decision Tree 1 was built using the **Gini impurity** criterion with a maximum 
        depth of 4 and achieved the highest accuracy among all three trees at **71.1%**. 
        The tree correctly classified 32 out of 45 test samples across the three severity 
        classes. Looking at the confusion matrix, the model performed best on **Moderate 
        Severity** events with 11 correct predictions out of 15, and reasonably well on 
        **High Severity** with 11 correct out of 15. However, **Low Severity** proved 
        more challenging with only 10 correct out of 15, with 5 samples being misclassified 
        as Moderate Severity. The root node of this tree splits on **latitude**, confirming 
        that geographic location is the most discriminative feature for wildfire severity 
        prediction. The tree visualization shows that latitude and longitude dominate the 
        upper levels of the tree, while month and precipitation appear in deeper splits 
        for finer distinctions. The depth of 4 provides a good balance between model 
        complexity and generalization, capturing important patterns without overfitting 
        to training noise. This tree serves as the baseline for comparison with the other 
        two configurations.
        """)
 
    st.markdown("---")
 
    # --- Tree 2 ---
    st.markdown("### 🔴 Decision Tree 2 — Entropy, max_depth=5")
 
    st.image("images/dt2_tree.png",
             caption="Decision Tree 2 — Full Tree Visualization (Entropy, depth=5)",
             use_container_width=True)
 
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/dt2_cm.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "66.7%")
        st.write("""
        Decision Tree 2 was built using the **Entropy** criterion with a deeper maximum 
        depth of 5 and achieved **66.7% accuracy**, lower than Tree 1 despite having a 
        more complex structure. This is a clear example of **overfitting** — the deeper 
        tree learned very specific patterns from the training data that did not generalize 
        well to the test set. The confusion matrix reveals that the model correctly 
        classified 12 out of 15 High Severity events, which is actually better than Tree 1 
        for that class. However, it performed significantly worse on **Low Severity** (only 
        10 correct) and **Moderate Severity** (only 8 correct), with 5 Moderate events 
        being misclassified as High Severity. The additional depth allowed the tree to 
        create very narrow, specific rules that fit training noise rather than true patterns. 
        The tree visualization shows a much larger and more complex structure with many 
        more leaf nodes compared to Tree 1. The root node again splits on **latitude**, 
        consistent with Tree 1, but the subsequent splits differ due to the Entropy 
        criterion's different sensitivity to class imbalance at each node. This result 
        demonstrates that a deeper and more complex model does not always produce better 
        predictions, and that simpler trees can sometimes outperform their deeper counterparts.
        """)
 
    st.markdown("---")
 
    # --- Tree 3 ---
    st.markdown("### 🟢 Decision Tree 3 — Gini, max_depth=3, min_leaf=5")
 
    st.image("images/dt3_tree.png",
             caption="Decision Tree 3 — Full Tree Visualization (Gini, depth=3, different root)",
             use_container_width=True)
 
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/dt3_cm.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "64.4%")
        st.write("""
        Decision Tree 3 was built with the **Gini criterion**, a shallower maximum depth 
        of 3, a minimum of 5 samples per leaf node, and a different random seed (99) to 
        encourage structural variation. It achieved the lowest accuracy at **64.4%**, 
        classifying 29 out of 45 test samples correctly. The `min_samples_leaf=5` constraint 
        prevents the tree from creating overly specific leaf nodes, resulting in broader and 
        more generalized decision boundaries. The confusion matrix shows strong performance 
        on **High Severity** (11 correct out of 15) and **Moderate Severity** (10 correct), 
        but poor performance on **Low Severity** with only 8 correct and 7 samples misclassified 
        as Moderate Severity. The root node of this tree also splits on **latitude**, consistent 
        with the other two trees, which reinforces that latitude is the single most important 
        feature regardless of tree configuration. The shallower depth of 3 means the tree has 
        fewer decision nodes and cannot capture as many fine-grained patterns as Trees 1 and 2. 
        While this tree has the lowest accuracy, its simpler structure makes it the most 
        interpretable and least prone to overfitting — it would likely perform more consistently 
        on completely new data from different time periods or regions.
        """)
 
    st.markdown("---")
 
    # --- Feature Importance ---
    st.markdown("### 📊 Feature Importance Analysis")
 
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/dt_feature_importance.png", use_container_width=True)
    with col2:
        st.write("""
        Feature importance was extracted from Tree 1 (the best-performing model at 71.1% 
        accuracy) to understand which variables contribute most to wildfire severity 
        classification. **Latitude** is by far the most important feature with an importance 
        score exceeding 0.50, meaning more than half of the tree's decision-making power 
        comes from geographic latitude alone. This makes physical sense because latitude 
        determines a region's climate zone, vegetation type, and solar exposure — all critical 
        factors in wildfire behavior. **Longitude** is the second most important feature with 
        a score around 0.33, reflecting that east-west positioning captures continental vs 
        coastal climate differences that affect fire conditions. Together, latitude and longitude 
        account for over 83% of the model's predictive power, showing that **geographic location 
        is the dominant factor** in wildfire severity. **Month** contributes about 10% of the 
        importance, capturing seasonal patterns in wildfire activity. **Precipitation** has 
        the smallest importance at roughly 2%, which is surprising but suggests that once 
        geographic location is known, precipitation adds relatively little additional 
        information for severity prediction in this dataset.
        """)
 
    st.markdown("---")
 
    # --- Comparison ---
    st.markdown("### 📊 Decision Tree Model Comparison")
 
    st.image("images/dt_comparison.png",
             caption="Accuracy Comparison Across All Three Decision Trees",
             use_container_width=True)
 
    st.markdown("""
    | Tree Configuration                    | Criterion | Max Depth | Root Feature | Accuracy |
    |---------------------------------------|-----------|-----------|-------------|----------|
    | Tree 1 (Gini, d=4)                    | Gini      | 4         | Latitude    | 71.1%    |
    | Tree 2 (Entropy, d=5)                 | Entropy   | 5         | Latitude    | 66.7%    |
    | Tree 3 (Gini, d=3, leaf≥5)            | Gini      | 3         | Latitude    | 64.4%    |
    """)
 
    st.info("""
    **Key Observations from the Comparison:**
 
    All three trees selected **latitude** as the root node, confirming it is the most 
    discriminative feature regardless of the splitting criterion or hyperparameters used. 
    Tree 1 with Gini criterion and depth 4 achieved the best accuracy at 71.1%, suggesting 
    that a moderate depth provides the best trade-off between underfitting and overfitting 
    for this dataset size. Tree 2 with Entropy and depth 5 actually performed worse despite 
    being more complex, demonstrating that deeper trees are not always better — the additional 
    depth led to overfitting on the 105-sample training set. Tree 3 with the shallowest depth 
    of 3 had the lowest accuracy but is the most interpretable and robust model. The accuracy 
    spread of 64.4% to 71.1% across three different configurations shows that Decision Trees 
    are moderately sensitive to hyperparameter choices. Overall, Decision Trees achieved lower 
    accuracy than Gaussian Naive Bayes (88.9%) on this dataset, suggesting that the probabilistic 
    approach of GNB better captures the relationships in this climate data.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (e) Conclusions
    # ----------------------------
    st.subheader("✅ Conclusions")
 
    st.info("""
    **Key Findings from Decision Tree Analysis:**
 
    1. **Latitude is the most important feature** for predicting wildfire severity, selected 
       as the root node by all three trees regardless of criterion or configuration. This 
       confirms that geographic location is the primary determinant of fire risk, which aligns 
       with domain knowledge about how latitude influences climate zones, vegetation, and 
       solar radiation patterns.
 
    2. **Geographic features (latitude + longitude) dominate** the model's predictive power, 
       accounting for over 83% of feature importance in the best-performing tree. This suggests 
       that knowing where a wildfire occurs tells us more about its likely severity than knowing 
       the season or local precipitation levels.
 
    3. **Moderate tree depth performs best** — Tree 1 (depth=4) outperformed both the deeper 
       Tree 2 (depth=5) and the shallower Tree 3 (depth=3). This illustrates the classic 
       bias-variance tradeoff: too shallow and the model underfits, too deep and it overfits.
 
    4. **Decision Trees are interpretable but less accurate than Gaussian NB** on this dataset. 
       The best Decision Tree achieved 71.1% compared to Gaussian NB's 88.9%. However, Decision 
       Trees provide clear, visual explanations of how predictions are made, which is valuable 
       for communicating results to stakeholders.
 
    5. **Infinite tree configurations are possible** from the same data, and even small changes 
       to hyperparameters (depth, criterion, minimum leaf size, random seed) produce structurally 
       different trees with different accuracy levels, reinforcing the importance of 
       hyperparameter tuning in machine learning.
    """)
 
    st.success("""
    **Prediction Insight:** Decision Trees reveal that wildfire severity is primarily driven 
    by **where** the fire occurs (latitude and longitude), with seasonal timing (month) and 
    local precipitation playing secondary roles. This geographic dominance suggests that 
    region-specific fire management strategies may be more effective than one-size-fits-all 
    approaches based solely on weather conditions.
    """)














# Regression


with tab9:
 
    st.header("📈 Regression Analysis")
 
    # ----------------------------
    # (a) Define Linear Regression
    # ----------------------------
    st.subheader("🔍 What is Linear Regression?")
 
    st.info("""
    **Linear Regression** is a supervised learning algorithm that models the relationship 
    between a continuous dependent variable (target) and one or more independent variables 
    (features) by fitting a straight line through the data. The goal is to find the line 
    (or hyperplane in multiple dimensions) that minimizes the sum of squared differences 
    between the predicted values and the actual values, a method known as **Ordinary Least 
    Squares (OLS)**. The equation takes the form `y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ`, 
    where `β₀` is the intercept and `β₁...βₙ` are the coefficients that represent how much 
    each feature contributes to the prediction. Linear regression assumes a linear relationship 
    between features and target, that residuals are normally distributed, and that features 
    are not highly correlated with each other (no multicollinearity). It is one of the most 
    widely used algorithms in statistics and machine learning due to its simplicity, 
    interpretability, and efficiency. Common applications include predicting house prices, 
    stock trends, sales forecasting, and any scenario where the output is a continuous number. 
    The model's performance is typically evaluated using metrics like R-squared, Mean Squared 
    Error (MSE), and Root Mean Squared Error (RMSE). Linear regression can only predict 
    continuous numerical outcomes — it cannot directly handle classification tasks where the 
    output is a category label. For classification problems, we turn to **Logistic Regression**, 
    which adapts the linear approach to produce probability-based class predictions.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (b) Define Logistic Regression
    # ----------------------------
    st.subheader("🔍 What is Logistic Regression?")
 
    st.info("""
    **Logistic Regression** is a supervised classification algorithm that predicts the 
    probability that an input belongs to a particular class, despite having "regression" 
    in its name. Instead of predicting a continuous value like linear regression, logistic 
    regression outputs a probability between 0 and 1, which is then mapped to a class label 
    using a decision threshold (typically 0.5). It achieves this by applying the **Sigmoid 
    (logistic) function** to a linear combination of input features, transforming the output 
    from an unbounded range into the [0, 1] probability range. The model learns coefficients 
    for each feature that maximize the likelihood of correctly classifying the training data, 
    a process called **Maximum Likelihood Estimation (MLE)**. For binary classification, 
    logistic regression draws a decision boundary that separates two classes, while for 
    multi-class problems (like our three severity levels), it can use strategies like 
    **one-vs-rest** or **multinomial** (softmax) to handle multiple classes simultaneously. 
    Logistic regression is widely used in medical diagnosis (disease vs. healthy), spam 
    detection (spam vs. not spam), credit scoring (approve vs. reject), and environmental 
    classification. It is computationally efficient, works well with linearly separable data, 
    and produces interpretable probability outputs that allow stakeholders to understand 
    prediction confidence. Unlike Decision Trees, logistic regression assumes a linear 
    relationship between features and the log-odds of the outcome, which can be a limitation 
    for highly nonlinear data. In this project, logistic regression was used to classify 
    wildfire severity levels using geographic and precipitation features.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (c) Similarities and Differences
    # ----------------------------
    st.subheader("🔄 How Are They Similar and Different?")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info("""
        **✅ Similarities**
 
        Both linear and logistic regression are **supervised learning** algorithms that learn 
        from labeled training data to make predictions on new unseen data. At their core, both 
        models compute a **linear combination** of input features — they multiply each feature 
        by a learned coefficient and sum the results to produce an intermediate value. Both 
        algorithms are **parametric models**, meaning they assume a specific functional form 
        for the relationship between features and output, and both learn a fixed set of 
        parameters (coefficients) during training. Both methods benefit from **feature scaling** 
        to improve convergence speed and numerical stability during optimization. They are both 
        interpretable models where the magnitude and sign of each coefficient directly indicate 
        how much and in which direction each feature influences the prediction. Both can handle 
        multiple input features simultaneously and can be extended with regularization techniques 
        (L1/Lasso, L2/Ridge) to prevent overfitting. Both are foundational algorithms taught in 
        every machine learning curriculum and serve as important baselines before trying more 
        complex models. Additionally, both assume that the input features are reasonably 
        independent of each other and that there is a meaningful relationship between the 
        features and the target variable.
        """)
 
    with col2:
        st.info("""
        **❌ Differences**
 
        The fundamental difference is in **what they predict**: linear regression predicts a 
        continuous numerical value (e.g., temperature = 27.5°C), while logistic regression 
        predicts a categorical class label through probabilities (e.g., High Severity with 
        85% probability). Linear regression uses **Ordinary Least Squares** to minimize the 
        sum of squared errors, while logistic regression uses **Maximum Likelihood Estimation** 
        to maximize the probability of correct classification. Linear regression produces 
        unbounded output from negative infinity to positive infinity, while logistic regression 
        applies the **Sigmoid function** to constrain output between 0 and 1. The loss function 
        differs: linear regression uses Mean Squared Error, while logistic regression uses 
        **cross-entropy loss** (log loss). Linear regression assumes normally distributed 
        residuals, while logistic regression assumes the target follows a Bernoulli or 
        multinomial distribution. Linear regression's output is directly the prediction, while 
        logistic regression's output is a probability that requires a threshold to become a 
        class label. Linear regression is evaluated with R², MSE, and RMSE, while logistic 
        regression is evaluated with accuracy, precision, recall, F1-score, and confusion 
        matrices. Finally, linear regression cannot handle classification tasks, while logistic 
        regression cannot predict continuous values.
        """)
 
    st.markdown("""
    | Aspect              | Linear Regression           | Logistic Regression              |
    |---------------------|-----------------------------|----------------------------------|
    | **Output**          | Continuous value             | Class probability (0 to 1)       |
    | **Function**        | Linear (y = mx + b)         | Sigmoid applied to linear combo  |
    | **Loss Function**   | Mean Squared Error           | Cross-Entropy (Log Loss)         |
    | **Optimization**    | Ordinary Least Squares       | Maximum Likelihood Estimation    |
    | **Use Case**        | Predict prices, quantities   | Classify categories, yes/no      |
    | **Evaluation**      | R², MSE, RMSE               | Accuracy, Precision, Recall, F1  |
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (d) Sigmoid Function
    # ----------------------------
    st.subheader("📐 Does Logistic Regression Use the Sigmoid Function?")
 
    st.info("""
    **Yes**, logistic regression fundamentally relies on the **Sigmoid function** (also called 
    the logistic function) to transform its predictions into probabilities. The Sigmoid function 
    is defined as `σ(z) = 1 / (1 + e^(-z))`, where `z` is the linear combination of input 
    features (`z = β₀ + β₁x₁ + β₂x₂ + ...`). Without the Sigmoid, logistic regression would 
    just be linear regression — it would output unbounded values that could be negative or 
    greater than 1, which are meaningless as probabilities. The Sigmoid function maps any real 
    number to the range (0, 1), making the output interpretable as the probability of belonging 
    to the positive class. When `z` is very large and positive, the Sigmoid outputs a value 
    close to 1 (high probability of positive class). When `z` is very large and negative, the 
    Sigmoid outputs a value close to 0 (high probability of negative class). When `z = 0`, the 
    Sigmoid outputs exactly 0.5, representing maximum uncertainty. The S-shaped curve of the 
    Sigmoid is smooth and differentiable everywhere, which is essential for gradient-based 
    optimization during model training. For multi-class problems like our three-class severity 
    prediction, the Sigmoid is generalized to the **Softmax function**, which outputs a 
    probability distribution across all classes that sums to 1. The Sigmoid's gradient 
    (derivative) has a convenient mathematical property: `σ'(z) = σ(z) × (1 - σ(z))`, 
    which simplifies the backpropagation calculations during training.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # (e) Maximum Likelihood Estimation
    # ----------------------------
    st.subheader("📊 How is Maximum Likelihood Connected to Logistic Regression?")
 
    st.info("""
    **Maximum Likelihood Estimation (MLE)** is the optimization method that logistic regression 
    uses to learn its coefficients from training data, making it the mathematical engine behind 
    the model. The core idea of MLE is to find the set of model parameters (coefficients) that 
    make the observed training data most probable — in other words, the parameters that maximize 
    the **likelihood function**. For logistic regression, the likelihood function is the product 
    of all individual prediction probabilities: for each correctly classified sample, we want 
    the predicted probability to be as close to 1 as possible, and for each incorrectly 
    classified sample, as close to 0 as possible. In practice, we work with the **log-likelihood** 
    (the natural logarithm of the likelihood) because products become sums, which are 
    computationally easier to optimize and numerically more stable. The negative log-likelihood 
    is equivalent to the **cross-entropy loss** function, which is minimized during training 
    using gradient descent or more advanced optimizers like L-BFGS (Limited-memory 
    Broyden–Fletcher–Goldfarb–Shanno). Unlike linear regression's OLS which has a closed-form 
    solution, logistic regression's MLE requires iterative numerical optimization because the 
    Sigmoid function makes the problem non-linear. At each iteration, the optimizer computes 
    the gradient of the log-likelihood with respect to each coefficient and updates the 
    coefficients in the direction that increases the likelihood. Convergence is reached when 
    the changes between iterations become negligibly small, indicated by parameters like 
    `max_iter` in Scikit-Learn. MLE ensures that the final model coefficients are statistically 
    optimal — no other set of coefficients could explain the training data better under the 
    logistic regression assumptions.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Coding: Multi-class Logistic Regression
    # ----------------------------
    st.subheader("💻 Logistic Regression Implementation")
 
    st.info("""
    Logistic Regression was applied to the same wildfire severity dataset used for Naive Bayes 
    and Decision Trees, ensuring a fair comparison across all model families. The features used 
    are **latitude, longitude, month, and precipitation**, and the target is the three-class 
    severity label (Low, Moderate, High). The data was standardized using StandardScaler before 
    fitting, as logistic regression's gradient-based optimization converges faster and more 
    reliably with scaled features. The `multinomial` multi-class strategy with the `lbfgs` 
    solver was used, which directly models all three classes simultaneously using the Softmax 
    function rather than training separate binary classifiers. For the binary comparison, a 
    subset containing only **Low Severity** and **Moderate Severity** events was created to 
    directly compare Logistic Regression against Multinomial Naive Bayes on a two-class problem. 
    These two adjacent severity levels were chosen because they are the hardest to distinguish, 
    providing a more meaningful comparison than the easily separable Low vs High pair. The 
    binary Logistic Regression used StandardScaler while the binary Multinomial NB used 
    MinMaxScaler, each matching their respective model's requirements. Both models were 
    evaluated on the same stratified test set to ensure an apples-to-apples comparison. All 
    code was implemented using Scikit-Learn's `LogisticRegression` class with `max_iter=1000` 
    to ensure convergence.
    """)
 
    st.code("""
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
    
    # Multi-class Logistic Regression
    lr_multi = LogisticRegression(
        multi_class="multinomial", solver="lbfgs",
        max_iter=1000, random_state=42)
    lr_multi.fit(X_train_g, y_train)   # X_train_g = StandardScaler transformed
    y_pred_lr = lr_multi.predict(X_test_g)
    acc_lr = accuracy_score(y_test, y_pred_lr)  # 97.8%
    
    # Binary: Low_Severity vs Moderate_Severity
    top2 = ["Low_Severity", "Moderate_Severity"]
    mask = combined_df["severity"].isin(top2)
    X_binary = combined_df.loc[mask, features]
    y_binary = LabelEncoder().fit_transform(combined_df.loc[mask, "severity"])
    
    # Binary Logistic Regression
    lr_bin = LogisticRegression(max_iter=1000, random_state=42, C=0.5)
    lr_bin.fit(X_train_bs, y_train_b)
    
    # Binary Multinomial NB
    mnb_bin = MultinomialNB(alpha=2.0)
    mnb_bin.fit(X_train_bmn, y_train_b)
        """, language="python")
 
    st.markdown("📌 [View Full Regression Code on GitHub](https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis/blob/main/NASA_climate_analysis-2.ipynb)")
 
    st.markdown("---")
 
    # ----------------------------
    # Results: Multi-class LR
    # ----------------------------
    st.subheader("📈 Multi-class Logistic Regression Results")
 
    col1, col2 = st.columns([1.3, 2])
    with col1:
        st.image("images/lr_multiclass_cm.png", use_container_width=True)
    with col2:
        st.metric("Accuracy", "97.8%")
        st.write("""
        Multi-class Logistic Regression achieved an outstanding **97.8% accuracy**, correctly 
        classifying 44 out of 45 test samples across all three wildfire severity levels. This 
        is the highest accuracy achieved by any model in this project, significantly outperforming 
        both Gaussian Naive Bayes (88.9%) and the best Decision Tree (71.1%). The confusion 
        matrix reveals near-perfect classification: all 15 High Severity and all 15 Low Severity 
        events were classified correctly with zero errors, and 14 out of 15 Moderate Severity 
        events were correct with only a single sample misclassified as Low Severity. The model 
        achieved perfect precision (1.00) for both High and Moderate Severity, meaning every 
        sample it predicted as High or Moderate was actually that class. The recall was also 
        perfect (1.00) for High and Low Severity, meaning it identified every single High and 
        Low event without any misses. The only imperfection was one Moderate Severity event that 
        was incorrectly labeled as Low, giving Moderate Severity a recall of 0.93. The F1-scores 
        across all classes were 0.97 or higher, indicating excellent and balanced performance. 
        This exceptional performance suggests that there are strong linear relationships between 
        the geographic and precipitation features and the severity labels, which logistic 
        regression's linear decision boundaries can capture effectively. The `lbfgs` optimizer 
        converged within the 1000 iteration limit, confirming the model's stability.
        """)
 
    st.markdown("---")
 
    # ----------------------------
    # Results: Binary Comparison
    # ----------------------------
    st.subheader("📊 Binary Classification: Logistic Regression vs Multinomial NB")
 
    st.image("images/lr_binary_comparison.png",
             caption="Binary Classification: Low Severity vs Moderate Severity",
             use_container_width=True)
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info("""
        **Logistic Regression — Accuracy: 70.0%**
 
        In the binary classification task comparing Low Severity against Moderate Severity 
        events, Logistic Regression achieved **70.0% accuracy**, correctly classifying 21 out 
        of 30 test samples. The confusion matrix shows that the model performed well on Low 
        Severity with 13 correct out of 15, but struggled significantly with Moderate Severity, 
        correctly identifying only 8 out of 15 while misclassifying 7 as Low Severity. This 
        indicates that the linear decision boundary drawn by logistic regression tends to favor 
        the Low Severity class, possibly because Low Severity events have more distinct geographic 
        signatures. The regularization parameter C=0.5 added moderate regularization to prevent 
        overfitting on this smaller binary subset. The drop from 97.8% (multi-class) to 70.0% 
        (binary) is expected because Low and Moderate Severity are adjacent classes with 
        overlapping feature distributions, making them inherently harder to separate than the 
        three-class problem where High Severity provides additional contrast.
        """)
 
    with col2:
        st.info("""
        **Multinomial NB — Accuracy: 73.3%**
 
        Multinomial Naive Bayes achieved **73.3% accuracy** on the same binary task, slightly 
        outperforming Logistic Regression by 3.3 percentage points. The confusion matrix shows 
        that MNB also correctly classified 13 out of 15 Low Severity events (same as LR), but 
        performed better on Moderate Severity with 9 correct out of 15 compared to LR's 8. 
        This means MNB misclassified only 6 Moderate events as Low, compared to LR's 7. The 
        alpha=2.0 smoothing parameter helped MNB handle the limited training data by preventing 
        zero-probability issues that can occur with small sample sizes. The fact that MNB 
        outperformed LR on this binary task is notable because MNB achieved lower accuracy on 
        the full three-class problem (75.6% vs 97.8%). This reversal suggests that Multinomial 
        NB's probabilistic approach handles the overlapping distributions between adjacent 
        severity classes slightly better than LR's linear boundary when only two classes are 
        present.
        """)
 
    st.markdown("""
    | Model                | Binary Accuracy | Strength                          | Weakness                        |
    |----------------------|----------------|-----------------------------------|---------------------------------|
    | Logistic Regression  | 70.0%          | Strong Low Severity detection     | Misclassifies Moderate as Low   |
    | Multinomial NB       | 73.3%          | Better Moderate Severity recall   | Still struggles with overlap    |
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Conclusions
    # ----------------------------
    st.subheader("✅ Regression Conclusions")
 
    st.info("""
    **Key Findings from Logistic Regression Analysis:**
 
    1. **Logistic Regression is the best overall model** in this project, achieving 97.8% 
       accuracy on the three-class wildfire severity prediction task. Its linear decision 
       boundaries effectively separate the severity levels based on latitude, longitude, month, 
       and precipitation, outperforming all Naive Bayes variants and all Decision Tree 
       configurations by a significant margin.
 
    2. **The Sigmoid function and Maximum Likelihood Estimation** work together to produce 
       well-calibrated probability predictions. The model doesn't just classify — it provides 
       confidence scores that could be used for risk assessment, such as flagging events with 
       borderline severity scores for closer monitoring.
 
    3. **Adjacent severity classes are harder to separate** than the full three-class problem. 
       Both LR (70.0%) and MNB (73.3%) showed reduced accuracy when tasked with distinguishing 
       only Low from Moderate Severity, confirming that these middle classes have overlapping 
       geographic and precipitation profiles.
 
    4. **Multinomial NB slightly outperforms LR on binary classification** (73.3% vs 70.0%), 
       suggesting that probabilistic models handle overlapping distributions between similar 
       classes marginally better than linear boundary methods.
 
    5. **Feature scaling is essential for logistic regression** — StandardScaler normalization 
       ensured fast convergence and numerically stable coefficient estimation, contributing 
       to the model's strong performance.
    """)
 
    st.success("""
    **Prediction Insight:** Logistic Regression demonstrates that wildfire severity can be 
    predicted with near-perfect accuracy (97.8%) using only four geographic and climate 
    features. This has practical implications for early warning systems — given a fire's 
    coordinates, the month, and local precipitation data, responders could quickly estimate 
    the likely severity and allocate resources accordingly.
    """)









# all models


with tab10:
 
    st.header("🤖 Machine Learning Models — Complete Comparison")
 
    # ----------------------------
    # Overview
    # ----------------------------
    st.subheader("🔍 Overview of All Models Used")
 
    st.info("""
    Throughout this project, **seven different supervised classification models** were trained 
    and evaluated on the same wildfire severity prediction task, using the same train/test 
    split to ensure a fair and consistent comparison. The models span three major algorithm 
    families: **Naive Bayes** (Multinomial, Gaussian, and Bernoulli), **Decision Trees** 
    (three configurations with different criteria, depths, and constraints), and **Logistic 
    Regression** (multinomial multi-class). All models were trained on 105 samples (70%) and 
    tested on 45 samples (30%) with stratified sampling to maintain equal class representation. 
    The target variable is wildfire severity (Low, Moderate, High), derived from a composite 
    risk score of temperature, humidity, and wind speed. The prediction features are latitude, 
    longitude, month, and precipitation — variables that are independent of the label 
    construction. Each model family has different assumptions about the data: Naive Bayes 
    assumes feature independence, Decision Trees learn hierarchical rules through recursive 
    splitting, and Logistic Regression assumes linear relationships between features and 
    log-odds. By comparing all seven models, we can determine which approach best captures 
    the patterns in disaster-climate data and draw meaningful conclusions about the predictability 
    of wildfire severity from geographic and meteorological features.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Grand Comparison Chart
    # ----------------------------
    st.subheader("📊 All Models — Accuracy Comparison")
 
    st.image("images/all_models_comparison.png",
             caption="Complete Accuracy Comparison Across All Seven Models",
             use_container_width=True)
 
    st.markdown("""
    | Rank | Model                          | Family              | Accuracy |
    |------|--------------------------------|---------------------|----------|
    | 1    | Logistic Regression            | Logistic Regression | 97.8%    |
    | 2    | Gaussian NB                    | Naive Bayes         | 88.9%    |
    | 3    | Bernoulli NB                   | Naive Bayes         | 77.8%    |
    | 4    | Multinomial NB                 | Naive Bayes         | 75.6%    |
    | 5    | Decision Tree 1 (Gini, d=4)    | Decision Tree       | 71.1%    |
    | 6    | Decision Tree 2 (Entropy, d=5) | Decision Tree       | 66.7%    |
    | 7    | Decision Tree 3 (Gini, d=3)    | Decision Tree       | 64.4%    |
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Analysis by Family
    # ----------------------------
    st.subheader("📋 Analysis by Model Family")
 
    col1, col2, col3 = st.columns(3)
 
    with col1:
        st.info("""
        **🔵 Naive Bayes Family**
        
        Accuracy range: **75.6% — 88.9%**
 
        Gaussian NB was the clear winner within the NB family, benefiting from the assumption 
        that continuous features follow normal distributions. Bernoulli NB performed second 
        best at 77.8% despite losing information through binarization. Multinomial NB came 
        last at 75.6% because it is designed for count data, not continuous climate measurements. 
        All three NB models perfectly classified Low Severity events, indicating this class 
        has the most distinctive geographic signature. The NB family's strength lies in its 
        computational efficiency and ability to work well with limited training data.
        """)
 
    with col2:
        st.info("""
        **🟣 Decision Tree Family**
        
        Accuracy range: **64.4% — 71.1%**
 
        Decision Trees produced the lowest accuracies overall, with Tree 1 (Gini, depth=4) 
        performing best at 71.1%. Interestingly, the deepest tree (depth=5) did not perform 
        the best, demonstrating overfitting on the 105-sample training set. All three trees 
        selected latitude as the root node, confirming its importance. The trees' main value 
        is interpretability — they provide clear visual rules for how predictions are made. 
        However, the small dataset size limits their ability to learn robust splitting rules 
        that generalize well to unseen data.
        """)
 
    with col3:
        st.info("""
        **🔴 Logistic Regression**
        
        Accuracy: **97.8%**
 
        Logistic Regression dramatically outperformed all other models, achieving near-perfect 
        classification with only one error out of 45 test samples. Its success indicates that 
        the relationship between geographic/precipitation features and severity labels is 
        approximately linear in the feature space. The multinomial strategy with Softmax 
        effectively modeled all three classes simultaneously. StandardScaler normalization 
        ensured optimal coefficient estimation. Logistic Regression's combination of high 
        accuracy, probabilistic outputs, and interpretable coefficients makes it the ideal 
        model for this wildfire severity prediction task.
        """)
 
    st.markdown("---")
 
    # ----------------------------
    # Which Model Works Best
    # ----------------------------
    st.subheader("🏆 Which Model Works Best for This Project?")
 
    st.success("""
    **🥇 Winner: Logistic Regression — 97.8% Accuracy**
 
    Logistic Regression is the clear winner for wildfire severity prediction in this project, 
    and the reasons go beyond just having the highest accuracy number. First, its 97.8% accuracy 
    means it made only **one mistake** out of 45 test predictions, a level of performance that 
    is practically usable for real-world applications. Second, unlike Decision Trees which 
    create rigid threshold-based rules, Logistic Regression produces **smooth probability 
    estimates** that can be used for risk scoring — a fire event predicted as "High Severity 
    with 92% confidence" provides more actionable information than a simple label. Third, the 
    model is **computationally efficient** — it trains in milliseconds and predicts instantly, 
    making it suitable for real-time severity assessment during active wildfire events. Fourth, 
    its coefficients are **directly interpretable** — positive coefficients for latitude mean 
    that fires at higher latitudes tend to be classified differently than those near the equator. 
    Fifth, the model's success confirms that the **geographic and seasonal features** chosen for 
    this analysis are genuinely informative predictors of wildfire severity, validating the 
    entire data science pipeline from data collection through feature engineering to modeling.
    """)
 
    st.markdown("---")
 
    # ----------------------------
    # Key Takeaways
    # ----------------------------
    st.subheader("🧠 Key Takeaways from Model Comparison")
 
    st.info("""
    **1. Model choice matters significantly.** Accuracy ranged from 64.4% (worst Decision Tree) 
    to 97.8% (Logistic Regression) — a 33.4 percentage point spread. Choosing the wrong model 
    for your data can cost you a third of your predictive performance.
 
    **2. Simpler assumptions can outperform complex structures.** Logistic Regression's simple 
    linear boundaries beat Decision Trees' complex hierarchical rules because the underlying 
    data relationships happen to be approximately linear.
 
    **3. Feature preprocessing impacts results.** The same features produced different accuracies 
    depending on how they were scaled (StandardScaler vs MinMaxScaler vs binarization), showing 
    that data preparation is as important as model selection.
 
    **4. Geographic features dominate.** Across all models, latitude and longitude were the most 
    important predictors, confirming that where a wildfire occurs is the strongest indicator 
    of its severity.
 
    **5. More complexity doesn't mean better performance.** The deepest Decision Tree (depth=5) 
    performed worse than the moderate one (depth=4), and the simplest probabilistic model 
    (Logistic Regression) outperformed everything else.
 
    **6. All models agree on easy cases.** Low Severity events were consistently well-classified 
    across all seven models, suggesting these events have the most distinctive and separable 
    feature profiles in the dataset.
 
    **7. Moderate Severity is the hardest class.** Every model struggled most with Moderate 
    Severity, which sits between the two extremes and shares feature characteristics with both 
    neighboring classes.
    """)


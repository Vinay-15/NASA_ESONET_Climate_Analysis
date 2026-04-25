# 🌍 NASA EONET Climate Analysis: Predicting Wildfire Severity from Climate Patterns

> **Disasters by the Numbers** — A complete data science pipeline that integrates real-time NASA disaster tracking with global climate data to understand, classify, and predict wildfire severity using machine learning.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-yellow.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

Website Link : https://nasa-esonet-climate-analysis.streamlit.app

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Motivation](#-motivation)
- [Data Sources](#-data-sources)
- [Methodology](#-methodology)
- [Models Implemented](#-models-implemented)
- [Key Results](#-key-results)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Streamlit Website](#-streamlit-website)
- [Tech Stack](#-tech-stack)
- [Future Work](#-future-work)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Project Overview

This project investigates whether **climate and geographic variables can predict the severity of natural disasters** — with a focus on wildfires. By combining real-time disaster events from **NASA EONET** with daily climate observations from **NASA POWER**, the project builds a complete data science pipeline that spans data collection, exploratory analysis, dimensionality reduction, clustering, association rule mining, and supervised classification across seven different machine learning algorithms.

The final deliverable is an **interactive Streamlit dashboard** that walks through every stage of the analysis — from raw data to predictive models — providing an accessible, story-driven presentation of the findings for both technical and non-technical audiences.

### What this project answers

- Do certain disaster types occur under specific climate conditions?
- Can climate variables be used to cluster and classify disaster events?
- Which features are most predictive of wildfire severity?
- How do simple linear models compare to complex ensembles on real-world climate data?

---

## 💡 Motivation

Natural disasters — wildfires, storms, floods, volcanic activity — are intensifying as climate patterns shift. The relationship between **local climate conditions** (temperature, humidity, wind, precipitation) and **disaster outcomes** is well known qualitatively, but quantitative, data-driven analysis at scale remains underutilized for early warning and resource planning.

This project bridges that gap by demonstrating that **publicly available NASA data combined with modern machine learning** can produce meaningful, accurate predictions of disaster severity using only a handful of geographic and climate features. The work is intended both as an academic exercise in the full data science lifecycle and as a proof-of-concept for how open data and accessible ML tools can support climate-aware decision-making.

---

## 🛰️ Data Sources

### 1. NASA EONET (Earth Observatory Natural Event Tracker)
**Endpoint:** `https://eonet.gsfc.nasa.gov/api/v3/events`

Provides near real-time information on global natural events:
- Event category (Wildfire, Storm, Flood, Volcano, Sea/Lake Ice, etc.)
- Event date and geographic coordinates
- Event title and source links

### 2. NASA POWER (Prediction Of Worldwide Energy Resources)
**Endpoint:** `https://power.larc.nasa.gov/api/temporal/daily/point`

Provides daily meteorological observations matched to each event location:
- **T2M** — Temperature at 2 meters (°C)
- **RH2M** — Relative humidity at 2 meters (%)
- **WS2M** — Wind speed at 2 meters (m/s)
- **PRECTOTCORR** — Precipitation (mm/day)

### Final Combined Dataset
- **150 disaster events** with same-day climate measurements
- Features: temperature, humidity, wind, precipitation, latitude, longitude, month
- Engineered target: wildfire severity (Low / Moderate / High) — 50 samples per class

---

## 🔬 Methodology

The project follows a complete data science lifecycle, with each stage informing the next:

### 1. Data Collection & Cleaning
- Pulled disaster events from NASA EONET API
- Matched each event with same-day climate data from NASA POWER
- Removed events with missing or invalid measurements
- Standardized date formats and merged into a unified dataset

### 2. Exploratory Data Analysis (EDA)
- Distribution analysis of temperature, humidity, wind, precipitation
- Disaster category breakdown and seasonal patterns
- Correlation heatmaps between climate variables
- Box plots and violin plots showing climate variation by disaster type

### 3. Dimensionality Reduction (PCA)
- StandardScaler normalization of all numeric features
- Principal Component Analysis with 2D and 3D projections
- Variance retention analysis: 2 components capture **85.15%**, 3 components capture **94.03%**
- Eigenvalue inspection and scree plots

### 4. Unsupervised Learning (Clustering)
- **K-Means** clustering with K = 3, 4, 5 (silhouette method to choose K)
- **Hierarchical clustering** with Ward's linkage and dendrogram visualization
- **DBSCAN** for density-based clustering and outlier detection

### 5. Association Rule Mining (ARM)
- Categorical binning of climate variables (Low / Medium / High)
- Apriori algorithm via `mlxtend` for frequent itemset mining
- Top rules ranked by support, confidence, and lift
- Network visualization of strongest associations

### 6. Feature Engineering for Supervised Learning
Because the dataset is dominated by wildfires (149 of 150 events), a direct multi-class category prediction was not meaningful. Instead, a **composite fire risk score** was engineered:

```
risk_score = temperature × 0.4 + (100 − humidity) × 0.35 + wind × 0.25
```

This score was binned via quantile partitioning into three balanced classes: **Low**, **Moderate**, and **High Severity** (50 samples each).

**Crucially**, the features used for prediction (latitude, longitude, month, precipitation) are **independent of the variables used to construct the label** — preventing data leakage.

### 7. Supervised Learning
A 70/30 stratified train/test split (105/45) was used consistently across all models for fair comparison.

---

## 🤖 Models Implemented

The project implements and compares **seven supervised classifiers across four major algorithm families**, plus three ensemble methods:

| Family | Model | Description |
|--------|-------|-------------|
| **Naive Bayes** | Multinomial NB | For count/scaled data |
| | Gaussian NB | For continuous features |
| | Bernoulli NB | For binarized features |
| **Decision Trees** | Tree 1 (Gini, depth=4) | Best single tree |
| | Tree 2 (Entropy, depth=5) | Demonstrates overfitting |
| | Tree 3 (Gini, depth=3) | Most generalizable |
| **Logistic Regression** | Multinomial (Softmax) | Best overall model |
| **SVMs** | Linear, Polynomial (d=2), RBF | All cost values 0.01–100 tested |
| **Ensemble Methods** | Random Forest (200 trees) | Bagging |
| | AdaBoost (100 learners) | Boosting |
| | Voting Classifier (SVM + DT + LR) | Soft voting |

---

## 🏆 Key Results

### Final Model Accuracy Ranking

| Rank | Model | Accuracy | Notes |
|------|-------|----------|-------|
| 🥇 1 | **Logistic Regression** | **97.8%** | 44/45 correct — near-perfect |
| 🥈 2 | Gaussian NB | 88.9% | Best probabilistic model |
| 🥉 3 | Bernoulli NB | 77.8% | Despite info loss from binarization |
| 4 | Multinomial NB | 75.6% | Designed for count data |
| 5 | Decision Tree (Gini, d=4) | 71.1% | Most interpretable |
| 6 | Decision Tree (Entropy, d=5) | 66.7% | Overfit |
| 7 | Decision Tree (Gini, d=3) | 64.4% | Most robust but underfit |

### Major Findings

1. **Geographic location dominates prediction.** Across every model and feature-importance method, **latitude and longitude account for over 80%** of predictive power. Where a wildfire occurs is the single most powerful indicator of how severe it will be.

2. **Simple beats complex.** Logistic Regression — one of the oldest and simplest classifiers — outperformed every Decision Tree, Naive Bayes variant, SVM kernel, and ensemble method tested. When the underlying relationship is approximately linear, sophisticated models offer no advantage.

3. **PCA reveals strong dimensionality compression.** Just 2 principal components retain over 85% of dataset variance, indicating that the 7 original variables share substantial redundant information.

4. **Clustering finds meaningful disaster groupings** based on climate alone — separating hot/dry (wildfire-prone), high-moisture (storm/flood-prone), and cold/extreme regimes.

5. **Ensemble methods provide robustness** but do not significantly beat the best single model (Logistic Regression) on this dataset, demonstrating that ensembles' real value is in stability and noise tolerance rather than raw accuracy.

---

## 📁 Project Structure

```
NASA_ESONET_Climate_Analysis/
│
├── NASA_climate_analysis.ipynb    # Main Jupyter notebook (full pipeline)
├── app.py                          # Streamlit dashboard
├── README.md                       # This file
├── requirements.txt                # Python dependencies
│
├── data/                           # Raw and cleaned datasets
│   ├── eonet_events.csv
│   ├── power_climate.csv
│   └── combined_df.csv
│
├── images/                         # Generated visualizations for the website
│   ├── EONET.png
│   ├── NASAPwer.png
│   ├── cleandata.png
│   ├── pca_2d.png, pca_3d.png, pca_variance.png
│   ├── kmeans_345.png, dendrogram.png, dbscan.png
│   ├── support_vs_confidence.png, arm_network.png
│   ├── cm_multinomial_nb.png, cm_gaussian_nb.png, cm_bernoulli_nb.png
│   ├── dt1_tree.png, dt2_tree.png, dt3_tree.png
│   ├── dt1_cm.png, dt2_cm.png, dt3_cm.png
│   ├── dt_feature_importance.png, dt_comparison.png
│   ├── lr_multiclass_cm.png, lr_binary_comparison.png
│   ├── all_models_comparison.png
│   ├── svm_cm_linear.png, svm_cm_poly.png, svm_cm_rbf.png
│   ├── svm_comparison.png, svm_boundaries_2d.png
│   ├── ensemble_cm_rf.png, ensemble_cm_ada.png, ensemble_cm_voting.png
│   ├── ensemble_feature_importance.png, ensemble_vs_all.png
│   └── vinay.jpg
│
└── notebooks/                      # Optional: split notebooks per module
    ├── 01_data_collection.ipynb
    ├── 02_eda.ipynb
    ├── 03_pca_clustering_arm.ipynb
    └── 04_supervised_models.ipynb
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.10 or higher
- pip or conda

### Setup

```bash
# Clone the repository
git clone https://github.com/Vinay-15/NASA_ESONET_Climate_Analysis.git
cd NASA_ESONET_Climate_Analysis

# (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate          # macOS/Linux
# venv\Scripts\activate            # Windows

# Install dependencies
pip install -r requirements.txt
```

### Required Packages

```
streamlit>=1.28
scikit-learn>=1.3
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
mlxtend>=0.22
scipy>=1.11
jupyter>=1.0
nbformat>=5.9
requests>=2.31
```

---

## 🚀 Usage

### Run the Jupyter Notebook

The notebook contains the **complete analysis pipeline** — data loading, EDA, PCA, clustering, ARM, and all supervised models including SVMs and ensembles.

```bash
jupyter notebook NASA_climate_analysis.ipynb
```

Run cells **in order from top to bottom**. Each section produces visualizations that are saved into the `images/` folder, which the Streamlit dashboard then reads.

> 💡 **Tip:** If you encounter errors after editing cells, re-run cells in strict order. Stale in-memory variables from earlier runs can persist and cause confusing failures.

### Launch the Streamlit Dashboard

After the notebook has generated all images, launch the interactive website:

```bash
streamlit run app.py
```

Open the URL shown (typically `http://localhost:8501`) in your browser.

---

## 🌐 Streamlit Website

The dashboard is organized into **15 tabs**, walking through the project from introduction to conclusions:

| # | Tab | Content |
|---|-----|---------|
| 1 | **Introduction** | Project overview, objectives, research questions |
| 2 | **Data Collection** | NASA EONET + POWER API documentation, cleaning steps |
| 3 | **Exploratory Analysis** | Distributions, correlations, climate-by-category plots |
| 4 | **PCA Analysis** | 2D/3D projections, variance retention, eigenvalue analysis |
| 5 | **Clustering Analysis** | K-Means, Hierarchical, DBSCAN with comparisons |
| 6 | **ARM Analysis** | Frequent itemsets, top rules, association network |
| 7 | **Naive Bayes** | All 3 NB flavors with confusion matrices and comparison |
| 8 | **Decision Tree** | 3 trees with Gini/Entropy, depths, and visualizations |
| 9 | **Regression** | Multi-class & binary logistic regression vs MNB |
| 10 | **Models** | Cross-family comparison of all 7 supervised models |
| 11 | **SVM** | Linear/Poly/RBF kernels with kernel trick explanation |
| 12 | **Ensemble Learning** | Random Forest + AdaBoost + Voting Classifier |
| 13 | **Results & Discussion** | Synthesis of findings, research question answers |
| 14 | **Conclusion** | Non-technical narrative of the project's takeaways |
| 15 | **About Me** | Author bio, skills, research interests, contact |

---

## 🛠️ Tech Stack

**Languages & Frameworks**
- Python 3.10+
- Jupyter Notebook
- Streamlit (interactive dashboard)

**Data Science Libraries**
- Pandas, NumPy (data manipulation)
- Matplotlib, Seaborn (visualization)
- Scikit-Learn (ML models)
- mlxtend (Apriori / association rules)
- SciPy (hierarchical clustering)

**APIs**
- NASA EONET (`https://eonet.gsfc.nasa.gov/api/v3/events`)
- NASA POWER (`https://power.larc.nasa.gov/api/temporal/daily/point`)

**Version Control & Deployment**
- Git / GitHub
- Streamlit Cloud (optional deployment)

---

## 🚀 Future Work

While this project provides a solid foundation, several extensions could strengthen and expand the analysis:

- **Larger dataset** — collect events over longer time windows and across more disaster categories (floods, storms, earthquakes) for true multi-category classification
- **Additional features** — incorporate vegetation index (NDVI), elevation, soil moisture, population density, and proximity to water bodies
- **Advanced ensembles** — Gradient Boosting (XGBoost, LightGBM) and stacking
- **Time-series modeling** — capture how climate evolves in the days/weeks before a disaster
- **Real-time prediction dashboard** — ingest live NASA EONET + POWER feeds for ongoing severity prediction
- **Regional risk maps** — geographic visualizations of fire risk by season
- **Cross-validation** — bootstrapping and k-fold CV for robust accuracy estimates with confidence intervals

---

## 👩‍💻 Author

**Vinay**
Data Science & Machine Learning Student

- 💻 **GitHub:** [github.com/Vinay-15](https://github.com/Vinay-15)
- 💼 **LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/vinaychandra15)

### Research Interests
Applied machine learning for real-world decision support — climate analytics, disaster risk prediction, and deployment of AI systems in production environments (including on-premises LLM serving).

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **NASA EONET** for providing open access to global natural event data
- **NASA POWER** for free, high-quality climate measurements worldwide
- **Scikit-Learn** maintainers for the most accessible ML library in Python
- The open-source data science community

---

## 📚 References

- NASA EONET API Documentation: https://eonet.gsfc.nasa.gov/docs/v3
- NASA POWER API Documentation: https://power.larc.nasa.gov/docs/services/api/
- Scikit-Learn: https://scikit-learn.org/stable/
- Streamlit: https://docs.streamlit.io/

---

⭐ **If you found this project useful, please consider giving it a star on GitHub!** ⭐

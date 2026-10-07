# AI-Based Synthetic Liver Scaffold Optimization

> **Machine learning for analyzing and predicting hepatic cell responses to synthetic 3D liver scaffolds**

## 📌 Project Overview

This project develops a machine learning framework for analyzing synthetic 3D liver scaffolds using literature-derived experimental data. The goal is to reduce the traditional trial-and-error approach in scaffold development by identifying relationships between scaffold properties and hepatic cellular responses.

The project integrates scaffold composition, structural and physicochemical properties, fabrication information, and biological response data to discover patterns and support ML-guided scaffold design.

## 🎯 Objectives

- Build a standardized dataset from published synthetic liver scaffold studies.
- Clean, preprocess, and standardize experimental data.
- Analyze relationships between scaffold properties and hepatic cellular responses.
- Apply PCA and clustering to identify scaffold patterns and groups.
- Develop machine learning models for predicting hepatic functional outcomes.
- Identify important scaffold properties using explainable ML.
- Generate promising scaffold designs for future experimental validation.

## 🔬 Research Problem

Synthetic liver scaffolds can differ in polymer composition, concentration, pore structure, porosity, swelling, stiffness, degradation, permeability, and other properties. Their effects on hepatic cell behavior are not always straightforward.

Researchers often rely on experimental trial and error to determine suitable scaffold conditions.

**This project asks:**

> Can machine learning identify combinations of scaffold properties associated with improved hepatic cellular function and use these relationships to support scaffold design?

## 📊 Dataset

The dataset is being constructed from quantitative information reported in published research papers.

### Main data categories

| Category                   | Example parameters                                                      |
| -------------------------- | ----------------------------------------------------------------------- |
| Scaffold composition       | Polymer, polymer ratio, polymer concentration, crosslinker              |
| Fabrication                | Fabrication method                                                      |
| Structure                  | Pore size, porosity                                                     |
| Physicochemical properties | Swelling, water uptake, stiffness, elastic modulus, compressive modulus |
| Material behavior          | Degradation, permeability                                               |
| Biological information     | Cell type, cell density, culture duration                               |
| Cellular response          | Viability, Albumin, Urea, CYP                                           |
| Metadata                   | Study ID, Scaffold ID, source, figure/table                             |

Each experimental scaffold condition is intended to be represented as a standardized observation where the reported information is available.

## 🧠 Machine Learning Workflow

```text
Published Research Papers
          ↓
Literature Data Extraction
          ↓
Dataset Construction
          ↓
Data Cleaning & Standardization
          ↓
Exploratory Data Analysis
          ↓
PCA & Clustering
          ↓
Feature Engineering
          ↓
Machine Learning Models
          ↓
Model Evaluation
          ↓
Explainable ML
          ↓
Candidate Scaffold Design
          ↓
Future Experimental Validation
```

## 📈 Exploratory Data Analysis

EDA will be used to understand:

- Missing values
- Feature distributions
- Relationships between scaffold properties
- Correlations between variables
- Differences between scaffold groups
- Relationships between scaffold properties and biological responses

Planned visualizations include:

- Histograms
- Box plots
- Scatter plots
- Correlation heatmaps
- Bar charts
- PCA plots
- Cluster visualizations

## 🔎 PCA and Clustering

Principal Component Analysis (PCA) will be used to reduce the dimensionality of the scaffold dataset and identify major patterns in the data.

Clustering will then be explored to determine whether scaffold conditions naturally form groups based on their composition and physicochemical characteristics.

## 🤖 Machine Learning Models

Candidate models include:

- Support Vector Regression (SVR)
- Random Forest
- XGBoost
- Linear/Ridge Regression where appropriate
- Classification models where the biological outcome is converted into categories

The final models will depend on dataset size, target availability, data quality, and whether the selected target is continuous or categorical.

## 🎯 Prediction Targets

Potential biological targets include:

- Hepatic cell viability
- Albumin secretion
- Urea production
- CYP activity

The final primary target will be selected after assessing data availability, sample size, measurement consistency, and comparability across studies.

## 📏 Model Evaluation

For regression tasks:

- MAE
- RMSE
- R²

For classification tasks:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Where multiple scaffold observations originate from the same study, study-level splitting or grouped validation will be considered to reduce data leakage.

## 🔍 Explainable Machine Learning

Model interpretation will be used to determine which scaffold properties contribute most strongly to predicted hepatic responses.

This can help answer questions such as:

- Which scaffold properties are most important?
- Does stiffness influence hepatic function?
- How do pore size and porosity relate to cellular response?
- Which combinations of properties appear promising?

The objective is not only to make predictions but also to obtain biologically interpretable insights from the data.

## 🧪 From Prediction to Experimental Validation

The computational framework is intended to support a future iterative workflow:

```text
Literature Data
      ↓
ML Model
      ↓
Important Scaffold Properties
      ↓
Candidate Scaffold Design
      ↓
Fabrication
      ↓
Hepatic Cell Testing
      ↓
Experimental Validation
      ↓
New Data
      ↓
Model Improvement
```

The current M.Tech work primarily focuses on the **computational and machine-learning framework**. Fabrication and biological validation are future/experimental components of the broader research workflow.

## 📁 Repository Structure

```text
AI-Liver-Scaffold-Optimization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_pca_clustering.ipynb
│   └── 04_ml_prediction.ipynb
│
├── src/
│   ├── preprocessing/
│   ├── features/
│   ├── models/
│   └── evaluation/
│
├── figures/
├── results/
├── literature/
├── requirements.txt
└── README.md
```

## 📚 Methodological Reference

A key methodological reference for this project is:

**Rafieyan et al. (2023), “MLATE: Machine learning for predicting cell behavior on cardiac tissue engineering scaffolds,” Computers in Biology and Medicine.**

The study demonstrates a workflow involving literature mining, dataset construction and standardization, exploratory analysis, machine learning, model comparison, and interpretation.

The present project adapts this general machine-learning workflow to the **synthetic liver scaffold** domain. The reference study focused on cardiac tissue-engineering scaffolds, so its results are not treated as direct evidence for liver scaffolds.

## ⚠️ Current Limitations

- Literature-derived datasets can contain missing values.
- Experimental measurements may use different units or protocols.
- Different studies may use different cell lines and culture conditions.
- Dataset size may be limited compared with conventional ML datasets.
- Biological outcomes may not be directly comparable across all studies.
- Experimental validation is required before treating ML predictions as confirmed scaffold designs.

## 🚀 Future Work

- Expand the literature-derived dataset.
- Improve data standardization and quality control.
- Compare additional ML algorithms.
- Optimize model hyperparameters.
- Apply explainable AI techniques.
- Identify promising combinations of scaffold properties.
- Collaborate with experimental researchers for scaffold fabrication and hepatic testing.
- Iteratively update the model using experimentally validated results.

## 👨‍💻 Project Type

**M.Tech Computer Science & Information Technology Research Project**

**Domain:** Machine Learning × Tissue Engineering × Synthetic Liver Scaffolds

**Status:** 🚧 Under Development

## 📌 Project Vision

> **From literature-derived experimental data to ML-guided synthetic liver scaffold design.**

The long-term vision is to develop a data-driven framework that can help researchers move from trial-and-error scaffold development toward systematic, evidence-based scaffold design.

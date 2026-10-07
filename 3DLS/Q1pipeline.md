
Can machine learning identify relationships between 3D liver-scaffold properties and healthy-like hepatic cellular function?




                 RESEARCH PAPERS
                       │
                       ▼
          ┌─────────────────────────┐
          │  Literature Collection  │
          │  10–30 liver scaffold   │
          │       studies           │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │   Data Extraction       │
          │                         │
          │ Scaffold properties     │
          │ • Polymer               │
          │ • Concentration         │
          │ • Pore size             │
          │ • Porosity              │
          │ • Swelling              │
          │ • Stiffness             │
          │ • Crosslinking          │
          │ • Fabrication           │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Hepatic Response Data   │
          │                         │
          │ • Viability             │
          │ • Albumin               │
          │ • Urea                  │
          │ • CYP3A4                │
          │ • CYP1A2 / CYP450       │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Data Standardization    │
          │                         │
          │ • Units                 │
          │ • Missing values        │
          │ • Ranges                │
          │ • Different assays      │
          │ • Cell types            │
          └────────────┬────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   EDA + PCA     │
              │                 │
              │ Relationships   │
              │ Correlations    │
              │ Patterns        │
              └────────┬────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Healthy-like Function  │
          │        Label           │
          │                         │
          │ Healthy-like            │
          │ vs                      │
          │ Disease/low-function   │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │      ML MODELS          │
          │                         │
          │ Logistic Regression     │
          │ Random Forest           │
          │ SVM                     │
          │ XGBoost                 │
          │                         │
          │ Regression models       │
          │ for ALB/Urea/CYP        │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Model Interpretation    │
          │                         │
          │ Which scaffold          │
          │ properties matter?     │
          │                         │
          │ SHAP / Feature         │
          │ Importance              │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Scaffold Optimization  │
          │                         │
          │ Predict combinations   │
          │ associated with        │
          │ healthy-like function  │
          └────────────┬────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ FINAL RESULT    │
              │                 │
              │ Scaffold        │
              │ properties →    │
              │ hepatic         │
              │ function        │
              └─────────────────┘



----------------------------------------------------------------------

report -
Yes. For your M.Tech project, I would structure the pipeline around the central research question:

> **Can machine learning identify relationships between 3D liver-scaffold properties and healthy-like hepatic cellular function?**

## 🧬 Overall Project Pipeline

```text
                 RESEARCH PAPERS
                       │
                       ▼
          ┌─────────────────────────┐
          │  Literature Collection  │
          │  10–30 liver scaffold   │
          │       studies           │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │   Data Extraction       │
          │                         │
          │ Scaffold properties     │
          │ • Polymer               │
          │ • Concentration         │
          │ • Pore size             │
          │ • Porosity              │
          │ • Swelling              │
          │ • Stiffness             │
          │ • Crosslinking          │
          │ • Fabrication           │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Hepatic Response Data   │
          │                         │
          │ • Viability             │
          │ • Albumin               │
          │ • Urea                  │
          │ • CYP3A4                │
          │ • CYP1A2 / CYP450       │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Data Standardization    │
          │                         │
          │ • Units                 │
          │ • Missing values        │
          │ • Ranges                │
          │ • Different assays      │
          │ • Cell types            │
          └────────────┬────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   EDA + PCA     │
              │                 │
              │ Relationships   │
              │ Correlations    │
              │ Patterns        │
              └────────┬────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Healthy-like Function  │
          │        Label           │
          │                         │
          │ Healthy-like            │
          │ vs                      │
          │ Disease/low-function   │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │      ML MODELS          │
          │                         │
          │ Logistic Regression     │
          │ Random Forest           │
          │ SVM                     │
          │ XGBoost                 │
          │                         │
          │ Regression models       │
          │ for ALB/Urea/CYP        │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Model Interpretation    │
          │                         │
          │ Which scaffold          │
          │ properties matter?     │
          │                         │
          │ SHAP / Feature         │
          │ Importance              │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │ Scaffold Optimization  │
          │                         │
          │ Predict combinations   │
          │ associated with        │
          │ healthy-like function  │
          └────────────┬────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ FINAL RESULT    │
              │                 │
              │ Scaffold        │
              │ properties →    │
              │ hepatic         │
              │ function        │
              └─────────────────┘
```

## 1. Literature collection

Start with approximately **10–30 primary research papers**.

Your inclusion criteria should be something like:

* 3D liver scaffold or 3D bioprinted liver model
* Quantitative scaffold/bioink information
* Hepatic cells
* At least one measurable hepatic-function outcome
* Experimental data available in tables/text/figures

Your current Lewis et al. paper is a good example because it contains quantitative fabrication information and hepatic-function measurements. 

---

## 2. Build the dataset

Think of the dataset as:

### Input — scaffold

```text
Polymer
Polymer concentration
Gelatin/GelMA concentration
ECM
Crosslinker
Crosslinking condition
Fabrication method
Pore size
Porosity
Swelling
Water uptake
Stiffness
```

### Experimental conditions

```text
Cell type
Cell density
Culture duration
```

### Output — hepatic function

```text
Viability
Albumin
Urea
CYP3A4
CYP1A2
CYP450
```

So mathematically:

$$
X = \text{Scaffold + experimental properties}
$$

and

$$
Y = \text{Hepatic function}
$$

---

# 3. Data cleaning and standardization

This will be one of the **most important parts of your project**.

For example, papers may report stiffness as:

```text
3.2 kPa
3.2 ± 0.4 kPa
2–5 kPa
3200 Pa
```

You need to standardize them to:

```text
Stiffness_kPa
```

Similarly:

```text
0.0032 MPa
```

becomes:

```text
3.2 kPa
```

But don't convert things that are not equivalent.

For example, in the Lewis paper:

> **700 μm is reported as strut spacing**, not necessarily pore diameter.

So your dataset should distinguish:

```text
Pore_size_um
Strut_spacing_um
```

rather than assuming they are the same. 

---

# 4. Exploratory Data Analysis

Before ML, understand your dataset.

### Questions:

**Does stiffness relate to hepatic function?**

```text
Stiffness
    ↓
Albumin
```

**Does porosity relate to viability?**

```text
Porosity
    ↓
Viability
```

**Does pore size relate to albumin?**

```text
Pore size
    ↓
Albumin
```

You can generate:

* Histograms
* Scatter plots
* Correlation matrix
* Box plots
* Pair plots

---

# 5. PCA

Use PCA to reduce multiple scaffold variables into major patterns.

For example:

```text
                 PCA
                  │
       ┌──────────┴──────────┐
       │                     │
   PC1                     PC2
       │                     │
stiffness             porosity
polymer                swelling
crosslinking           pore size
```

Then visualize the experimental conditions.

This helps answer:

> **Are there natural groups of scaffold designs?**

---

# 6. Clustering

After PCA, you can use:

* K-Means
* Hierarchical clustering

For example:

```text
Cluster 1
Soft + highly porous
        ↓
Higher hepatic function

Cluster 2
Stiffer + lower porosity
        ↓
Lower hepatic function
```

That would be a **data-derived pattern**, not something you assume beforehand.

---

# 7. Define your target

This is where your previous question about "healthy parameters" becomes important.

Don't define:

```text
Albumin > arbitrary value = healthy
```

Instead, construct the label from the experimental context and reported hepatic-function evidence.

For example:

```text
Healthy-like
       │
       ├── healthy hepatocyte model
       ├── maintained viability
       ├── albumin production
       ├── urea production
       └── hepatic CYP activity
```

versus:

```text
Disease-associated /
low-function
       │
       ├── fibrosis model
       ├── MASH/MASLD model
       ├── cirrhosis model
       └── reduced hepatic function
```

You should keep the **raw measurements** even after creating the label.

---

# 8. ML — Classification

Your first ML experiment can be:

$$
\text{Scaffold properties}
\rightarrow
\text{Healthy-like / non-healthy-like}
$$

Models:

### Model 1

Logistic Regression

### Model 2

Decision Tree

### Model 3

Random Forest

### Model 4

SVM

### Model 5

XGBoost

Compare:

```text
Accuracy
Precision
Recall
F1
ROC-AUC
```

But because multiple rows can come from the **same paper**, don't randomly split rows without considering study-level leakage.

Use something like:

```text
Paper 1 ─┐
Paper 2 ─┤
Paper 3 ─┤ → TRAIN
Paper 4 ─┘

Paper 5 ─┐
Paper 6 ─┘ → TEST
```

or **GroupKFold / Leave-One-Study-Out** validation.

---

# 9. ML — Regression

This is actually a very interesting second part of your project.

Instead of predicting only:

```text
Healthy / Not healthy
```

predict individual hepatic-function measurements.

### Model A

$$
Scaffold \ properties
\rightarrow Albumin
$$

### Model B

$$
Scaffold \ properties
\rightarrow Urea
$$

### Model C

$$
Scaffold \ properties
\rightarrow CYP3A4
$$

### Model D

$$
Scaffold \ properties
\rightarrow Viability
$$

Then you can say:

> **Which scaffold properties can predict quantitative hepatic function?**

This is stronger scientifically than only making a binary classifier.

---

# 10. Explain the ML model

After training Random Forest/XGBoost, use feature importance or SHAP.

Example:

```text
Feature importance

Stiffness          █████████████
Porosity           █████████
Polymer conc.      ███████
Pore size          ██████
Swelling           ████
Crosslinking       ███
```

Your question becomes:

> **Which scaffold properties contribute most to predicted hepatic function?**

---

# 11. Scaffold optimization

Finally:

```text
                  ML MODEL
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
   Stiffness      Porosity      Pore size
       │             │             │
       └─────────────┼─────────────┘
                     ↓
              Predicted function
                     ↓
             Albumin / Urea /
                CYP / Viability
```

You can then search for combinations associated with higher predicted function.

For example:

```text
Candidate scaffold
        ↓
GelMA = X%
Porosity = Y%
Stiffness = Z kPa
Pore size = W μm
        ↓
ML prediction
        ↓
Albumin = predicted value
Urea = predicted value
CYP = predicted value
```

**Important:** this is a computationally predicted candidate, not proof that the scaffold is biologically optimal. Experimental validation would be the next stage.

---

# 🎯 Your complete M.Tech methodology

I would present your methodology as these **8 phases**:

```text
PHASE 1
Literature Collection
       ↓
PHASE 2
Data Extraction
       ↓
PHASE 3
Data Cleaning & Standardization
       ↓
PHASE 4
EDA + PCA + Clustering
       ↓
PHASE 5
Healthy-like Function Labeling
       ↓
PHASE 6
ML Classification + Regression
       ↓
PHASE 7
Feature Interpretation
       ↓
PHASE 8
Scaffold Property Optimization
```

### The research story in one sentence

> **We collect quantitative data from published 3D liver-scaffold studies, standardize scaffold and hepatic-function parameters, use statistical and machine-learning methods to identify relationships between scaffold properties and hepatic function, and computationally identify scaffold-property combinations associated with healthy-like hepatic performance.**

That is the pipeline I would recommend you use for your **M.Tech project presentation, thesis methodology, and eventual ML implementation**.


import pandas as pd
import numpy as np

from sklearn.model_selection import LeaveOneGroupOut
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import clone
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ============================================================
# 1. LOAD DATA
# ============================================================

file_path = "3D_Liver_Scaffold_Stiffness_ML_Preprocessed.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="03_Preprocessed_ML_Filter"
)

print("Dataset shape:", df.shape)
print(df.head())


# ============================================================
# 2. SELECT DATA FOR ML
# ============================================================

# Keep rows having:
# - numerical stiffness
# - outcome code

data = df[
    df["Stiffness_ML_kPa"].notna() &
    df["Outcome_code"].notna()
].copy()

print("\nML dataset shape:", data.shape)


# ============================================================
# 3. CREATE TARGET VARIABLE
# ============================================================

# Outcome_code = 0 means Healthy
# Other codes = Non-healthy

data["Healthy_binary"] = (
    data["Outcome_code"] == 0
).astype(int)

print("\nTarget distribution:")
print(data["Healthy_binary"].value_counts())


# ============================================================
# 4. DEFINE X AND Y
# ============================================================

# X = scaffold stiffness
X = data[[
    "Stiffness_ML_kPa"
]]

# Y = healthy / non-healthy
y = data[
    "Healthy_binary"
]

# Paper ID is used for grouped validation
groups = data[
    "Paper_ID"
]


# ============================================================
# 5. DEFINE MODELS
# ============================================================

models = {

    "Logistic Regression": Pipeline([
        (
            "scaler",
            StandardScaler()
        ),

        (
            "model",
            LogisticRegression(
                max_iter=2000
            )
        )
    ]),

    "Random Forest": RandomForestClassifier(
        n_estimators=500,
        random_state=42,
        class_weight="balanced"
    )
}


# ============================================================
# 6. LEAVE-ONE-PAPER-OUT CROSS VALIDATION
# ============================================================

logo = LeaveOneGroupOut()

results = []


for model_name, model in models.items():

    y_true = []
    y_pred = []

    print("\n================================")
    print(model_name)
    print("================================")

    for train_index, test_index in logo.split(
        X,
        y,
        groups
    ):

        X_train = X.iloc[train_index]
        X_test = X.iloc[test_index]

        y_train = y.iloc[train_index]
        y_test = y.iloc[test_index]

        # Skip fold if training data contains
        # only one class
        if y_train.nunique() < 2:
            continue

        current_model = clone(model)

        current_model.fit(
            X_train,
            y_train
        )

        predictions = current_model.predict(
            X_test
        )

        y_true.extend(
            y_test.tolist()
        )

        y_pred.extend(
            predictions.tolist()
        )


    # ========================================================
    # 7. EVALUATION
    # ========================================================

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        zero_division=0
    )

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    print("\nAccuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")
    print(
        classification_report(
            y_true,
            y_pred,
            target_names=[
                "Non-healthy",
                "Healthy"
            ],
            zero_division=0
        )
    )

    results.append({

        "Model": model_name,

        "Accuracy": accuracy,

        "Precision": precision,

        "Recall": recall,

        "F1": f1
    })


# ============================================================
# 8. MODEL COMPARISON
# ============================================================

results_df = pd.DataFrame(
    results
)

print("\n\nMODEL COMPARISON")
print(
    results_df
)


# ============================================================
# 9. IDENTIFY HEALTHY STIFFNESS RANGE
# ============================================================

healthy_data = data[
    data["Healthy_binary"] == 1
]

healthy_stiffness = healthy_data[
    "Stiffness_ML_kPa"
]


print("\n================================")
print("HEALTHY STIFFNESS ANALYSIS")
print("================================")

print(
    "Minimum:",
    healthy_stiffness.min(),
    "kPa"
)

print(
    "Median:",
    healthy_stiffness.median(),
    "kPa"
)

print(
    "Mean:",
    healthy_stiffness.mean(),
    "kPa"
)

print(
    "Maximum:",
    healthy_stiffness.max(),
    "kPa"
)

print(
    "Number of observations:",
    len(healthy_stiffness)
)

print(
    "Number of papers:",
    healthy_data["Paper_ID"].nunique()
)


# ============================================================
# 10. SHOW HEALTHY SCAFFOLD DATA
# ============================================================

print("\nHealthy observations:")

print(
    healthy_data[
        [
            "Paper_ID",
            "First_author",
            "Year",
            "Stiffness_kPa",
            "Stiffness_ML_kPa",
            "Outcome_bank"
        ]
    ].sort_values(
        "Stiffness_ML_kPa"
    )
)
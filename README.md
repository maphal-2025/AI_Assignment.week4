# AI_Assignment.week4
# Breast Cancer Survival Prediction
ataset
The dataset includes medical and demographic records of breast cancer patients. It contains categorical and numerical features, including:
-Demographics: Age, Race, Marital Status
-Staging: T Stage, N Stage, A Stage, 6th Stage
-Tumor Attributes: Tumor Size, Grade, Differentiation
-Hormone Receptor Status: Estrogen & Progesterone
-Clinical Outcomes: Node exams, Survival Months, Vital Status
-The goal is to predict Status (Alive or Dead) based on these features.

# Data Preprocessing
-Cleaned categorical inconsistencies (e.g., whitespace and case)
-Encoded ordinal and nominal variables appropriately
-Normalized numerical features
-Handled class imbalance (if necessary)

# Exploratory Data Analysis (EDA)
-Assessed target class balance
-Visualized distributions and correlations
-Explored subgroup patterns by race, age group, and receptor status

# Models & Evaluation
-Trained multiple classifiers, including:
-Logistic Regression
-Random Forest
-Support Vector Machine (SVM)
-XGBoost
Evaluated models using:
Accuracy, Precision, Recall, F1-score
Confusion Matrix
ROC-AUC Curve

# Fairness & Ethics
Bias across sensitive attributes (e.g., Race, Marital Status) assessed using IBM AIF360. Mitigation strategies considered to enhance fairness in predictions.

# Key Findings
Features like Tumor Size, Node Positivity, and T/N Stage showed strong correlations with survival.
Class imbalance minimally affected model performance after stratified sampling.
Fairness interventions revealed disparities that could be reduced via preprocessing re-weighting.

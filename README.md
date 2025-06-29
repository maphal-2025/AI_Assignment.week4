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



# Part 3: Ethical Reflection.

# 1. Potential Biases in the Dataset
Even in a clinical dataset like Breast_Cancer.csv, several forms of bias can quietly creep in:
•	Demographic Imbalance: If certain groups (e.g., racial minorities or gender identities) are underrepresented, the model may perform poorly on them—leading to inequitable outcomes.
•	Labelling Subjectivity: Categories like 'Status' or 'A Stage' may reflect subjective clinical assessments, which vary by practitioner or institution, embedding inconsistent standards into the data.
•	Proxy Variables: Columns like 'Race' or 'Income Group' (if present) might act as proxies for systemic disparities, leading the model to inadvertently learn patterns of inequality rather than underlying clinical risk.

# 2. How IBM AI Fairness 360 Can Help
IBM AI Fairness 360 (AIF360) is designed to identify and mitigate such biases. Here's how it contributes to your workflow:
•	Bias Detection: Tools like Statistical Parity Difference and Disparate Impact assess whether predictions vary unfairly across groups (e.g., race, age). You can run these tests before and after model training to monitor fairness.
•	Preprocessing Remedies: Algorithms like Reweighing adjust the training data to reduce representational disparities, helping the model learn equitable patterns from the start.
•	In-Processing Mitigation: For more hands-on control, methods like Adversarial Debiasing integrate fairness constraints directly into the model’s learning process.
•	Postprocessing Techniques: If the model is already trained, techniques like Equalized Odds Postprocessing can tweak predictions to equalize false-positive/false-negative rates across groups.






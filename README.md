# Heart-Disease-Prediction-App-
This project is a machine learning-powered web application built with Streamlit that predicts the likelihood of heart disease based on user-provided health parameters. It provides an interactive interface where users can input medical attributes and receive real-time predictions.

## 🩺 Explanation of Input Columns

Age → The person’s age in years.

Gender (M/F) → Biological sex: M = Male, F = Female.

Chest Pain Type → Describes the kind of chest pain:
 
  **ATA (Atypical Angina) → Chest pain not typical of heart disease.
  NAP (Non-Anginal Pain) → Pain not related to the heart.
  TA (Typical Angina) → Classic chest pain linked to reduced blood flow.
  ASY (Asymptomatic) → No chest pain, but heart disease may still be present.**

Resting Blood Pressure (mmHg) → Blood pressure measured while at rest.

Cholesterol (mg/dL) → Amount of cholesterol in the blood. High values can indicate risk.

Fasting Blood Sugar (>120 mg/dL) → Whether fasting blood sugar is above 120 mg/dL:
  
  **1 = Yes (high)
  0 = No (normal)**

Resting ECG → Results of an electrocardiogram taken at rest:
  
  **Normal → No abnormalities.
  ST → ST-T wave abnormality (possible ischemia).
  LVH → Signs of left ventricular hypertrophy (thickened heart muscle).**

Max Heart Rate → The highest heart rate achieved during exercise.

Exercise-Induced Angina (Y/N) → Whether angina (chest pain) occurs during exercise.

Oldpeak (ST Depression) → Depression in the ST segment of an ECG during exercise, compared to rest. Higher values may indicate heart stress.

ST Slope → The slope of the ST segment during exercise:
  
  **Up → Upsloping (usually normal).
  Flat → Flat (possible abnormality).
  Down → Downsloping (often linked to heart disease).**


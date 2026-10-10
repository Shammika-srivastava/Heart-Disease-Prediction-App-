import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Naive_bayes.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")
st.title("Heart stroke prediction by MAHI")
st.markdown("Provide the following details")

age = st.slider("Age",10,100,40)
gender = st.selectbox("Gender",['M','F'])
chest_pain = st.selectbox("chest Pain type",["ATA","NAP","TA","ASY"])
resting_bp = st.number_input("Resting blood pressure(mmhg)",80,200,120)
cholestrol = st.number_input("cholestrol(mg/dL)",100,600,200)
fasting_bs = st.selectbox("fasting BP>120 mg/dL",[0,1])
resting_ecg = st.selectbox("Resting ECG",["Normal","ST","LVH"])
max_hr = st.slider("Max Heart Rate", 60,150,120)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y","N"])
oldpeak = st.slider("OldPeak(ST Depression)",0.0,6.0,1.0)
st_slope = st.selectbox("ST Slope",["Up","Flat","Down"])

if st.button("Predict"):
    raw_input = {
        'Age': age,
        'isFemale': 1 if gender == 'F' else 0,
        'RestingBP': resting_bp,
        'Cholesterol': cholestrol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'isExerciseAngina': 1 if exercise_angina == 'Y' else 0,
        'Oldpeak': oldpeak,

        'ST_Slope_Flat': 1 if st_slope == 'Flat' else 0,
        'ST_Slope_Up': 1 if st_slope == 'Up' else 0,

        'RestingECG_Normal': 1 if resting_ecg == 'Normal' else 0,
        'RestingECG_ST': 1 if resting_ecg == 'ST' else 0,

        'ChestPainType_ATA': 1 if chest_pain == 'ATA' else 0,
        'ChestPainType_NAP': 1 if chest_pain == 'NAP' else 0,
        'ChestPainType_TA': 1 if chest_pain == 'TA' else 0
    }

    input_df = pd.DataFrame([raw_input])
    input_df = input_df[expected_columns]
    
    numeric_cols = [
        'Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak'
    ]

    scaled_input = input_df.copy()

    scaled_input[numeric_cols] = scaler.transform(
        input_df[numeric_cols]
    )

    prediction = model.predict(scaled_input)[0]

    probability = model.predict_proba(scaled_input)[0][1]  # get probability of positive class
    
    # Show probability text
    st.write(f"Risk of Heart Disease: {probability*100:.2f}%")
    
    # Show progress bar
    st.progress(int(probability*100))
    
    # Show metric
    st.metric(label="Heart Disease Risk", value=f"{probability*100:.1f}%")



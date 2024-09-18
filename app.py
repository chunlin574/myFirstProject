import streamlit as st
import pandas as pd
import joblib

# 页面配置
st.set_page_config(page_title="CVEs Risk Prediction Tool", 
                  layout="wide",
                  initial_sidebar_state="expanded")

# 自定义样式
st.markdown("""
<style>
    .stButton>button {
        color: white;
        background-color: #079992;
        height: 50px;
        width: 150px;
        font-size: 18px;
    }
    .stNumberInput>div>div>input {
        height: 35px !important;
        font-size: 16px;
    }
    .stMarkdown {
        font-size: 20px;
        color: #4a4a4a;
        margin-bottom: 15px;
    }
    .stTextInput>div>div>input {
        height: 35px !important;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# 标题和副标题
st.markdown("<h1 style='text-align: center; color: #079992;'>CVEs Risk Prediction Tool for PD Patients</h1>", unsafe_allow_html=True)

# 两列布局
col1, col2 = st.columns(2)

# 第一列输入
with col1:
    Gender = st.number_input("Gender (1-Male, 2-Female)", min_value=1, max_value=2, step=1, format="%d")
    Height = st.number_input("Height (cm)", min_value=0, step=1)
    Marital_status = st.number_input("Marital Status (1-Unmarried, 2-Married, 3-Divorced)", min_value=1, max_value=4, step=1, format="%d")
    HDL = st.number_input("High-density lipoprotein,HDL (mmol/L)", min_value=0, step=1)
    PTH = st.number_input("Parathyroid Hormone, PTH (pg/ml)", min_value=0, step=1)
    PET = st.number_input(" Peritoneal Equilibration Test, PET (1-High transport, 2-High average transport, 3-Low average transport, 4-Low transport)", min_value=1, max_value=4, step=1, format="%d")
    Peritonitis = st.number_input("Peritonitis History (1-Yes, 0-No)", min_value=0, max_value=1, step=1, format="%d")

# 第二列输入
with col2:
    Age_at_catheterization = st.number_input("Age at Catheterization (Years)", min_value=0, step=1)
    SBP = st.number_input("Systolic Blood Pressure, SBP (mmHg)", min_value=0, step=1)
    Hemoglobin = st.number_input("Hemoglobin (g/L)", min_value=0.0, step=0.1)
    Triglyceride = st.number_input("Triglyceride (mg/dL)", min_value=0, step=1)
    Total_Ccr = st.number_input("Total Creatinine Clearance (ml/min)", min_value=0.0, step=0.1)

# 提交按钮美化
submit_button = st.button("Predict Risk", type="primary", use_container_width=True)

if submit_button:
    model = joblib.load("model_xgb.pkl")
    columns = ["Age_at_catheterization", "Gender", "Height", "Marital_status", "SBP", "Hemoglobin", "Triglyceride", "HDL", "PTH", "Total_Ccr", "PET", "Peritonitis"]
    X = pd.DataFrame([[Age_at_catheterization, Gender, Height, Marital_status, SBP, Hemoglobin, Triglyceride, HDL, PTH, Total_Ccr, PET, Peritonitis]], columns=columns)
    prediction = model.predict(X)[0]
    risk_labels = {0: "Low Risk", 1: "High Risk"}
    predicted_risk = risk_labels[prediction]
    
    st.success(f"Prediction Result: {predicted_risk}")

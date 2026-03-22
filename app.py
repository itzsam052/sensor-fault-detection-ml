import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Sensor Fault Detection System")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Original Data", data.head())

    #  Drop unwanted columns
    data = data.drop(columns=[ 'time', 'fault'], errors='ignore')

    #  Select required features
    features = ['signal', 'rolling_mean', 'rolling_std', 'diff','rolling_mean_long']


    if not all(col in data.columns for col in features):
        st.error("Dataset must contain: diff, rolling_mean,rolling_mean_long rolling_std, signal")
        st.stop()

    X = data[features]

    st.write("Processed Data", X.head())

    #  Prediction
    prediction = model.predict(X)

    # Add prediction to original dataset
    data['Prediction'] = prediction

    st.write("Final Output", data.head())

    # Download
    csv = data.to_csv(index=False)
    st.download_button("Download Results", csv, "predictions.csv", "text/csv")
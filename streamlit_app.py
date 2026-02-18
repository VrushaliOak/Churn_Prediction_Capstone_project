import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page Config
st.set_page_config(page_title="Capstone ML App", layout="centered")

# Title
st.title("Customer Churn Prediction App")
st.write("This app predicts whether a customer is likely to churn based on input features.")

@st.cache_resource
def load_model():
    model_path = "model.pkl"
    if not os.path.exists(model_path):
        return None
    try:
        return joblib.load(model_path)
    except Exception:
        return None

model = load_model()
if model is None:
    st.error("Model file 'model.pkl' not found or failed to load. Place the file in the app directory.")
    st.stop()
st.subheader("Enter Customer Details")

tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=50.0)

contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
input_data = pd.DataFrame({
    "tenure_months": [tenure],
    "monthly_charges": [monthly_charges],
    "total_charges": [total_charges],
    "contract_type": [contract_type]
})
# Build a full feature vector matching the training features expected by the model
def build_feature_vector(model, user_df):
    # get expected feature names from model
    try:
        expected = list(model.feature_names_in_)
    except Exception:
        return user_df

    # start with zeros
    row = {c: 0 for c in expected}

    # map direct numeric fields if present
    if "tenure_months" in expected:
        row["tenure_months"] = int(user_df.loc[0, "tenure_months"])
    # map monthly_charges -> arpu if model has arpu
    if "arpu" in expected:
        try:
            row["arpu"] = float(user_df.loc[0, "monthly_charges"])
        except Exception:
            row["arpu"] = 0.0

    # Attempt to set contract one-hot column based on selection
    contract_val = str(user_df.loc[0, "contract_type"]) if "contract_type" in user_df.columns else ""
    for col in expected:
        if col.startswith("contract_type_"):
            # normalize both strings for comparison
            key = col.replace("contract_type_", "").lower()
            if key in contract_val.lower() or contract_val.lower() in key:
                row[col] = 1

    # Ensure numeric types (no object dtype)
    out = pd.DataFrame([row])
    for c in out.columns:
        if out[c].dtype == object:
            try:
                out[c] = out[c].astype(float)
            except Exception:
                out[c] = out[c].astype('category')
    return out

# Convert user input to full feature set
input_data = build_feature_vector(model, input_data)
if st.button("Predict Churn"):
    try:
        prediction = model.predict(input_data)[0]
    except Exception as e:
        st.error(f"Prediction failed: {e}")
    else:
        probability = None
        if hasattr(model, "predict_proba"):
            try:
                probs = model.predict_proba(input_data)[0]
                probability = probs[1] if len(probs) > 1 else probs[0]
            except Exception:
                probability = None

        is_churn = False
        if isinstance(prediction, (int, np.integer)) and int(prediction) == 1:
            is_churn = True
        elif isinstance(prediction, (float, np.floating)) and prediction >= 0.5:
            is_churn = True
        elif isinstance(prediction, str) and prediction.lower() in ("yes", "churn", "true", "1", "y"):
            is_churn = True

        prob_text = f" (Probability: {probability:.2f})" if probability is not None else ""

        if is_churn:
            st.error(f"⚠️ Customer is likely to churn{prob_text}")
        else:
            st.success(f"✅ Customer is likely to stay{prob_text}")

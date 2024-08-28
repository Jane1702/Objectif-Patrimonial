import streamlit as st
import joblib
import pandas as pd

st.title('Patrimonial Objective Prediction')

model = joblib.load('Objectif Patrimonial.pkl')

features = [
    'Nombre enfants',
    'GP-Impôt sur le Revenu brut',
    'GP-Revenus professionnels foyer',
    'GP-Solde Flux',
    'GP-Patrimoine Professionnel',
    'GP-Passif cumulé',
    'GP-Patrimoine immobilier',
    'GP-Patrimoine financier',
    'GP-Solde actif&passif',
    'GP-Total actif brut',
    'Age'
]

data = {
    'Nombre enfants': st.number_input('Nombre enfants', min_value=0),
    'GP-Impôt sur le Revenu brut': st.number_input('GP-Impôt sur le Revenu brut', value=0.0),
    'GP-Revenus professionnels foyer': st.number_input('GP-Revenus professionnels foyer', value=0.0),
    'GP-Solde Flux': st.number_input('GP-Solde Flux', value=0.0),
    'GP-Patrimoine Professionnel': st.number_input('GP-Patrimoine Professionnel', value=0.0),
    'GP-Passif cumulé': st.number_input('GP-Passif cumulé', value=0.0),
    'GP-Patrimoine immobilier': st.number_input('GP-Patrimoine immobilier', value=0.0),
    'GP-Patrimoine financier': st.number_input('GP-Patrimoine financier', value=0.0),
    'GP-Solde actif&passif': st.number_input('GP-Solde actif&passif', value=0.0),
    'GP-Total actif brut': st.number_input('GP-Total actif brut', value=0.0),
    'Age': st.number_input('Age', min_value=0)
}

input_df = pd.DataFrame([data])
if st.button('Predict'):
    try:
        prediction = model.predict(input_df)[0]
        st.write(f'Predicted Patrimonial Objective: {prediction}')
    except Exception as e:
        st.error(f'Error during prediction: {e}')

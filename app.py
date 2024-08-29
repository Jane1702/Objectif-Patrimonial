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

with st.form(key='prediction_form'):
    cols = st.columns(3)
    
    data = {
        'Nombre enfants': cols[0].number_input('Nombre enfants', min_value=0, step=1),
        'GP-Impôt sur le Revenu brut': cols[1].number_input('GP-Impôt sur le Revenu brut', value=0.0, format='%f'),
        'GP-Revenus professionnels foyer': cols[2].number_input('GP-Revenus professionnels foyer', value=0.0, format='%f'),
        'GP-Solde Flux': cols[0].number_input('GP-Solde Flux', value=0.0, format='%f'),
        'GP-Patrimoine Professionnel': cols[1].number_input('GP-Patrimoine Professionnel', value=0.0, format='%f'),
        'GP-Passif cumulé': cols[2].number_input('GP-Passif cumulé', value=0.0, format='%f'),
        'GP-Patrimoine immobilier': cols[0].number_input('GP-Patrimoine immobilier', value=0.0, format='%f'),
        'GP-Patrimoine financier': cols[1].number_input('GP-Patrimoine financier', value=0.0, format='%f'),
        'GP-Solde actif&passif': cols[2].number_input('GP-Solde actif&passif', value=0.0, format='%f'),
        'GP-Total actif brut': cols[0].number_input('GP-Total actif brut', value=0.0, format='%f'),
        'Age': cols[1].number_input('Age', min_value=0, step=1)
    }

    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    input_df = pd.DataFrame([data])
    try:
        prediction = model.predict(input_df)[0]
        st.success(f'Predicted Patrimonial Objective: {prediction}')
    except Exception as e:
        st.error(f'Error during prediction: {e}')

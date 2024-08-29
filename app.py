import streamlit as st
import joblib
import pandas as pd



title_html = '<p style="font-family:sans-serif; color:#137a93; font-size: 42px; text-align:center;">Prédiction objective du patrimoine</p>'
st.markdown(title_html, unsafe_allow_html=True)
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

form_container_html = '''
<div style="background-color:#7be5ff; padding:20px; border-radius:10px; box-shadow:0px 0px 15px rgba(0, 0, 0, 0.2);">
'''
st.markdown(form_container_html, unsafe_allow_html=True)
with st.container():
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
st.markdown('</div>', unsafe_allow_html=True)

if submit_button:
    input_df = pd.DataFrame([data])
    try:
        prediction = model.predict(input_df)[0]
        st.success(f'Predicted Patrimonial Objective: {prediction}')
    except Exception as e:
        st.error(f'Error during prediction: {e}')



import streamlit as st
import joblib
import pandas as pd

logo_url = 'logo.png'  

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
columns_html = '''
<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1; background-color: #e0f7fa; padding: 10px; margin-right: 10px;">
        {col1}
    </div>
    <div style="flex: 1; background-color: #f1f8e9; padding: 10px; margin-right: 10px;">
        {col2}
    </div>
    <div style="flex: 1; background-color: #fbe9e7; padding: 10px;">
        {col3}
    </div>
</div>
'''
"""
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
"""
with st.form(key='prediction_form'):
    col1_html = st.empty()
    col2_html = st.empty()
    col3_html = st.empty()
    
    col1_html.markdown('''
    <div style="margin-bottom: 10px;">
        <label for="Nombre_enfants">Nombre enfants</label><br>
        <input type="number" id="Nombre_enfants" name="Nombre_enfants" min="0" step="1">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="GP-Solde_Flux">GP-Solde Flux</label><br>
        <input type="number" id="GP-Solde_Flux" name="GP-Solde_Flux" value="0.0">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="GP-Patrimoine_immobilier">GP-Patrimoine immobilier</label><br>
        <input type="number" id="GP-Patrimoine_immobilier" name="GP-Patrimoine_immobilier" value="0.0">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="GP-Total_actif_brut">GP-Total actif brut</label><br>
        <input type="number" id="GP-Total_actif_brut" name="GP-Total_actif_brut" value="0.0">
    </div>
    ''', unsafe_allow_html=True)

    col2_html.markdown('''
    <div style="margin-bottom: 10px;">
        <label for="GP-Impôt_sur_le_Revenu_brut">GP-Impôt sur le Revenu brut</label><br>
        <input type="number" id="GP-Impôt_sur_le_Revenu_brut" name="GP-Impôt_sur_le_Revenu_brut" value="0.0">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="GP-Patrimoine_Professionnel">GP-Patrimoine Professionnel</label><br>
        <input type="number" id="GP-Patrimoine_Professionnel" name="GP-Patrimoine_Professionnel" value="0.0">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="GP-Patrimoine_financier">GP-Patrimoine financier</label><br>
        <input type="number" id="GP-Patrimoine_financier" name="GP-Patrimoine_financier" value="0.0">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="Age">Age</label><br>
        <input type="number" id="Age" name="Age" min="0" step="1">
    </div>
    ''', unsafe_allow_html=True)

    col3_html.markdown('''
    <div style="margin-bottom: 10px;">
        <label for="GP-Passif_cumulé">GP-Passif cumulé</label><br>
        <input type="number" id="GP-Passif_cumulé" name="GP-Passif_cumulé" value="0.0">
    </div>
    <div style="margin-bottom: 10px;">
        <label for="GP-Solde_actif&passif">GP-Solde actif&passif</label><br>
        <input type="number" id="GP-Solde_actif&passif" name="GP-Solde_actif&passif" value="0.0">
    </div>
    ''', unsafe_allow_html=True)

    submit_button = st.form_submit_button(label='Predict')

# End custom HTML container
st.markdown('</div>', unsafe_allow_html=True)

# Handle form submission
if submit_button:
    # Create a dictionary with data (mocked for this example)
    data = {
        'Nombre enfants': st.session_state['Nombre_enfants'],
        'GP-Impôt sur le Revenu brut': st.session_state['GP-Impôt_sur_le_Revenu_brut'],
        'GP-Revenus professionnels foyer': st.session_state['GP-Revenus_professionnels_foyer'],
        'GP-Solde Flux': st.session_state['GP-Solde_Flux'],
        'GP-Patrimoine Professionnel': st.session_state['GP-Patrimoine_Professionnel'],
        'GP-Passif cumulé': st.session_state['GP-Passif_cumulé'],
        'GP-Patrimoine immobilier': st.session_state['GP-Patrimoine_immobilier'],
        'GP-Patrimoine financier': st.session_state['GP-Patrimoine_financier'],
        'GP-Solde actif&passif': st.session_state['GP-Solde_actif&passif'],
        'GP-Total actif brut': st.session_state['GP-Total_actif_brut'],
        'Age': st.session_state['Age']
    }

    input_df = pd.DataFrame([data])
    try:
        prediction = model.predict(input_df)[0]
        st.success(f'Predicted Patrimonial Objective: {prediction}')
    except Exception as e:
        st.error(f'Error during prediction: {e}')


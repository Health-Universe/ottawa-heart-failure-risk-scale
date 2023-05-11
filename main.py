import streamlit as st

def calculate_ohfrs(data):
    score = sum(data.values())
    return score

st.title('Ottawa Heart Failure Risk Scale Calculator')

st.header('Patient Information')
stroke_history = st.checkbox('History of stroke or TIA')
intubation_history = st.checkbox('History of intubation for respiratory distress')
heart_rate = st.checkbox('Heart rate > 110 bpm at disposition')
systolic_bp = st.checkbox('Systolic blood pressure < 115 mmHg at disposition')
saO2 = st.checkbox('SaO2 < 90% on room air at any point during visit')
creatinine = st.checkbox('Creatinine > 90 μmol/L (1.02 mg/dL) at disposition')
age = st.checkbox('Age > 65')
home_oxygen = st.checkbox('Currently on home oxygen therapy')
ambulance_arrival = st.checkbox('Arrival by ambulance')
no_ace_inhibitor = st.checkbox('No ACE inhibitor or ARB at presentation')

data = {
    'stroke_history': stroke_history,
    'intubation_history': intubation_history,
    'heart_rate': heart_rate,
    'systolic_bp': systolic_bp,
    'saO2': saO2,
    'creatinine': creatinine,
    'age': age,
    'home_oxygen': home_oxygen,
    'ambulance_arrival': ambulance_arrival,
    'no_ace_inhibitor': no_ace_inhibitor
}

if st.button('Calculate'):
    result = calculate_ohfrs(data)
    st.write('The Ottawa Heart Failure Risk Score is ', result)

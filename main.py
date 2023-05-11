import streamlit as st

def calculate_ohfrs(data):
    score = sum(data.values())
    return score

st.title('Ottawa Heart Failure Risk Scale Calculator')

st.sidebar.header('Patient Information')
stroke_history = st.sidebar.checkbox('History of stroke or TIA')
intubation_history = st.sidebar.checkbox('History of intubation for respiratory distress')
heart_rate = st.sidebar.checkbox('Heart rate > 110 bpm at disposition')
systolic_bp = st.sidebar.checkbox('Systolic blood pressure < 115 mmHg at disposition')
saO2 = st.sidebar.checkbox('SaO2 < 90% on room air at any point during visit')
creatinine = st.sidebar.checkbox('Creatinine > 90 μmol/L (1.02 mg/dL) at disposition')
age = st.sidebar.checkbox('Age > 65')
home_oxygen = st.sidebar.checkbox('Currently on home oxygen therapy')
ambulance_arrival = st.sidebar.checkbox('Arrival by ambulance')
no_ace_inhibitor = st.sidebar.checkbox('No ACE inhibitor or ARB at presentation')

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

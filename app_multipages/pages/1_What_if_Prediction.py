import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Obesity Prediction", page_icon="./img/BMI.png")
st.sidebar.header('What if Prediction')
st.title("Insurance prediction")

st.markdown("Predict medical insurance based on the following features:")

# -- Parameters -- #

age = st.number_input(label='Age', value=18, min_value=10, max_value=70)
gender = st.selectbox(label='Gender', options=['Male', 'Female'])
height = st.number_input(label='Height', value=1.70, min_value=1.30, max_value=2.10, step=0.01)
weight = st.number_input(label='Weight', value=70, min_value=25, max_value=200)
calc = st.selectbox(label='How often do you drink alcohol?', options=['Sometimes', 'no', 'Frequently', 'Always' ])
favc = st.selectbox(label='Do you eat high caloric food frequently?', options=['no','yes'])
fcvc = st.slider(label='Do you usually eat vegetables in your meals?', min_value=1.00, max_value=3.00, step=0.01 )
ncp = st.slider(label='How many main meals do you have daily?', min_value=1, max_value=4 )
scc = st.selectbox(label=' Do you monitor the calories you eat daily?', options=['no', 'yes'])
smoke = st.selectbox(label='Smoker?', options=['no','yes'])
ch2o = st.slider(label='How much water do you drink daily?', min_value=1.00, max_value=3.00, step=0.01 )
history = st.selectbox(label='Has a family member suffered or suffers from overweight?', options=['no','yes'])
faf = st.slider(label='How often do you have physical activity?', min_value=0.00, max_value=3.00, step=0.01 )
tue = st.slider(label='How much time do you use technological devices such as cell phone, videogames and others?', min_value=0.00, max_value=2.00, step=0.01 )
caec = st.selectbox(label='Do you eat any food between meals?', options=['Sometimes', 'no', 'Frequently', 'Always' ])
mtrans = st.selectbox(label='Which transportation do you usually use?', options=['Public_Transportation', 'Automobile', 'Walking', 'Motorbike', 'Bike',  ])

# -- Model -- #

with open('./models/model.pkl', 'rb') as file:
    model = pickle.load(file)

mapeamento_invertido = {
    1: 'Insufficient_Weight',
    2: 'Normal_Weight',
    3: 'Overweight_Level_I',
    4: 'Overweight_Level_II',
    5: 'Obesity_Type_I',
    6: 'Obesity_Type_II',
}

def prediction():
    df_input = pd.DataFrame([{'Age':age, 'Gender':gender, 'Height':height, 'Weight':weight, 'CALC':calc, 'FAVC':favc, 'FCVC':fcvc, 'NCP':ncp, 'SCC':scc, 'SMOKE':smoke,
    'CH2O':ch2o, 'family_history_with_overweight':history, 'FAF':faf, 'TUE':tue, 'CAEC':caec, 'MTRANS':mtrans}])
    prediction = model.predict(df_input)[0]
    return prediction

# Predict
if st.button('Predict'):
    try:
        obesity = prediction()
        st.success(f'**Obesity Type:** {mapeamento_invertido[obesity]}')
    except Exception as error:
        st.error(f"Couldn't predict the input data. The following error occurred: \n\n{error}")

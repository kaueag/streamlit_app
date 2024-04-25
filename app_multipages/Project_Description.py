import streamlit as st

st.set_page_config(
    page_title="Obesity Prediction",
    page_icon="./img/BMI.png",
)

st.sidebar.header('Project Description')

st.write("# Welcome to the Obesity Level (BMI) prediction")
st.write("\n\n")

st.image('./img/BMI.png')
st.write("\n\n")

st.markdown(
    """

   Obesity

Obesity, which causes physical and mental problems, is a global health problem with serious consequences. 
The prevalence of obesity is increasing steadily, and therefore, new research is needed that examines the influencing factors of obesity and how to predict the occurrence of the condition according to these factors.

These are the features:

- Gender: Male and Female
- Age: 14-61
- Height: 1.45 - 1.98 m
- Weight: 39-173 kg
- family_history_with_overweight: " Has a family member suffered or suffers from overweight? " - Yes or No

- FAVC: " Do you eat high caloric food frequently? " - Yes or No
- FCVC: " Do you usually eat vegetables in your meals? " - Between 1 and 3
- NCP:  " How many main meals do you have daily? " - Between 1 and 4
- CAEC: " Do you eat any food between meals? " 
- SMOKE: " Do you smoke? " - Yes or No
- CH2O: " How much water do you drink daily? " - Between 1 and 3
- SCC: " Do you monitor the calories you eat daily? " - Yes or No
- FAF: " How often do you have physical activity? " - Between 1 and 3
- TUE:  " How much time do you use technological devices such as cell phone, videogames, television, computer and others? " - Between 1 and 2

- CALC: " How often do you drink alcohol? "
- MTRANS: " Which transportation do you usually use? "
- NObeyesdad: Target, Categorical, "Obesity level" 
    """
)

st.success('Please **go to the next pages** to get the predictions.')

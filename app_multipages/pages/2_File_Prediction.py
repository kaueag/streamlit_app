import pickle
import pandas as pd
import streamlit as st

banner_image = "./img/BMI.png"
st.set_page_config(page_title="Obesity Prediction", page_icon="./img/BMI.png")
st.image(banner_image, use_column_width=True)
st.sidebar.header('File Prediction')
st.title("Obesity prediction")

st.markdown("Predict obesity level (BMI) using a csv file:")

# -- Model -- #
with open(r'C:\Users\vanes\Desktop\Kaue Aulas DNC\Kaggle - Obesidade\Pipelines\data\models\model.pkl', 'rb') as file:
    model = pickle.load(file)
def nomear_predict(valores):
    mapeamento_invertido = {
    1: 'Insufficient_Weight',
    2: 'Normal_Weight',
    3: 'Overweight_Level_I',
    4: 'Overweight_Level_II',
    5: 'Obesity_Type_I',
    6: 'Obesity_Type_II',
}
    return [mapeamento_invertido[pred] for pred in valores]

data = st.file_uploader('Upload your file')
if data:
    df_input = pd.read_csv(data)
    obesity_prediction = model.predict(df_input)
    obesity_prediction_cats = nomear_predict(obesity_prediction)
    df_output = df_input.assign(prediction=obesity_prediction_cats)

    st.markdown('Obesity prediction:')
    st.write(df_output)
    st.download_button(
        label='Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv', file_name='predicted_obesity.csv'
        )


<<<<<<< HEAD
import streamlit as st
import pandas as pd
from sklearn import neighbors
import matplotlib.pyplot as plt 
import joblib
# import pickle

# print(sklearn.__version__)

modelscorev2 = joblib.load('heart_failure_pred.pkl' , mmap_mode ='r')
# loaded_model = pickle.load(open('hybrid_knn.sav', 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)

st.header("Welcome to the experiment")

st.write("In this survey we want to determine your risk to heart disease given the data you will give us below")

def user_input():
        Diabetes_string = st.radio("Do you have a history of diabetes?" , ["Never had" , "Pre diabetic" , "Diabetic"])

        if Diabetes_string == "Never had":
            Diabetes = 0
        elif Diabetes_string == "Pre diabetic":
            Diabetes = 1
        elif Diabetes_string == "Diabetic":
            Diabetes = 2

        Smoker_string = st.radio("Are you a frequent smoker? Do you smoke everyday or every two days?" , ["No" , "Yes"])

        if Smoker_string == "No":
            Smoker = 0
        elif Smoker_string == "Yes":
            Smoker = 1

        Stroke_string = st.radio("Have you ever had a stroke?" , ["No" , "Yes"])

        if Stroke_string == "No":
            Stroke = 0
        elif Stroke_string == "Yes":
            Stroke = 1

        HighBP_string = st.radio("Do you have high blood pressure? higher than 140/90" , ["No" , "Yes" , "I have no idea"])

        if HighBP_string == "No":
            HighBP = 0
        elif HighBP_string == "Yes":
            HighBP = 1
        elif HighBP_string == "I have no idea" and Smoker_string == "Yes":
            HighBP = 0

        HighChol_string = st.radio("Do you have high cholesterol? A measurement above 200 mg/dl is regarded as high" , ["Yes" , "No" , "I have no idea"] )

        if HighChol_string == "No":
            HighChol = 0
        elif HighChol_string == "Yes":
            HighChol = 1
        elif HighChol_string == "I have no idea" and Smoker_string == "Yes" and HighBP_string == "Yes":
            HighChol = 1
        else:
            HighChol = 0

        CholCheck_string = st.radio("Do you have a regular cholesterol check? More than once in six months." , ["Yes" , "No"] )

        if CholCheck_string == "No":
            CholCheck = 0
        elif CholCheck_string == "Yes":
            CholCheck = 1

        st.write("This is calculated by dividing your body weight(kg) by your height(meters) squared")

        Bmi = st.slider("Slide to your BMI (Body Mass Index)" , 0 , 100)

        Age = st.slider("What is your age? Please slide to the appropriate answer." , 0 , 130)

        data = {'HighBp': HighBP,
            'HighChol': HighChol,
            'Cholcheck': CholCheck,
            'BMI': Bmi,
            'Smoker': Smoker,
            'Stroke': Stroke,
            'Diabetes': Diabetes,
            'Age': Age
            }
        features = pd.DataFrame(data, index=[0])
        return features

df = user_input()

st.subheader('User Input parameters')
st.write(df)

st.subheader("Results")

prediction = modelscorev2.predict_proba(df)

print(prediction)

st.write(prediction)

if prediction[0][0] > prediction[0][1]:
    pred = prediction[0][0] * 100
    pred = str(pred)
    st.write("The patient is likely to **NOT** be diagnosed with heart disease with a **" + pred + "%** probability")
elif prediction[0][0] < prediction[0][1]:
    pred = prediction[0][1] * 100
    pred = str(pred)
    st.write("The patient has a **HIGH** risk of being diagnosed with a **" + pred + "**% probabilty")
else:
    pred = prediction[0][0] * 100
    pred = str(pred)
=======
import streamlit as st
import pandas as pd
from sklearn import neighbors
import matplotlib.pyplot as plt 
import joblib
# import pickle

# print(sklearn.__version__)

modelscorev2 = joblib.load('knn_model2.pkl' , mmap_mode ='r')
# loaded_model = pickle.load(open('hybrid_knn.sav', 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)

st.header("Welcome to the experiment")

st.write("In this survey we want to determine your risk to heart disease given the data you will give us below")

def user_input():
        Diabetes_string = st.radio("Do you have a history of diabetes?" , ["Never had" , "Pre diabetic" , "Diabetic"])

        if Diabetes_string == "Never had":
            Diabetes = 0
        elif Diabetes_string == "Pre diabetic":
            Diabetes = 1
        elif Diabetes_string == "Diabetic":
            Diabetes = 2

        Smoker_string = st.radio("Are you a frequent smoker? Do you smoke everyday or every two days?" , ["No" , "Yes"])

        if Smoker_string == "No":
            Smoker = 0
        elif Smoker_string == "Yes":
            Smoker = 1

        Stroke_string = st.radio("Have you ever had a stroke?" , ["No" , "Yes"])

        if Stroke_string == "No":
            Stroke = 0
        elif Stroke_string == "Yes":
            Stroke = 1

        HighBP_string = st.radio("Do you have high blood pressure? higher than 140/90" , ["No" , "Yes" , "I have no idea"])

        if HighBP_string == "No":
            HighBP = 0
        elif HighBP_string == "Yes":
            HighBP = 1
        elif HighBP_string == "I have no idea" and Smoker_string == "Yes":
            HighBP = 0

        HighChol_string = st.radio("Do you have high cholesterol? A measurement above 200 mg/dl is regarded as high" , ["Yes" , "No" , "I have no idea"] )

        if HighChol_string == "No":
            HighChol = 0
        elif HighChol_string == "Yes":
            HighChol = 1
        elif HighChol_string == "I have no idea" and Smoker_string == "Yes" and HighBP_string == "Yes":
            HighChol = 1
        else:
            HighChol = 0

        CholCheck_string = st.radio("Do you have a regular cholesterol check? More than once in six months." , ["Yes" , "No"] )

        if CholCheck_string == "No":
            CholCheck = 0
        elif CholCheck_string == "Yes":
            CholCheck = 1

        st.write("This is calculated by dividing your body weight(kg) by your height(meters) squared")

        Bmi = st.slider("Slide to your BMI (Body Mass Index)" , 0 , 100)

        Age = st.slider("What is your age? Please slide to the appropriate answer." , 0 , 130)

        data = {'HighBp': HighBP,
            'HighChol': HighChol,
            'Cholcheck': CholCheck,
            'BMI': Bmi,
            'Smoker': Smoker,
            'Stroke': Stroke,
            'Diabetes': Diabetes,
            'Age': Age
            }
        features = pd.DataFrame(data, index=[0])
        return features

df = user_input()

st.subheader('User Input parameters')
st.write(df)

st.subheader("Results")

prediction = modelscorev2.predict_proba(df)

print(prediction)

st.write(prediction)

if prediction[0][0] > prediction[0][1]:
    pred = prediction[0][0] * 100
    pred = str(pred)
    st.write("The patient is likely to **NOT** be diagnosed with heart disease with a **" + pred + "%** probability")
elif prediction[0][0] < prediction[0][1]:
    pred = prediction[0][1] * 100
    pred = str(pred)
    st.write("The patient has a **HIGH** risk of being diagnosed with a **" + pred + "**% probabilty")
else:
    pred = prediction[0][0] * 100
    pred = str(pred)
>>>>>>> 8960190 (initial commit)
    st.write("The patient has a risk of being diagnosed with heart disease by a figure of " + pred + "%")
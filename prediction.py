import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder,PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st
df=pd.read_csv("insurance.csv")

print(df.columns)
X=df[["age","bmi","children"]]
Y=df["charges"]

features=df[["sex","smoker","region"]]
ohe=OneHotEncoder(sparse_output=False,drop="first")
encode_array=ohe.fit_transform(features)
get_col=ohe.get_feature_names_out(["sex","smoker","region"])
encode_df=pd.DataFrame(encode_array,columns=get_col)

X_final=pd.concat([X,encode_df],axis=1)
pe=PolynomialFeatures(degree=2)
pe.fit(X_final)
x_pe=pe.transform(X_final)
x_train,x_test,y_train,y_test=train_test_split(x_pe,Y,test_size=0.2,random_state=42)
le=LinearRegression()

le.fit(x_train,y_train)

acc=le.score(x_test,y_test)

st.title("🩺 Medical Insurance Cost Prediction App")
st.write("Model Accuracy: {:.2f}%".format(acc * 100))

# User Inputs
age = st.number_input("Enter Age", min_value=0, max_value=120, step=1)
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=60.0, step=0.1)
children = st.number_input("Enter Number of Children", min_value=0, max_value=10, step=1)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Insurance Charges"):
    try:
        encode_features=pd.DataFrame([[sex,smoker,region]],columns=["sex","smoker","region"])
        array=ohe.transform(encode_features)
        df_fet=pd.DataFrame(array,columns=get_col)
    
        normal_df=pd.DataFrame([[age,bmi,children]],columns=["age","bmi","children"])
    
        final_input=pd.concat([normal_df,df_fet],axis=1)
        input_pe=pe.transform(final_input)
        prediction=le.predict(input_pe)[0]
        st.success(f"💰 Predicted Insurance Charges: Rs {round(prediction, 2)}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

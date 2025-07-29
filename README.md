# 🩺 Medical Insurance Cost Prediction using Polynomial Regression

A simple yet impactful machine learning solution to predict medical insurance charges based on individual health and demographic information. This project is built using **Polynomial Regression** and includes a **Streamlit frontend** for easy user interaction.

---

## 💡 Problem Statement

In countries like **Pakistan**, medical treatment costs are rising and often unaffordable. Health insurance can help, but understanding and estimating insurance charges remains confusing for many individuals.

This project aims to:
- Predict **insurance charges** based on inputs like age, BMI, smoking habits, etc.
- Provide a **user-friendly interface** using Streamlit.
- Demonstrate the use of **Polynomial Regression** to handle non-linear relationships in data.

---

## 📁 Dataset

The dataset used is the [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) from Kaggle.

**Features:**
- `age`: Age of the person
- `sex`: Gender
- `bmi`: Body Mass Index
- `children`: Number of children
- `smoker`: Smoking status
- `region`: Residential region
- `charges`: Medical insurance cost (target variable)

---

## 🧠 Model: Polynomial Regression

Medical charges do not increase linearly with features like age or BMI. To capture these patterns, **Polynomial Regression** (degree=2) is used instead of simple linear regression.

### ✳️ Steps:
1. Encode categorical features (`sex`, `smoker`, `region`) using `OneHotEncoder`
2. Combine them with numerical features (`age`, `bmi`, `children`)
3. Apply `PolynomialFeatures` to expand feature space
4. Train a `LinearRegression` model on the transformed features

---

## 📊 Exploratory Data Analysis (EDA)

### 1. Age vs Charges
Shows that charges generally increase with age.
### 2. Smoker vs Non-Smoker
Smokers pay significantly higher insurance charges.
### 3. BMI vs Charges (Colored by Smoker)
Smoking and high BMI together increase charges.

## ⚙️ Technologies & Libraries Used
Python

Pandas – for data loading and preprocessing

Scikit-learn – for encoding, regression model, and transformation

Matplotlib & Seaborn – for data visualization

Streamlit – for building a web-based user interface

## 🖥️ Streamlit App
A clean and interactive app built with Streamlit allows users to:

Input their personal info (age, BMI, sex, smoking status, region)

Instantly get a predicted insurance charge

View model accuracy

## 🎯 App Features:
Real-time prediction

Model accuracy display

Simple UI for non-technical users

## 📈 Model Performance
Train/Test Split: 80/20

Model Used: LinearRegression on polynomial-transformed features

Model Accuracy: ~XX.XX% on test data (replace with actual score)

## 📂 Project Structure

insurance_prediction/
│
├── insurance.csv                # Dataset
├── app.py                       # Streamlit web app
├── model.py                     # Core ML model training
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
└── images/                      # Graphs and visuals for documentation
## 🧠 Key Learnings
Polynomial Regression can capture complex, non-linear trends in real-world data

Streamlit is a powerful tool to deploy ML models with minimal effort

Real-world problems like healthcare can be tackled using data science

### 📌 Streamlit App: https://medical-insurance-cost-prediction-7ftjcfsyqgsbz3jkkmlixm.streamlit.app/

## 🏁 Final Note
“Not every project needs to be complex to be impactful.”
This project reflects both technical skill and social value — helping bridge the gap between healthcare and machine learning.

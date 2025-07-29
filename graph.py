import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
df=pd.read_csv("insurance.csv")

# 1. Charges vs Smoking (Boxplot)
fig1, ax1 = plt.subplots()
sns.boxplot(x='smoker', y='charges', data=df, ax=ax1)
ax1.set_title("Insurance Charges vs Smoking Status")
ax1.set_xlabel("Smoker")
ax1.set_ylabel("Insurance Charges")
plt.savefig("insuranceVsmoking.png")
plt.show()

# 2. Charges vs BMI (Colored by Smoker)
fig2, ax2 = plt.subplots()
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df, ax=ax2)
ax2.set_title("BMI vs Insurance Charges (Colored by Smoker)")
ax2.set_xlabel("BMI")
ax2.set_ylabel("Insurance Charges")
plt.savefig("bmivsins.png")
plt.show()

# 3. Region-wise Average Charges (Bar Chart)
fig3, ax3 = plt.subplots()
region_avg = df.groupby("region")["charges"].mean()
region_avg.plot(kind="bar", color="skyblue", ax=ax3)
ax3.set_title("Average Insurance Charges by Region")
ax3.set_xlabel("Region")
ax3.set_ylabel("Average Charges")
plt.savefig("averageinsurancebyregion.png")
plt.show()

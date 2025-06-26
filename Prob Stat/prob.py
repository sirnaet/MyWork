import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Current working directory:", os.getcwd())

# Load Excel data
# df = pd.read_excel("DATA.xlsx", sheet_name="Sheet1")
df = pd.read_excel(r"C:\Users\memus\Sanaet\Personal\Prob Stat\DATA.xlsx", sheet_name="Sheet1") #Depends on the location saved

# Pearson correlation coefficient
correlation, _ = stats.pearsonr(df["Hours_Coding"], df["Num_Bugs"])
print("Pearson correlation coefficient (r):", correlation)

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df["Hours_Coding"], df["Num_Bugs"])
print(f"Regression equation: Num_Bugs = {intercept:.2f} + {slope:.2f} * Hours_Coding")

# Predict number of bugs for 20 hours
predicted_bugs = intercept + slope * 20
print("Predicted bugs for 20 hours of coding:", predicted_bugs)

# Frequency distribution table
freq_table = df["Num_Bugs"].value_counts().sort_index().reset_index()
freq_table.columns = ["Num_Bugs", "Frequency"]
print("\nFrequency Distribution Table:\n", freq_table)

# Histogram with normal curve overlay
mean_bugs = df["Num_Bugs"].mean()
std_bugs = df["Num_Bugs"].std()

# Plot histogram
plt.figure(figsize=(8,6))
sns.histplot(df["Num_Bugs"], bins=10, kde=False, stat="density", color="skyblue", edgecolor="black", label="Histogram")

# Normal distribution curve
x = np.linspace(df["Num_Bugs"].min(), df["Num_Bugs"].max(), 100)
plt.plot(x, stats.norm.pdf(x, mean_bugs, std_bugs), color="red", lw=2, label="Normal Curve")

plt.title("Histogram of Number of Bugs with Normal Curve")
plt.xlabel("Number of Bugs")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()

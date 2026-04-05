import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Day": np.arange(1, 11),
    "Sales": [200, 220, 250, 270, 300, 280, 260, 500, 290, 310]
}

df = pd.DataFrame(data)
print(df)

mean_sales = df["Sales"].mean()
median_sales = df["Sales"].median()
std_sales = df["Sales"].std()

print("Mean:", mean_sales)
print("Median:", median_sales)
print("Std Dev:", std_sales)

threshold = mean_sales + 2 * std_sales
outliers = df[df["Sales"] > threshold]

print("Outliers:\n", outliers)

df["Normalized"] = (df["Sales"] - mean_sales) / std_sales
print(df)


plt.figure()
plt.plot(df["Day"], df["Sales"])
plt.title("Daily Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

plt.figure()
plt.plot(df["Day"], df["Sales"])
plt.scatter(outliers["Day"], outliers["Sales"])
plt.title("Sales with Outliers Highlighted")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

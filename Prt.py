import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv(r"d:\Eng. Bro\Robotic\Iris.csv")
num = df

print(df.head())

print("Mean:", num.mean(numeric_only=True))
print("Variance:", num.var(numeric_only=True))
print("corr:", num.corr(numeric_only=True))
sns.scatterplot(data=df, x="SepalLengthCm", y="PetalLengthCm", hue="Species")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import openpyxl


df = pd.read_excel(r"D:\Eng. Bro\Robotic\Date_Fruit_Datasets.xlsx")
print(df.head())

area = df['AREA']

print("Area Mean:", np.mean(area))
print("Area Median:", np.median(area))
print("Area Standard Deviation:", np.std(area))
print("Area Variance:", np.var(area))
print("Area mode:", area.mode())


sns.histplot(area, bins=30)
plt.title('Histogram of Area')
plt.show()



import pandas as pd
df = pd.read_excel("Date_Fruit_Datasets.xlsx")

print(df.shape)
print(df.isnull().sum().sum())
print(df.duplicated().sum())


import numpy as np

df2 = df.copy()
df2.loc[0:4, "AREA"] = np.nan

print(df2.isnull().sum().sum())
print(df2["AREA"].head(7))

median_val = df2["AREA"].median()
print("median:", median_val)
df2["AREA"] = df2["AREA"].fillna(median_val)

print(df2.isnull().sum().sum())
print(df2["AREA"].head(7))


df3 = pd.concat([df, df.iloc[:3]], ignore_index=True)

print(df3.shape)
print(df3.duplicated().sum())

df3 = df3.drop_duplicates()

print(df3.shape)
print(df3.duplicated().sum())


import seaborn as sns
import matplotlib.pyplot as plt


sns.boxplot(x=df["AREA"])
plt.show()


Q1 = df["AREA"].quantile(0.25)
Q3 = df["AREA"].quantile(0.75)
IQR = Q3 - Q1

low = Q1 - 1.5 * IQR
high = Q3 + 1.5 * IQR

outliers = df[(df["AREA"] < low) | (df["AREA"] > high)]
print(len(outliers))



print(df["Class"].unique())
print(df["Class"].nunique())
df["Class_num"] = df["Class"].astype("category").cat.codes

print(df[["Class", "Class_num"]].head(3))
print(df.groupby("Class")["Class_num"].first())


cols = ["AREA", "ECCENTRICITY"]
print(df[cols].agg(["min", "max"]))

for c in cols:
    df[c + "_s"] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

print(df[["AREA_s", "ECCENTRICITY_s"]].agg(["min", "max"]))


import requests

url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()

api_df = pd.DataFrame(data)
print(api_df.shape)
print(api_df[["id", "name", "email"]].head(3))



df["AREA_PER_PERIMETER"] = df["AREA"] / df["PERIMETER"]

print(df[["AREA", "PERIMETER", "AREA_PER_PERIMETER"]].head(3))

df["AREA_GROUP"] = pd.cut(df["AREA"], bins=3, labels=["choto", "majhari", "boro"])

print(df[["AREA", "AREA_GROUP"]].head(3))
print(df["AREA_GROUP"].value_counts())



d = pd.DataFrame({"date": ["2026-10-14", "2026-12-25", "2027-01-04"]})

d["date"] = pd.to_datetime(d["date"])

d["bochor"] = d["date"].dt.year
d["mash"] = d["date"].dt.month
d["din"] = d["date"].dt.day
d["shoptaher_din"] = d["date"].dt.day_name()

print(d)
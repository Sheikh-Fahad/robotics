import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

marks = pd.Series([45, 60, 60, 72, 88, 91, 55, 60, 79, 100])


print("Mean:", marks.mean())
print("Median:", marks.median())
print("Standard Deviation:", marks.std())
print("Variance:", marks.var())
print("mode:", marks.mode()[0])

sns.histplot(marks)
plt.show()
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# df = pd.DataFrame({"hours": [1,2,3,4,5,6,7,8],
#                    "marks": [40,45,52,58,65,70,78,85]})

# print("corr:", df["hours"].corr(df["marks"]))
# sns.scatterplot(data=df, x="hours", y="marks")
# plt.show()


# marks = pd.Series([45, 60, 60, 72, 88, 91, 55, 60, 79, 100])
# print("probability marks > 60:", (marks > 60).mean())


x = np.random.normal(70, 10, 1000)
print("mean:", x.mean(), "std:", x.std())
sns.histplot(x, kde=True)
plt.show()

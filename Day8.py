import numpy as np
from scipy import stats


Class_a = np.array([1, 2, 3, 4, 5])
Class_b = np.array([2, 3, 4, 5, 6])

print("Class A Mean:", np.mean(Class_a))
print("Class B Mean:", np.mean(Class_b))

t, p = stats.ttest_ind(Class_a, Class_b)
print("P value", p)
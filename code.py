import pandas as pd
import numpy as np
from scipy.stats import psistat

df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")


df1_counts = df1["purchase_category"].value_counts().sort_index()
df2_counts = df2["purchase_category"].value_counts().sort_index()


psi, pval = psistat(df1_counts, df2_counts)
print(f"PSI: {psi:.4f}, p-value: {pval:.4f}")

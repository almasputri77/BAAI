#
# Almas,2025/10/22
# File: Correlation_Analysis.py
# Short description of the task
# Apply correlation analysis to business problem


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

# 1. Input
df = pd.read_csv('Correlation_Analysis_Data.csv')

df.info()

# correlation, pvalue = stats.pearsonr(df['Marketing_Spend'], df['Sales_Revenue'])

correlation_matrix = df.iloc[:,1:6].corr()
print(correlation_matrix.round(3))


# 2. Process
# df[].corr()

# print(df.isnull().sum())
# print(df.isnull().sum().sum())



# 3. Output
# print ('Data loaded successfully!')
# print (f'Dataset shape:{df.shape}')
# print(f'Correlation: {correlation:.2f}')
# print(f'P value: {pvalue:.4e}') 

sns.heatmap(correlation_matrix)
plt.title('Almas is the most intelligent person in the wolrd')
plt.tight_layout()
plt.show()
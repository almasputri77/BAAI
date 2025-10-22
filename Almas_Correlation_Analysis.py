#
# Almas,2025/10/22
# File: Correlation_Analysis.py
# Short description of the task
# Apply correlation analysis to business problem


import pandas as pd

# 1. Input
df = pd.read_csv('Simple_Data.csv')

# 2. Process
print(df.isnull().sum())
print(df.isnull().sum().sum())



# 3. Output
print ('Data loaded successfully!')
print (f'Dataset shape:{df.shape}')
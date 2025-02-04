"" 
import numpy as np
import pandas as py
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "whitegrid")

#load the dataset
file_path =  "sales_data.csv"
df = pd.read_csv(file_path)

print("data set preview:")
print(df.head())

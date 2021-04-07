import pandas as pd 
import seaborn as sns


df = sns.load_dataset('titanic')

# To check if the data has Gaussian Distribution

from scipy.stats import shapiro

stat, p = shapiro(df['age'])

print("Stats=%.3f, p=%.3f" %(stat,p))

if p < 0.05:
    print("Not Gaussian")
else:
    print("Gaussian")
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')

# To check if the data has Gaussian Distribution
# Tests the null hypothesis that a sample comes from a normally distributed population.

# Assumptions : Observations in each samples are IID (Independent and Identically 
# Distributed)

from scipy.stats import shapiro

stat, p = shapiro(df['age'])

print("Stats=%.3f, p=%.3f" %(stat,p))

if p < 0.05:
    print("Not Gaussian")
else:
    print("Gaussian")

stat, p = shapiro(df['fare'])

print("Stats : %.3f, p : %.3f"%(stat,p))

if p < 0.05:
    print("Not Gaussian")
else:
    print("Gaussian")


# Plotting KDE Plot to see both the chart

fig, axs = plt.subplots(ncols=2)

sns.kdeplot(data=df,x='fare',ax=axs[0])
sns.kdeplot(data=df,x='age',ax=axs[1])

# Another common test that measures if the sample is Gaussian 
# Anderson Darling Test

# Assumption : Observation in each sample are IID (Independent and Identically Distributed)
# H0 : The sample has Gaussian Distribution
# H1 : The sample does not have a Gaussian Distribution

from scipy.stats import anderson

result = anderson(df['age'])

for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < 0.05:
        print("Probably Gaussian at the %.1f%% level"%(sl))
    else:
        print("Probably not Gaussian at the %.1f%% level"%(sl))


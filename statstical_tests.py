import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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

# Since Age is Not Gaussian , we will do some transformation

# Applying Power Transformation

df['AGE_POWER'] = np.exp(df['age'])

result = anderson(df['AGE_POWER'])

for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i],result.critical_values[i]
    if result.statistic < 0.05:
        print("Probably Gaussian at the %.1f%%"%(sl))
    else:
        print("Probably not Gaussian at the %.1f%%"%(sl))

# Applying Log Transformation

df['AGE_LOG'] = np.log(df['age'])

result = anderson(df['AGE_LOG'])

for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i],result.critical_values[i]
    if result.statistic < 0.05:
        print("Probably Gaussian at the %.1f%%"%(sl))
    else:
        print("Probably not Gaussian at the %.1f%%"%(sl))

# Correlation Tests 

# Pearson's Correlation

# Assumptions :

# Samples are IID
# Are Normally Distributed
# Have same variance

# H0 : The samples are Independent
# H1 : The samples are not Independent

from scipy.stats import pearsonr

df = df.dropna()

stat, p = pearsonr(df['age'],df['fare'])

print('stat=%.3f, p=%.3f'%(stat,p))

if p > 0.05:
    print("{} and {} are Independent".format('age','fare'))
else:
    print("{} and {} Dependent".format('age','fare'))

# Relationship plot between age and fare

sns.relplot(df['age'],df['fare'])

sns.relplot(df['age'],df['fare'],hue=df['class'])

sns.relplot(df['age'],df['fare'],hue=df['class'],style=df['class'])

sns.relplot(x='age',y='fare',size='class', hue='class', data=df)
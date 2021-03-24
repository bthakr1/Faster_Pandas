# Reference Article 
# https://towardsdatascience.com/sampling-distributions-with-python-implementation-3f4555e1d450

# Sampling Distributions

# Important in inferential statistics where the goal is to draw conclusion about a population
# from a sample 

# Sample is small subset of population. 

import numpy as np 

# Puppies where 1 represent blue eye and 0 represent hazel eye

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

print("Mean of puppies : " , puppies.mean())
print("Standard deviation of population : ", puppies.std())
print("Variance of population : ", puppies.var())


# first lets setup the seed

np.random.seed(123)

# Let's simulate draw from the puppies array.

sample_puppies = np.random.choice(puppies,size=(1,5),replace=True)

print(sample_puppies)

# mean of the draw of puppies

print(sample_puppies.mean())

# Now let's repeat the experiment of drawing 5 puppoes each time for 10,000 times

sample_props = []

for i in range(10_000):
    sample = np.random.choice(puppies,size=5,replace=True)
    sample_props.append(sample.mean())

sample_props = np.array(sample_props)


# Similarly for standard deviation and variance

print("Mean for this experiment is : ", sample_props.mean(), "Standard Deviation is : ", sample_props.std(), "And Variance is : ", sample_props.var())

# Doing the same sampling but this time we will increase the sample size to 20

sample_props_20 = []

for i in range(10_000):
    sample = np.random.choice(puppies, size=20, replace=True)
    sample_props_20.append(sample.mean())

sample_props_20 = np.array(sample_props_20)

print("Mean for this experiment is : ", sample_props_20.mean(), "Standard Deviations is : ", sample_props_20.std(), "And Variance is : ", sample_props_20.var())

import matplotlib.pyplot as plt 

# Histogram of both experiments

# fig = plt.figure(figsize=(10,7))
# bins = np.linspace(0,1,10)
# plt.hist(sample_props,bins=bins,label="Sample Props with 5 sample size")
# plt.hist(sample_props_20,bins=bins,label="Sample Props with 20 sample size")
# plt.title("Histogram with sample size of 5 vs 20")
# plt.legend(loc='upper left')
# #plt.show()


# Law of large number

# As the sample size increases, the sample mean will get closer to the population mean

new_puppies = np.random.choice(puppies,size=100,replace=True)

hundred_sample_props = []

for i in range(10_000):
    sample = np.random.choice(puppies,size=100,replace=True)
    hundred_sample_props.append(sample.mean())

hundred_sample_props = np.array(hundred_sample_props)

# We will increase size in the following lines of code
# You will see with the increase in sample size, the mean of samples
# gets closer to the population mean


print("Origina Mean (also Population): ", puppies.mean())
print("Mean with 5 samples : " , np.random.choice(puppies,size=5,replace=True).mean())
print("Mean with 20 samples : ", np.random.choice(puppies,size=20,replace=True).mean())
print("Mean with 100 samples : ", np.random.choice(puppies,size=100,replace=True).mean())
print("Mean with 1000 samples : ", np.random.choice(puppies,size=1000, replace=True).mean())
print("Mean with 10,000 samples : ", np.random.choice(puppies,size=10_000, replace=True).mean())

# Central Limit Theorem

# With a large enough sample size, the sampling distribution of the the mean will be 
# normally distributed.

# Applies to following scneario.

# Sample Means
# Difference between sample means
# Sample Proportions
# Difference between sample proportions

# Gamms distribution arises when the waiting time or any quantity (in denominator) are relevant to each other.
# Compared to Poisson , where events or rate are not related to each other. 
# Gamms is used in queuing model, climatology, and finance. 
# Amount of rainfall accumulated in reservoir
# Load of web servers

puppies_data = np.random.gamma(1,100,size=1000)


# Now lets create 4 bins with different number of samples taken from the above gamma distribution

mean_size_3 = []
mean_size_10 = []
mean_size_20 = []
mean_size_30 = []

for i in range(10_000):
    mean_size_3.append(np.random.choice(puppies_data,size=(1,3),replace=True).mean())
    mean_size_10.append(np.random.choice(puppies_data,size=(1,10),replace=True).mean())
    mean_size_20.append(np.random.choice(puppies_data,size=(1,20),replace=True).mean())
    mean_size_30.append(np.random.choice(puppies_data,size=(1,30),replace=True).mean())


# plt.figure(figsize=(7,10))
# plt.hist(mean_size_3,label="Mean with sample size of 3")
# plt.hist(mean_size_10,label="Mean with sample size of 10")
# plt.hist(mean_size_20,label="Mean with sample size of 20")
# plt.hist(mean_size_30,label="Mean with sample size of 30")
# plt.axvline(puppies_data.mean(),color='k',linestyle='dashed',linewidth=1)
# plt.legend(loc='upper right')
# plt.show()


# Poisson Distribution 

# Estimates how many times an event can happend in specified time. 
# Describe the probability that an event will occur a certain number of times in a 
# fixed time or space interval.

# Model for a series of discrete event where the average time between events is knows,
# but the exact timing is random.

# Events are memoryless. Arrival of an event is independent of event before and after. 

# Meets the following criteria.

# 1. Events are independent of each other.
# 2. Average rate (event per period ) is constant.
# 3. Two events cannot occur at the same time.

# Number of emails recieved in an hour
# number of leaves in a grass patch
# number of customers walking in a day

# lambda is the rate of known number of occurences or number of events
# size is the size of array

from scipy.stats import poisson
import seaborn as sns

# mu is the lambda
# size is the number of variate in the distribution

data_points = poisson.rvs(mu=3,size=10_000)

# Graphical Representation

# ax = sns.distplot(data_points,
#                 bins=30,
#                 kde=True,
#                 color='skyblue',
#                 hist_kws={'linewidth':15,'alpha':1})
# ax.set(xlabel='Poisson Distribution', ylabel='Frequency')
# plt.show()


# Let's see if Law of large number works for poisson distribution
# Again, we are checking if the "sample mean" comes close to the "population mean"
# if we increase the sample size


print("Population mean of Poisson Process : ", data_points.mean())
print("Sample mean of Poisson Process with 5 Samples : ", np.random.choice(data_points,5,replace=True).mean())
print("Sample mean of Poisson Process with 10 Samples : ", np.random.choice(data_points,10,replace=True).mean())
print("Sample mean of Poisson Process with 20 Samples : ", np.random.choice(data_points,20,replace=True).mean())
print("Sample mean of Poisson Process with 30 Samples : ", np.random.choice(data_points,30,replace=True).mean())
print("Sample mean of Poisson Process with 40 Samples : ", np.random.choice(data_points,40,replace=True).mean())
print("Sample mean of Poisson Process with 80 Samples : ", np.random.choice(data_points,80,replace=True).mean())


# We can see the sample mean becomes closer to the Population mean with increase in sample size


# Now, let's check with Central Limit Theorem with Poisson Process
# CLT suggests that with large enough sample size the sampling distribution 
# of means will follow normal or Gaussian Distribution

sample_mean_poisson_5 = []
sample_mean_poisson_10 = []
sample_mean_poisson_20 = []
sample_mean_poisson_30 = []
sample_mean_poisson_40 = []
sample_mean_poisson_80 = []

for i in range(10_000):

    sample_mean_poisson_5.append(np.random.choice(data_points,5,replace=True).mean())
    sample_mean_poisson_10.append(np.random.choice(data_points,10,replace=True).mean())
    sample_mean_poisson_20.append(np.random.choice(data_points,20,replace=True).mean())
    sample_mean_poisson_30.append(np.random.choice(data_points,30,replace=True).mean())
    sample_mean_poisson_40.append(np.random.choice(data_points,40,replace=True).mean())
    sample_mean_poisson_80.append(np.random.choice(data_points,80,replace=True).mean())


# Graphical Representation

# plt.figure(figsize=(7,10))
# plt.hist(sample_mean_poisson_5,label="Mean with sample size of 5")
# plt.hist(sample_mean_poisson_10,label="Mean with sample size of 10")
# plt.hist(sample_mean_poisson_20,label="Mean with sample size of 20")
# plt.hist(sample_mean_poisson_30,label="Mean with sample size of 30")
# plt.hist(sample_mean_poisson_40,label="Mean with sample size of 40")
# plt.hist(sample_mean_poisson_80,label="Mean with sample size of 80")
# plt.axvline(data_points.mean(),color='k',linestyle='dashed',linewidth=1)
# plt.title("Central Limit Theorem for Poisson Process")
# plt.legend(loc='upper right')
# plt.show()


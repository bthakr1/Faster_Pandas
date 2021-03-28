# Reference Article 
# https://towardsdatascience.com/sampling-distributions-with-python-implementation-3f4555e1d450


# Stephanie Glen. "Binomial Distribution: Formula, What it is and How to use it" 
# From StatisticsHowTo.com: Elementary Statistics for the rest of us! https://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/

# https://www.mathopolis.com/index.php
# https://www.mathsisfun.com/data/binomial-distribution.html

# https://towardsdatascience.com/6-useful-probability-distributions-with-applications-to-data-science-problems-2c0bee7cef28

# https://www.askpython.com/python/normal-distribution

# Sampling Distributions

# Important in inferential statistics where the goal is to draw conclusion about a population
# from a sample 

# Sample is small subset of population. 

import numpy as np 
import pandas as pd

# Puppies where 1 represent blue eye and 0 represent hazel eye

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

print("Mean of puppies : " , puppies.mean())
print("Standard deviation of population : ", puppies.std())
print("Variance of population : ", puppies.var())


# first lets setup the seed

np.random.seed(123)

# Let's simulate draw from the puppies array.

sample_puppies = np.random.choice(puppies,size=(1,5),replace=True)

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


print("Population Mean : ", puppies.mean())
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

# Gamma distribution arises when the waiting time or any quantity (in denominator) are relevant to each other.
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


print("\n")
print("-----"*20)
print("-----------------------------------------Poisson Distribution-----------------------------------------")

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
print("\n")
print("------ Poisson Process Law of Large Number ---------")
print("\n")
print("Population mean of Poisson Process : ", data_points.mean())
print("Sample mean of Poisson Process with 5 Samples : ", np.random.choice(data_points,5,replace=True).mean())
print("Sample mean of Poisson Process with 10 Samples : ", np.random.choice(data_points,10,replace=True).mean())
print("Sample mean of Poisson Process with 20 Samples : ", np.random.choice(data_points,20,replace=True).mean())
print("Sample mean of Poisson Process with 30 Samples : ", np.random.choice(data_points,30,replace=True).mean())
print("Sample mean of Poisson Process with 40 Samples : ", np.random.choice(data_points,40,replace=True).mean())
print("Sample mean of Poisson Process with 80 Samples : ", np.random.choice(data_points,80,replace=True).mean())
print("\n")
print("-------Completed Poisson Process Law of Large Number. ------------")
print("\n")
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

# Practical Examples of Poisson Distribution

# In the World Cup, an average of 2.5 goals are scored each game. Modeling this situation with a Poisson distribution, what is the probability that 
# k goals are scored in a game?

# lambda = 2.5

print("------------------------"*5)
print("Probability for each Possible Outcome ")
print("Probability of getting Zero Goal : ", "{0:.4f}".format(poisson.pmf(0,2.5)))
print("Probability of getting one Goal :", "{0:.4f}".format(poisson.pmf(1,2.5)))
print("Probability of getting Two Goals : ", "{0:.4f}".format(poisson.pmf(2,2.5)))
print("Probability of getting Three Goals : ", "{0:.4f}".format(poisson.pmf(3,2.5)))
print("Probability of getting Four Goals : ", "{0:.4f}".format(poisson.pmf(4,2.5)))
print("------------------------"*5)


# A fast food restaurant gets an average of 2.8 customers approaching the register every minute.
# Assuming the number of customers approaching the register per minute follows a Poisson distribution, 
# what is the probability that 4 customers approach the register in the next minute?
print("\n")
print("-----"*20)
print("Probability of getting 4 customer Approach the Register if Lambda is 2.8 : ", "{0:.3f}".format(poisson.pmf(4,2.8)))
print("-----"*20)
print("\n")


# A statistician records the number of cars that approach an intersection. He finds that an average of 1.6 cars approach the intersection every minute.
# Assuming the number of cars that approach this intersection follows a Poisson distribution, what is the probability that 3 or more cars will approach 
# the intersection within a minute?

print("\n")
print("-----"*20)
print("Probability of getting 3 or more cars if the lambda is 1.6 : ", "{0:.3f}".format(1-poisson.cdf(2,1.6)))
print("-----"*20)
print("\n")

# When a computer disk manufacturer tests a disk, it writes to the disk and then tests it using a certifier. The certifier counts the number of missing pulses or errors. 
# The number of errors in a test area on a disk has a Poisson distribution with λ=0.2.
# What percentage of test areas have two or fewer errors?

print("\n")
print("-----"*20)
print("Probability of getting 2 or fewer errors if the lambda is 0.2 : ", "{0:.2f}".format(100*poisson.cdf(2,0.2)))
print("-----"*20)
print("\n")

# Frequecny of Hurricanes in certain year
# On average over a long period of time we get 1.2 hurricanes over a given years
# lambda = mu = 1.2

x_rvs = pd.Series(poisson.rvs(mu=1.2,size=100_000,random_state=123))

# Mean of Hurricanes 

print("Mean of 100_000 Hurricanes : ", x_rvs.mean())
print("Lambda of Experiment : ", 1.2)
print("Variance of 100_000 Hurricane :", x_rvs.var())

# Mean equals the mu and lambda

data = x_rvs.value_counts().sort_index().to_dict()



# Let's draw the PMF of above date

# plt.figure(figsize=(16,6))
# plt.bar(range(len(data)),list(data.values()),align='center')
# plt.xticks(range(len(data)),list(data.keys()))
# plt.title("Hurricane PMF with Poisson Distribution and Lambda of 1.2")
# plt.show()

print("\n")
print("-----"*20)
print("-----------------------------------------Binomial Distribution-----------------------------------------")
# Binomial Distribution 

# To model binary data i.e. 1 or 0, Yes or No etc.
# Good for modeling decisions

# Important properties

# 1. Set of Trials
# 2. Probablity of Success

# For example, the customer came to shop 10 times
# but bought items only 3 times

# Probablity of observing success given number of trials and probability
# with each of them

# Assumptions :
# 1. Number of trials are independent.
# 2. Number of trials are fixed.
# 3. Probability of success is same between different trials.
# 4. Only two possible outcomes. Not more than 2 or less than 2. 

# binom.pmf(k) = choose(n, k) * p**k * (1-p)**(n-k)

# A coin is tossed 20 times. What is the probability of getting exactly 6 heads.

from scipy.stats import binom

# simulating Experiment of coin toss 

data_points = [binom.pmf(i,10,0.5) for i in range(11)]

print("Probability of getting Exactly 6 heads from 10 trials : ", "{0:.4f}".format(binom.pmf(6,10,0.5)))

print("Mean : %g" %np.mean(data_points))
print("Standard Deviation : %g" %np.std(data_points))

# An example of practical usage of the binomial distribution is to model clicks vs non-clicks on an ad banner, where the probability of success is the click-through rate. 
# The binomial distribution may serve as an anomaly detector. Say you have displayed your ad to 750 users and 34 clicked on it. This gives a click-through rate of 4.5%. 
# If you know the average click-through rate for all your previous ads was 6%, you might want to ask: what’s the probability of 
# observing no more than 4.5% this time? To answer this, you can model your clicks with a binomial distribution with the success probability of 6%, which looks like this:

# Probability of Success : Click Through Rate
# n = 750
# p = 0.045
# p1 = 0.06

result = binom.cdf(34,750,0.06)
print("Probability of observing no more than 34 clicks in 750 impressions ", "{0:.4f}".format(result))

# Toss a coin three times, What is the chance of getting two heads

T = binom(3,0.5) # Sample Space where 3 is the n and 0.5 is the p
print("Getting two heads if we toss coin three times : ", "{0:.4f}".format(T.pmf(2)))

# What is the probability of getting 5 heads in 9 tosses.

T = binom(9,0.5)
print("Probability of getting 5 heads in 9 tosses : ", "{0:.4f}".format(T.pmf(5)))

# John sells sandwiches. 70 % of people choose chickem, the rest something else.
# What is the probability of selling 2 chicken sandwiches to the next 3 customers.

T = binom(3,0.7)
print("Probability of selling 2 chickem sandiwches to the next 3 customers : ", "{0:.4f}".format(T.pmf(2)))

# A fair die is thrown four times. Calculate the probabilities of getting:

# 0 Twos
# 1 Two
# 2 Twos
# 3 Twos
# 4 Twos

T = binom(4,0.1667)

print("Probability of getting 0 Twos : ", "{0:.4f}".format(T.pmf(0)))
print("Probability of getting 1 Twos : ", "{0:.4f}".format(T.pmf(1)))
print("Probability of getting 2 Twos : ", "{0:.4f}".format(T.pmf(2)))
print("Probability of getting 3 Twos : ", "{0:.4f}".format(T.pmf(3)))
print("Probability of getting 4 Twos : ", "{0:.4f}".format(T.pmf(4)))

# Your company makes sports bikes. 90% pass final inspection (and 10% fail and need to be fixed).
# What is the expected Mean and Variance of the 4 next inspections?

T = binom(4,0.90)

print("Mean of next 4 inspections : ", "{0:.4f}".format(T.mean()))
print("Variance of next 4 inspections : ", "{0:.4f}".format(T.var()))

# A fair coin is tossed five times. 
# What is the probability of obtaining two heads?
T = binom(5,0.5)
print("Probability of getting 2 heads from 5 trials : ", "{0:.4f}".format(T.pmf(2)))

# A fair coin is tossed seven times. 
# What is the probability of obtaining five tails?
T = binom(7,0.5)
print("Probability of getting 5 tails in 7 trials : ", "{0:.4f}".format(T.pmf(5)))

# A fair coin is tossed 16 times.
# What is the mean number of Heads?

T = binom(16,0.5)
print("Mean number of heads : ", "{0:.4f}".format(T.mean()))

# A fair coin is tossed 16 times.
# What is the standard deviation for the number of Heads?

print("Standard Deviation of number of Heads : ", "{0:.4f}".format(np.sqrt(T.var())))

# A company makes electronic components for TV's. 
# 95% pass final inspection (and 5% fail and need to be fixed).

# 120 components are inspected in one day. What is the expected number that fail in one day?

T = binom(120,0.05)

print("Expected number of fail in One Day : ", "{0:.4f}".format(T.mean()))

# 120 components are inspected in one day. What is the variance of the number that pass inspection in one day?

T = binom(120,0.95)

print("Variance of number that pass inspection in one day : ", "{0:.4f}".format(T.var()))

# A fair cubical die is thrown four times.
# Use the binomial probability formula to calculate the probability of exactly two 5's.

T = binom(4,0.1667)

print("Probability of getting exactly two 5s : ", "{0:.4f}".format(T.pmf(2)))

# The diagram shows a spinner made up of a piece of card in the shape of a regular pentagon, with a toothpick pushed through its center. 
# The five triangles are numbered from 1 to 5.Each time, the spinner is spun until it lands on one of the five 
# edges of the pentagon. The spinner is spun four times.
# Use the binomial probability formula to calculate the probability of exactly two 1's.

T = binom(4,0.2)

print("Probability of Exactly two 1s : ", "{0:.4f}".format(T.pmf(2)))

# A fair coin is tossed five times.
# Use the binomial probability formula to calculate the probability of at least four heads.

# 1 Head
# 2 Head
# 3 Head

T = binom(5,0.5)

# Getting "at least" 4 heads means "at most" 3 Heads

print("Probability of getting at least 4 heads in 5 trials " , "{0:.4f}".format(1-T.cdf(3)))

# A fair coin is tossed six times.
# Use the binomial probability formula to calculate the probability of at most two tails.

T = binom(6,0.5)

# At most 2 Tails means sum of all probabilities upto 2 
# No Tails
# 1 Tail
# 2 Tail

print("Probability of getting at most 2 Tails in 6 trials is : ", "{0:.4f}".format(T.cdf(2)))

# A fair coin is tossed 100 times. What is the probability that:
# a.  heads will appear exactly 52 times?
# b.  there will be at most 52 heads?
# c.  there will be at least 48 heads?  

T = binom(100,0.5)

print("Probability of getting Heads EXACTLY 52 times : ", "{0:.4f}".format(T.pmf(52)))

print("Probability of getting AT MOST 52 Heads : ", "{0:.4f}".format(T.cdf(52)))

print("Probability of getting AT LEAST 48 Heads : ", "{0:.4f}".format(1-T.cdf(47)))

# Law of large number for Binomial Distribution

# Law of Lrage Number suggests that with enough sample size the mean of sample
# will be close to the Population Mean

# n specifieis we will get 0 or 1

population_binomial = binom.rvs(n=1,p=0.5,size=100_000)

# Now lets start getting samples of increasing size from the above population
# We will start with Population Mean and then start the experiment

print("Poluation mean of Binomial Distribution : ", population_binomial.mean())
print("Sample mean with size of 5 : ", np.random.choice(population_binomial,size=5,replace=True).mean())
print("Sample mean with size of 10 : ", np.random.choice(population_binomial,size=10,replace=True).mean() )
print("Sample mean with size of 20 : ", np.random.choice(population_binomial,size=20,replace=True).mean())
print("Sample mean with size of 100 : ", np.random.choice(population_binomial,size=100,replace=True).mean())
print("Sample mean with size of 500 : ", np.random.choice(population_binomial,size=500,replace=True).mean())

# Central Limit Theorem with binomial distribution
# CLT suggests that with large enough sample size the sampling distribution of means
# will follow normal distribution 

# This time we will do experimentation with Fair Die
# to have six possible outcomes instead of 2

n1 = np.array([1,2,3,4,5,6])

binomial_population = np.random.choice(n1,size=100_000,replace=True)

sample_mean_binomial_5 = []
sample_mean_binomial_10 = []
sample_mean_binomial_20 = []
sample_mean_binomial_100 = []
sample_mean_binomial_500 = []

for i in range(10_000):
    sample_mean_binomial_5.append(np.random.choice(binomial_population,size=5,replace=True).mean())
    sample_mean_binomial_10.append(np.random.choice(binomial_population,size=10,replace=True).mean())
    sample_mean_binomial_20.append(np.random.choice(binomial_population,size=20,replace=True).mean())
    sample_mean_binomial_100.append(np.random.choice(binomial_population,size=100,replace=True).mean())
    sample_mean_binomial_500.append(np.random.choice(binomial_population,size=500,replace=True).mean())


# Histogram to see the result of distribution of mean

# plt.figure(figsize=(7,10))
# plt.hist(sample_mean_binomial_5,label="Mean with sample size of 5")
# plt.hist(sample_mean_binomial_10,label="Mean with sample size of 10")
# plt.hist(sample_mean_binomial_20,label="Mean with sample size of 20")
# plt.hist(sample_mean_binomial_100,label="Mean with sample size of 100")
# plt.hist(sample_mean_binomial_500,label="Mean with sample size of 500")
# plt.axvline(binomial_population.mean(),color='k',linestyle='dashed',linewidth=1)
# plt.title("Central Limit Theorem for Binomial Distribution")
# plt.legend(loc='upper right')
# plt.show()


print("\n")
print("-----"*20)
print("-----------------------------------------Normal Distribution-----------------------------------------")

# Continous distribution or a function that can take any values on the real line. 

# Here we have created 2000 random numbers between 1 and 50

x = np.linspace(1,50,10_000)

def normal_dist(x):

    mean = np.mean(x)
    sd = np.std(x)

    prob_density = (np.pi * sd) * (np.exp(-0.5*((x-mean)/sd)**2))
    return prob_density


pdf = normal_dist(x)

print("Length of pdf : ", len(pdf))

# Let's draw the pdf of normal distribution

# plt.figure(figsize=(12,18))
# plt.plot(x,pdf,color='red')
# plt.xlabel("Data Points")
# plt.ylabel("Probability Density")
# plt.title("Probability Density Function for Normal Distribution")
# plt.show()


# Let's create some data now 

# PDF : Probability Density Function
# CDF : Cummulative Distribution Function

from scipy.stats import norm
import seaborn as sns

# Let's create some random points

data_points = np.arange(1,10,0.01)

pdf_data_points = norm.pdf(data_points,loc=5.5,scale=1) # loc is the location of mean. Default is Zero.
# scale is the standard deviation of data


# sns.set_style('whitegrid')
# sns.lineplot(data_points,pdf_data_points,color='black')
# plt.xlabel("Heights")
# plt.ylabel("Probability Density")
# plt.title("Height Distribution ")
# plt.show()

# Practical Question 

# if we were asked to pick one person randomly from this distribution, then 
# what is the probability that the height of the person will be smaller than 4.5 ft.

T = norm(loc=5.3,scale=1)

print("What is the probability that the height of the person will be smalled than 4.5 Ft :", "{0:.4f}".format((T.cdf(4.5))*100))

# we were asked to pick one person randomly from this distribution, then what is the probability 
# that the height of the person will be between 6.5 and 4.5 ft. ?

print("What is the probability that a person selected will be between 4.5 ft and 6.5 ft : ", "{0:.4f}".format((T.cdf(6.5) - T.cdf(4.5))*100))

# Law of Large number for Normal Distribution 

data_points = norm.rvs(np.arange(1,50,100_000),scale=1,loc=0)

print(np.mean(data_points))
print(np.std(data_points))


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
plt.style.use('ggplot')


# getting version number 

#print(pd.__version__)

# passing dictionary as data frame 

df = pd.DataFrame({'column 1': [1000,3000,''], 'name': ['amar','akbar','anthony'], 'age' : [201,201,'NA']})

print(df)

# replace the space in first column name

df.columns = df.columns.str.replace(' ','_')

real_column_name = df.columns

print(df)

# Let's add Prefix 

df.columns = ['X_' + str(col) for col in df.columns]

print(df)

# Let's add Suffix 

df.columns = [str(col) + '_Y' for col in df.columns]

print(df)

df.columns = real_column_name

print(df)

# Reversing the rows

# First lets check the right way

print(df)

# Now reverse the rows 

print(df.loc[::-1])

# Let's get some data frame 
print("-"*200)
print("\n")
print("New Section Start : ")

df = sns.load_dataset('geyser')

print(df.head())

# with indexing also starting from 0

print(df.loc[::-1].reset_index(drop=True).head())

# Reverse columns order

print(df.loc[:,::-1].head())

# Selecting number columns only

only_numeric = df.select_dtypes(include='number').columns

print("Only Numberic Columns : ", only_numeric)

# Selecting object columns only

only_object = df.select_dtypes(include='object').columns

print("Only Object Columns : ", only_object)

# Selecting only date columns 

only_date = df.select_dtypes(include='datetime').columns

print("Only Date Columns : ", only_date)

# Do not select object columns

except_object = df.select_dtypes(exclude='object').columns

print("Everything Except Object Columns : ", except_object)

# convert strings to numbers

df = pd.DataFrame({'col_one':['1.1','2.2','3.3'],
                    'col_two': ['4.4','5.5','6.6'],
                    'col_three': ['7.7','8.8','-']

})

print("Dataframe without type conversion")
print(df)

df.astype({'col_one':'float','col_two':'float'}).dtypes
print("After changing one and two column")
print(df)

pd.to_numeric(df.col_three,errors='coerce')
print("Using Coerce to change the third column")
print(df)

df = df.apply(pd.to_numeric,errors='coerce').fillna(0)
print("Changing all three at once using Apply")
print(df)

# Reduce data frame size

print(sns.get_dataset_names())

df = sns.load_dataset('car_crashes')

print(df.info())

print(df.info(memory_usage='deep'))

print(df.head())

# print based on location

# We will use index location for this
# Here we are printing 3 to 8 rows and only one column i.e. 1
print("\n")
print("Printing Rows from 3 to 8 and Columns from 1 to 2")
print("\n")
print(df.iloc[3:9,1:3])


# Now let's use the loc parameter

print("\n")
df.set_index('abbrev',inplace=True)

# Printing the index for AR, AZ , and OK with columns from "alcohol" to "ins_premuim"

print(df.loc[['AR','AZ','OK'],'alcohol':'ins_premium'])

# Let's select some other csv and try iloc and loc with that dataframe

df = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')

# Let's print the first two columns and 7-12 rows

print("Let's print the first two columns and 7-12 rows")
print(df.iloc[7:13,1:3])

# Let's print all columns and 15-35 rows

print(df.iloc[15:36,:])

# How about 3 to 7 column and 19-22 rows

print(df.iloc[19:23,3:8])

# Next we will try loc

print(df.county.value_counts())

df.set_index('county',inplace=True)

# Filetring everything with index as "Greater London"
print("\n")
print("Filetring everything with index as 'Greater London'")
print("\n")
print(df.loc['Greater London'])

# Let's do something interesting

# Print everyone who is using study.co.uk
print("\n")
print("Print everyone who is using study.co.uk")
print("\n")
print(df.loc[df['email'].str.contains('study.co.uk')])

# How about with gmail.com
print("\n")
print("Print everyone who is using gmail.com")
print("\n")
print(df.loc[df['email'].str.contains('gmail.com')])

# Last name as Katie
print("\n")
print("Print everyone who has a last name Katie")
print("\n")
print(df.loc[df['last_name'].str.contains('Katie')])

df.reset_index(inplace=True)

# Had a lot of fun with iloc and loc

# Some string manipulation

df[['area_code_phone_1','real_phone_phone_1']] = df['phone1'].str.split('-',expand=True)

print(df.head())

# Let's get the area code and phone number 2 for phone number 2

df[['area_code_phone_2','real_phone_phone_2']] = df['phone2'].str.split('-',expand=True)

print(df.tail())

# Let's get domain names from the email ids

df.drop(['area_code_phone_1','real_phone_phone_1','area_code_phone_2','real_phone_phone_2'],axis=1,inplace=True)

print("Getting domain names from the email ids")

df[['email','domain']] = df['email'].str.split('@',expand=True)

print(df.head())

# Let's see how many names start with A in first_name

print("Let's see how many names start with A in first_name")
print(df['first_name'].str.startswith('A'))
print("Count of names starting with A :" , df['first_name'].str.startswith('A').sum())
# How about how many ends with A in the first_name

print("How about how many ends with A in the first_name")
print(df['first_name'].str.endswith('a'))
print("Count of names ending with A :", df['first_name'].str.endswith('a').sum())

# Let's count on how many people are from same county

print(df['county'].value_counts(sort=True))

# How about domain names

print(pd.crosstab(df['county'],df['domain']))

# Let's remove any zero columns

cross_tab_county_domain = pd.DataFrame(pd.crosstab(df['county'],df['domain'],margins=True,margins_name="Total"))

# Remove any column with 0 entries

print(cross_tab_county_domain.loc[:,(cross_tab_county_domain != 0).any(axis=0)])

# Remove any row with 0 entries

print(cross_tab_county_domain.loc[(cross_tab_county_domain != 0).any(axis=1),:])

# Let's get the margin values. Only top 5

print(cross_tab_county_domain.iloc[-1,:-1].sort_values(ascending=False).head(5))

# Let's get the sns datasets again

print("SNS Dataset Names : ", sns.get_dataset_names())

# changing the dataframe 
# We are going to use mpg as we will be exploring filtering and pivoting a lot
print("\n")
print("*"*100,"New Data Frame : mpg","*"*100)
print("\n")
df = sns.load_dataset('mpg')

# Let's do some filtering

print("Lets get rows where weight is higher than 3400 and model year is smaller than 75")

print(df[(df['weight'] > 3400) & (df['model_year'] < 75)])

# How about origin not in USA

print("Origin not in USA")

print(df[df['origin'] != 'usa'])

# Let's see the average, min, median, and max mpg for all the countries

table = pd.pivot_table(df,index=['origin'],aggfunc={'mpg':[np.median,np.mean,np.max,np.min]})
print(table)
print("seems like Japan has the highest mpg & USA the lowest")

# How about average, min, median, and max horsepower for all the countries

table = pd.pivot_table(df,index=['origin'],aggfunc={'horsepower':[np.median,np.mean,np.max,np.min]})
print(table)
print("US has the highest horsepower while Japan the lowest")

# Let's combine both 

table = pd.pivot_table(df,index=['origin'],aggfunc={'mpg':[np.median],
                                                    'horsepower':[np.median]})

print(table)

# How about model year and origin
# Just for mpg

table = pd.pivot_table(df,index=['model_year','origin'],aggfunc={'mpg':[np.median],'horsepower':[np.median]})
print(table)

# Does US cars have more Cylinders

table = pd.pivot_table(df,index=['origin'],columns=['cylinders'],aggfunc='size',fill_value=0)
print(table)

# How about distribution of Origin and Model years

table = pd.DataFrame(pd.pivot_table(df,index=['model_year'],columns=['origin'],aggfunc='size'))

print(table)

# Let's see how many cars by origin and cylinders and their respective horsepower

table = pd.pivot_table(df,index=['origin'],columns=['cylinders'],values=['horsepower'],aggfunc=np.median,fill_value='NA')

print(table)

# Let's see the same for mpg

table = pd.pivot_table(df,index=['cylinders'],columns=['origin'],values=['mpg'],aggfunc=np.median)
print(table)

# Let's do it again on Titanic Datasets

df = sns.load_dataset('titanic')

# Let's see how many men and women were there

print(df['sex'].value_counts())

print(df.head())

# Survived or not survived based on sex

table = pd.pivot_table(df,index=['alive'],columns=['sex'],aggfunc='size')

print(table)

# same thing can be done with cross tab

print(100*pd.crosstab(df['alive'],df['sex'],margins=True,margins_name="Total",normalize=True))

# Let's see the same for class

table = pd.pivot_table(df,index=['alive'],columns=['class'],aggfunc='size')

print(table)

# Really interesting. 
# I am curious if we have any independence between "Class" and "Survival"

# We can use Chi Square Test for this
# Both features are "discrete"
# Null Hypothesis : There is no relationship between the "Class" and "Survival"
# Alternate Hypothesis : There is a significant realtionship between the "Class" and "Survival"

# Remember "If p is low H0 must go"
# p value is also called alpha value and denotes the probability of erroronesously rejecting H0
# when H0 is True
# Degree of Freedom = (number of rows - 1) * (number of columns - 1)

from scipy.stats import chi2_contingency

contingency_table_alive_class = pd.crosstab(df['alive'],df['class'])

stat, p, dof, expected = chi2_contingency(contingency_table_alive_class)

alpha = 0.05

print("p value is " + str(p))

if p <= alpha:
    print("Dependent (reject H0) : Survival and Class are Dependent")
else:
    print("Fail to reject Null Hypothesis : Survial and Class are Independent")

contingency_table_alive_sex = pd.crosstab(df['alive'],df['sex'])

stat, p, dof, expected = chi2_contingency(contingency_table_alive_sex)

print("p value is " + str(p))

if p <= alpha:
    print("Dependent (reject H0) : Survival and Sex are Dependent")
else:
    print("Fail to reject Null Hypothesis : Survial and Sex are Independent")

# Back to pivot tables

# Let's see the average age of Survining and Not Surviving members

table = pd.pivot_table(df,index=['alive'],columns=['age'],aggfunc={'age':[np.median,np.mean,np.min,np.max]})

print(table)

# Hmm a lot of age. Let's bin those.
# But first let's see the distribution

print(df['age'].describe())

# Minimum is 0 and Maximum is 80

# Let's cut this into 10 pieces

bins = list(np.linspace(0,100,11))

labels = ['0','0 to 10','10 to 20','20 to 30','30 to 40','40 to 50','50 to 60','60 to 70','70 to 80','80 to 90']

df['binned_age'] = pd.cut(df['age'],bins=bins,labels=labels)

# Now Let's see if the age has any influence on the survial 

table = pd.pivot_table(df,index=['alive'],columns=['binned_age'],aggfunc='size')

# Now let's see if the age had any influence on survival

contingency_table_alive_age = pd.crosstab(df['alive'],df['binned_age'])

stat, p , dof, expected = chi2_contingency(contingency_table_alive_age)

print("The p value is : ", "{0:.4f}".format(p))

if p <= alpha:
    print("There is a relationship between age and survival")
else:
    print("No relatonship between Age and Survival")

# Let' see the power of Group BY
# Though with pivot table most of the things can be done very easily

print("Row Count for each Class ")
print(df.groupby(['class']).size())

# Find different values for each group

print(df.groupby(['class']).groups.keys())

# Let's get average fare for each class

print(df.groupby(['class'])['fare'].mean())

# How about the sex

print(df.groupby(['sex'])['fare'].mean())

# Let's see by two columns now 

print(df.groupby(['sex','class']).agg({'fare':['mean','min','max']}))

# the same thing through pivot table

table = pd.pivot_table(df,index=['sex','class'],aggfunc={'fare':[np.mean,np.min,np.max]})
print(table)

# Let's see average , minimum, and maximum age for each class

print(df.groupby(['class']).agg({'age':['mean','min','max']}))


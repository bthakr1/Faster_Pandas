
import pandas as pd 
import numpy as np 
import seaborn as sns


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

df.set_index('city',inplace=True)

print(df.head())

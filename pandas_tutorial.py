
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
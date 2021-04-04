
import pandas as pd 
import numpy as np 

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

# with indexing also starting from 0

print(df.loc[::-1].reset_index(drop=True))
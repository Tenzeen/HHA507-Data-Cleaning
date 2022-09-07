#import packages
import pandas as pd
import numpy as np
import datetime as dt
import numpy as np

#Load dataset into python
df = pd.read_csv('data/School_Learning_Modalities.csv')

#Print column and row counts
print(df.shape) #781,148 rows x 9 columns
#Print column names
print(df.columns) #'District NCES ID', 'District Name', 'Week', 'Learning Modality',
                  #'Operational Schools', 'Student Count', 'City', 'State', 'ZIP Code'

#clean column names
df.columns = df.columns.str.lower() #made all characters lowercase
df.columns = df.columns.str.replace(' ', '_') #replaced whitespace with '_'
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') #made sure that column names were thoroughly cleaned
df.columns

#clean strings within columns
#list of column types
df.dtypes
#list of columns with strings
strings = df.select_dtypes('object').columns
strings

#clean strings within columns by removing whitespace, special characters, and uncapitalizing all characters
df['district_name'] = df['district_name'].str.replace('[^A-Za-z0-9]+', '_')
df['district_name'] = df['district_name'].str.lower()

df['week'] = df['week'].str.replace('[^A-Za-z0-9]+', '_')
df['week'] = df['week'].str.lower()

df['learning_modality'] = df['learning_modality'].str.replace('[^A-Za-z0-9]+', '_')
df['learning_modality'] = df['learning_modality'].str.lower()

df['city'] = df['city'].str.replace('[^A-Za-z0-9]+', '_')
df['city'] = df['city'].str.lower()

df['state'] = df['state'].str.replace('[^A-Za-z0-9]+', '_')
df['state'] = df['state'].str.lower()

#convert week column to datetime
df['week'] = pd.to_datetime(df['week'])

#duplicates cleaning
df.duplicated() #check for duplicates
df.drop_duplicates() #remove duplicates

#missing values cleaning
#check for missing values
df.isnull().sum()
#replace empty cells with nan 
df.replace(to_replace='', value=np.nan, inplace=True)

#Create new column called modality_inperso. This column contains a binary value of true or false
df['modality_inperson'] = (df['learning_modality'].apply(lambda x: 'true' if x == 'in_person' else 'false'))

#Save cleaned version
df.to_csv('data/School_Learning_Modalities.csv')
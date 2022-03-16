# -*- coding: utf-8 -*-
"""
Created by love on Tue Mar 15 22:10:57 2022

@author: oussama

Pandas Library

"""

"""
    Loading data
"""

#import library:
import pandas as pd

dataFrame = pd.read_csv('pokemon_data.csv')

#•printing a specic number of rows from the top of our dataframe:
print(dataFrame.head(3))

#•printing a specic number of rows from the tail of our dataframe:
print(dataFrame.tail(3))

dataFrame2 = pd.read_excel('pokemon_data.xlsx')

dataFrame3 = pd.read_csv('pokemon_data.txt', delimiter = '\t')


"""
    Reading Data in pandas:
"""

#Read headers
print(dataFrame.columns)

#Read each column
print(dataFrame[['Name', 'Type 1']]) #OR
print(dataFrame.Name)
print(dataFrame['Name'][2:5])

#♣Read each row
print(dataFrame.iloc[1]) #row with index = 1
print(dataFrame.iloc[3:6]) #rows from index = 3 until index = 5
for index, row in dataFrame.iterrows():
    print(index, row['Name'])
dataFrame.loc[dataFrame['Type 1'] == "Fire"]

#Read a specific location (R,C)
print(dataFrame.iloc[2, 1])

"""
    Sorting/Describing Data
"""
dataFrame.describe()
dataFrame.sort_values(['Name', 'HP'], ascending = False)
dataFrame.sort_values(['Name', 'HP'], ascending = [1, 0]) #First one ascending , second descending


"""
    Making changes to the data:
"""
#Add a new column
dataFrame['Total'] = dataFrame['HP'] + dataFrame['Attack'] + dataFrame['Defense'] + dataFrame['Sp. Atk'] + dataFrame['Sp. Def'] + dataFrame['Speed']
dataFrame['Total'] = dataFrame.iloc[:, 4:10].sum(axis = 1)

#Drop a specific column
dataFrame = dataFrame.drop(columns = ['Total']) #axis = 0 vertically , axis = 1 horizontaly

#Getting columns as a list
cols = dataFrame.columns.values
#change order of our columns
dataFrame = dataFrame[cols[0:4] + cols[-1] + cols[4:12]]

"""
    Saving our data
"""
#saving to csv
dataFrame.to_csv('modified.csv')
dataFrame.to_csv('modified2.csv', index = False) #saving without column = index 

#saving to excel file
dataFrame.to_excel('excelFile.xlsx')

"""
    Filtering Data:
"""
dataFrame.loc[(dataFrame['Type 1'] == 'Grass') & (dataFrame['Type 2'] == 'Poison')]
new_df = dataFrame.loc[(dataFrame['Type 1'] == 'Grass') | (dataFrame['Type 2'] == 'Poison')]

#reset index
new_df = new_df.reset_index(drop = True) #drop = True ==> drop the column for the last index

dataFrame.loc[dataFrame['Name'].str.contains('Mega')]
# ~ ==> NOT


"""
    Conditional changes
"""
dataFrame.loc[dataFrame['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
dataFrame.loc[dataFrame['Type 1'] == 'Fire', 'Legendry'] = True

dataFrame = pd.read_csv('modified.csv')

dataFrame.loc[dataFrame['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']

dataFrame = pd.read_csv('modified.csv')

"""
    Aggregate Statistics(GroupBy)
"""
#the average of all Type 1 pokemon
dataFrame.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)

#the sum
dataFrame.groupby(['Type 1']).sum()

#count
dataFrame['count'] = 1
dataFrame.groupby(['Type 1']).count()['count']

dataFrame.groupby(['Type 1', 'Type 2']).count()

"""
    Working with large amounts of data
"""
newDataFrame = pd.DataFrame(columns = dataFrame.columns)
for dataFrame in pd.read_csv('modified.csv', chunksize = 5): #5 Rows beeing passed it on a time
    #print("chunck data frame")
    #print(dataFrame)
    results = dataFrame.groupby(['Type 1']).count()
    newDataFrame = pd.concat([newDataFrame, results])





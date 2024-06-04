# ----------------------------------------------------------------------
# Name:        lecture23
# Purpose:     Demonstrate the use of Pandas
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 23.

Demonstrate using Pandas to answer the following questions about
National Parks.
What state is Glacier National Park in?
What is the park code and acreage of Yosemite National Park?
What is the largest national park in the US?
What state is home to the smallest national park?
How many national parks are there in Washington State?
How many national parks are there in California?
What is the average acreage of National parks?
What is the total area occupied by national parks in each state and
between which latitudes/longitudes are these parks located?
"""
import pandas as pd
import numpy as np
import re

def q1(df):
    """
    What state is Glacier National Park in?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: string - the name of the state where Glacier National Park
            is located
    """
    return df.loc['Glacier National Park','State']

def q2(df):
    """
    What is the park code and acreage of Yosemite National Park?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: tuple (string, integer) Park code and acreage
    """
    return (df.loc['Yosemite National Park','Park Code'],
            df.loc['Yosemite National Park','Acres'])

def q3(df):
    return df['Acres'].idxmax()

def q4(df):
    return df.loc[df['Acres'].idxmin(),'State']
def q5(df):
    list = df[df['State'] == 'WA']
    return len(list)
def q6(df):
    list = df[df['State'].str.contains('CA')]
    return len(list)
def q7(df):
    return df['Acres'].mean()
def q8(df):
    return df.groupby('State').agg({'Acres':np.sum,
                                    'Latitude': (np.max,np.min),
                                    'Longitude':(np.max,np.min)})


def species_q1(df):
    return len(df)
def species_q2(df):
    return len(df['Scientific Name'].unique())
def species_q3(df):
    return len(df[df['Conservation Status'] == 'Endangered'])
def species_q4(df):
    return len(df[(df['Conservation Status'] == 'Threatened') & (df['Nativeness'] == 'Native')])
def species_q5(df):
    return len(df[(df['Category'] == 'Bird') & (df['Conservation Status'] == 'Species of Concern')])
def species_q6(df):
    return df[()]
def species_q7(df):
    return df.loc[(df['Common Names'].str.contrains(r'\bBear\b',flags=re.IGNORECASE)) & (df['Category'] == 'Mammal'),'Park Name'].unique()
def both_q1(df):
    wa_only = df.loc9['WA']
    return len(wa_only.loc[wa_only['Conservation Status'] == 'Endangered'])
def both_q2(df):
    result = df.groupby('State').count()["Common Names"]
    return result.idxmax()
def both_q3(df):
    endangered_df = df.loc[df["Conservation Status"].str.contains("Endangered",na=False)]
    result = endangered_df.groupby('State').count()['Common Names'].idxmax()
    return result

def main():
    # Read the csv file and use colum 0 (Park Name) as our index
    df_parks = pd.read_csv('parks.csv', index_col=1)
    df_species = pd.read_csv('species.csv', index_col=0, usecols=range(13))
    df_both = pd.merge(df_parks,df_species, on = 'Park Name')
    df_both.set_index('State',inplace = True)
    df_multi = pd.merge(df_parks,df_species,on = 'Park Name')
    df_multi.set_index(["State", "Park Code"], inplace = True)
    print(df_multi.loc['CA'])
    # Question 1
    #print(f'{both_q3(df_both)}')

    # Question 2


    # Question 3


    # Question 4


    # Question 5


    # Question 6


    # Question 7


    # Question 8



if __name__ == "__main__":
    main()

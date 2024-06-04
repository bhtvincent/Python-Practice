# ----------------------------------------------------------------------
# Name:        hw10
# Purpose:     Use pandas to manipulate a big data set on cars
#
# Date:        4/29/19
# ----------------------------------------------------------------------
"""
Module to use pandas to manipulate a big data set on cars.

q1() - number of cars manufactured by honda
q2() - number of guzzlers
q3() - Highest FE
q4() - lowest FE
q5() - highest FE with 4x4
q6() - carline with biggest difference in city vs hwy FE
q7() - avg FE with supercharge
q8() - SUV with lowest fuel cost
q9() - mnf with most manual
q10() - avg annual fuel cost by division
q11() - perfect car

"""
import pandas as pd
import re
import numpy as np

def q1(df):
    '''How many cars are made by the manufacturer Honda?

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (integer) number of cars made by honda
    '''

    return len(df[df['Mfr Name'] == 'Honda'])


def q2(df):
    '''How many 'Guzzlers' are there?

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (integer) number of guzzlers
    '''

    return len(df['Guzzler?'].dropna())


def q3(df):
    '''What is the value of the highest combined Fuel Efficiency as
    given by "Comb FE (Guide) - Conventional Fuel"?

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (float) highest value of combined fuel efficiency
    '''

    return max(df['Comb FE (Guide) - Conventional Fuel'])


def q4(df):
    '''Which division and car line has the lowest combined
    FE - Conventional Fuel?

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (tuple of strings) division and carline
    '''

    min_fe_carline = df['Comb FE (Guide) - Conventional Fuel'].idxmin()
    min_fe_division = df['Division'].loc[min_fe_carline]

    return (min_fe_division, min_fe_carline)


def q5(df):
    '''What is the highest combined FE - Conventional Fuel among
    all wheel drives.  Use 'Drive Desc'.

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (float) highest combined FE - Conventional Fuel
    '''

    awd_max_fe = df[df['Drive Desc'] == 'All Wheel Drive']
    return awd_max_fe['Comb FE (Guide) - Conventional Fuel'].max()

def q6(df):
    '''Which car line has the largest difference between Highway and
    City Fuel efficiency - Conventional Fuel?

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (string) carline
    '''

    df['Difference'] = df['Hwy FE (Guide) - Conventional Fuel'] - \
                       df['City FE (Guide) - Conventional Fuel']
    return df['Difference'].idxmax()


def q7(df):
    '''What is the average annual fuel cost
    (Annual Fuel1 Cost - Conventional Fuel) of supercharged cars?

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (float) average annual fuel cost
    '''
    costs = df[df['Air Aspiration Method Desc'].str.startswith(
        'Supercharged', na=False)]
    return costs['Annual Fuel1 Cost - Conventional Fuel'].mean()



def q8(df):
    """What SUV has the lowest annual fuel cost?
    Use "Carline Class Desc" to identify SUVs.
    The function must return a string.

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (string) the SUV with the lowest annual fuel cost
    """
    df_suvs = df[df['Carline Class Desc'].str.contains(r'\bSUV\b', na=False)]
    return df_suvs['Annual Fuel1 Cost - Conventional Fuel'].idxmin()

def q9(df):
    """
    Which manufacturer has the most cars with manual transmission?
    The function must return a string.

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (string) the manufacturer with the most cars with manual
    transmission
    """
    df_manual = df.loc[df['Transmission'].str.contains('Manual', na=False)]
    return df_manual.groupby('Mfr Name').count()['Transmission'].idxmax()

def q10(df):
    """
    What is the average annual fuel cost by car division?
    The function must return a Pandas series.

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (Pandas Series) A series showing the average annual fuel
    cost by car division
    """
    return df.groupby('Division').agg({'Annual Fuel1 Cost - Conventional '
                                       'Fuel': np.average})

def q11(df):
    """
    What criteria would you use to buy a car?  Write a function that
    returns your perfect car based on your criteria.  This function must
    return a string representing the perfect carline for you.

    Criteria: Highest Combined Fuel Efficiency for a two-seater car

    :param df: (Pandas DataFrame) represents data in 2019 FE Guide.csv
    :return: (String) Sedan with the highest combined fuel efficiency
    """
    two_seaters = df[df['Carline Class ' \
                        'Desc'].str.contains('Two Seaters', na=False,
                                             flags=re.IGNORECASE)]
    return two_seaters['Comb FE (Guide) - Conventional Fuel'].idxmax()

def main():
    # read csv file and use col 3 (carline) as index
    df_cars = pd.read_csv('2019 FE Guide.csv', index_col=3)
    print(q1(df_cars))
    print(q2(df_cars))
    print(q3(df_cars))
    print(q4(df_cars))
    print(q5(df_cars))
    print(q6(df_cars))
    print(q7(df_cars))
    print(q8(df_cars))
    print(q9(df_cars))
    print(q10(df_cars))
    print(q11(df_cars))

if __name__ == '__main__':
    main()

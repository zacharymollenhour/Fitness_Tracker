import pandas as pd
import numpy as np


def main():
    #Read in CSV
    user_dataframe = pd.read_csv("./workoutData/user_readme.txt",error_bad_lines=False,delimiter=',',names = 
    ['Name', 'Age', 'Weight','Height','BMI'])


    #Store Data for starting metrics
    Name = user_dataframe.loc[:,'Name'].values[0]
    Age = user_dataframe.loc[:,'Age'].values[0]
    startingWeight = user_dataframe.loc[:,'Weight'].values[0]
    startingHeight = user_dataframe.loc[:,'Height'].values[0]
    startingBMI = user_dataframe.loc[:,'BMI'].values[0]




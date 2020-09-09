import pandas as pd
import numpy as np
from fitparse import FitFile
import matplotlib.pyplot as plt

def main():

    startingMetrics()

def workoutMetrics():
    pushup_df = pd.read_csv("./workoutData/user_readme.txt",error_bad_lines=False,delimiter=',',names = 
    ['Name', 'Age', 'Weight','Height','BMI'])


def startingMetrics():

    #Read in CSV
    cols = ['Date', 'Workout Type', 'Distance','Duration']
    user_dataframe = pd.read_csv("./workoutData/runworkout_data.csv",error_bad_lines=False,delimiter=',',usecols=cols)
    metrics = []
    cols2 = ['avgmile']

    #Get means for distance and duration
    df_dropped = user_dataframe.drop(['Date','Workout Type'], axis=1)
    means = df_dropped.mean()
    errors = df_dropped.std()
    fig, ax = plt.subplots()
    means.plot.bar(yerr=errors, ax=ax)
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


    #Store Data for starting metrics
    Date = user_dataframe.loc[:,'Date']
    Workout_Type = user_dataframe.loc[:,'Workout Type']
    Distance = user_dataframe.loc[1:,'Distance']
    Duration = user_dataframe.loc[1:,'Duration']
    user_dataframe.dropna()

    #print(user_dataframe.loc[['9/9/2020','Duration']])
    Distance.dropna()
    Duration.dropna()
    metrics.append([(Distance / Duration)])
    #print(Distance)

    df = pd.DataFrame(metrics, columns=cols2)
    df.dropna()
    print(df)
    #print(averageMileTime)

main()




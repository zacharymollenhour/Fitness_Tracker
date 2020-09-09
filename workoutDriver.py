#Driver code for the workout functions
#includes the class for workout
from datetime import date
import csv

#Class for tracking workout data
class Workout:
    "This is a class to track workout data"
    def __init__(self):
        self.date = ''
        self.workoutType = ''
        self.weight = 0
        self.duration = 0
        today = date.today()
        self.date = today.strftime("%m/%d/%y")
        self.distance = 0
        self.duration = 0
        self.repetitions = 0

    #Get data of cardio workout and output to csv file
    def cardioDetails(self):
        self.workoutType = 'Cardio'
        self.distance = input("Please Enter the distance ran (in miles): ")
        self.time = input("Please Enter the duration (in minutes): ")
        with open('./workoutData/runworkout_data.csv', mode='a+') as csv_file:
                csv_reader = csv.writer(csv_file)
                csv_reader.writerow(['Date','Workout Type', 'Distance','Duration'])
                csv_reader.writerow([self.date,self.workoutType,self.distance,self.time])

    #Get data of pullup workout
    def pullupDetails(self):
        self.workoutType = 'Pullup'
        self.repetitions = input("Please Enter the number of pullups: ")
        with open('./workoutData/pullupworkout_data.csv', mode='a+') as csv_file:
                csv_reader = csv.writer(csv_file)
                csv_reader.writerow(['Date','Workout Type', 'Repetitions'])
                csv_reader.writerow([self.date,self.workoutType,self.repetitions])

    #Get data of pullup workout
    def pushupDetails(self):
        self.workoutType = 'Pushup'
        self.repetitions = input("Please Enter the number of pushups:")
        with open('./workoutData/pushupupworkout_data.csv', mode='a+') as csv_file:
                csv_reader = csv.writer(csv_file)
                csv_reader.writerow(['Date','Workout Type', 'Repetitions'])
                csv_reader.writerow([self.date,self.workoutType,self.repetitions])

    #Main Menu
    def menu(self):
        ans = True
        while ans:
            print("""
            1.Add a Workout
            2.See Historical Data
            """)
            ans=input("What would you like to do?")
            if ans == "1":
                self.workoutMenu()
            if ans == "2":
                "comeback"

    #Workout Type Menu
    def workoutMenu(self):
        ans = True
        while ans:
            print("""
            1.Cardio
            2.Pushups
            3.Pullups
            """)
            ans=input("What type of workout would you like to track?")
            if ans == "1":
                self.cardioDetails()
            if ans == "2":
                self.pushupDetails()
            if ans == "3":
                self.pullupDetails()
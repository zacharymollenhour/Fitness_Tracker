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

    #Function to get workout information
    def workoutData(self):
        today = date.today()
        self.date = today.strftime("%m/%d/%y")
        self.distance = 0
        self.duration = 0
        self.repetitions = 0
        self.updateWorkoutData()

    #Class that writes workout data to a csv
    def updateWorkoutData(self):
            with open('workout_data.csv', mode='a+',newline='') as csv_file:
                csv_reader = csv.writer(csv_file)
                csv_reader.writerow([self.date])
                csv_reader.writerow([self.workoutType])

    #Get data of cardio workout
    def cardioDetails(self):
        self.workoutType = 'Cardio'
        self.distance = input("Please Enter the distance ran:")
        self.time = input("Please Enter the duration (in minutes)")

    #Get data of pullup workout
    def pullupDetails(self):
        self.workoutType = 'pullup'
        self.repetitions = input("Please Enter the number of pullups:")

    #Get data of pullup workout
    def pushupDetails(self):
        self.workoutType = 'pushup'
        self.repetitions = input("Please Enter the number of pushups:")

    #Menu
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

    #Menu
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
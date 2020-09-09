import numpy as np 
import pandas as pd
import csv
from datetime import date

#Get User Name
class Person:
    "This is a persons data class"
    def __init__(self):
        self.userData = []
        self.name = ''
        self.age = 0
        self.weight = 0

    #Greet User for data about the individual
    def greet(self):

        #User Data
        self.name = input("Enter in your name: ")
        print(self.name)
        self.age = input("Enter in your age: ")
        print(self.age)
        self.weight = input("Enter in your weight: ")
        print(self.weight)

    #Write Inital Data of individual being tracked
    def updateCSV(self):
        with open('user_statistics.csv', mode='w') as csv_file:
            csv_reader = csv.writer(csv_file)
            csv_reader.writerow(self.name)
            csv_reader.writerow(self.age)
            csv_reader.writerow(self.weight)

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
        self.workoutType = input("Please enter the workout type:")
        print(self.workoutType)
        self.updateWorkoutData()

    #Class that writes workout data to a csv
    def updateWorkoutData(self):
            with open('workout_data.csv', mode='a+',newline='') as csv_file:
                csv_reader = csv.writer(csv_file)
                csv_reader.writerow([self.date])
                csv_reader.writerow([self.workoutType])
    #Menu
    def menu(self):
        ans = True
        while ans:
            print("""
            1.Add a Workout
            2.Delete a Workout
            """)
            ans=input("What would you like to do?")
            if ans == "1":
                self.workoutData()
            if ans == "2":
                "comeback"


#Main Function
def main():
    #Declare a object
    person1 = Person()
    workoutObject = Workout()

    #Call object functions
    """ person1.greet()
    person1.updateCSV() """
    workoutObject.menu()
    #workoutObject.workoutData()
    #workoutObject.updateWorkoutData()
main()
import numpy as np 
import pandas as pd
import csv


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
        self.name = input("Enter in your name: ")
        print(self.name)
        self.age = input("Enter in your age: ")
        print(self.age)
        self.weight = input("Enter in your weight: ")
        print(self.weight)

    #Write Inital Data of individual being tracked
    def updateCSV(self):
        with open('Fitness_Statistics.csv', mode='w') as csv_file:
            csv_reader = csv.writer(csv_file)
            csv_reader.writerow(self.name)
            csv_reader.writerow(self.age)
            csv_reader.writerow(self.weight)
#Main Function
def main():
    #Declare a object
    person1 = Person()

    #Call object functions
    person1.greet()
    person1.updateCSV()

main()
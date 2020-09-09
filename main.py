import numpy as np 
import pandas as pd
import csv


#Get User Name
class Person:
    "This is a persons data class"

    #Greet User for data about the individual
    def greet(self):
        name = input("Enter in your name: ")
        print(name)
        age = input("Enter in your age: ")
        print(age)
        weight = input("Enter in your weight: ")
        print(weight)

#Main Function
def main():
    person1 = Person()
    person1.greet()

main()
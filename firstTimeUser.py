#Class file for new user inititation
import csv

#Get User Name
class Person:

    "This is a persons data class"
    def __init__(self,name,age,weight,height,bmi,bicepsize,chestsize,shouldersize,backsize):
        self.userData = []
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.intro = "Thank you for using our workout tool. This Software allows you to track your workout data over a period of time and analyze the data for optimal results.This page is used to keep track of user health data."        
        self.bmi = bmi
        self.bicep = bicepsize
        self.chest = chestsize
        self.shoulder = shouldersize
        self.back = backsize

    #Write Inital Data of individual being tracked
    def updatereadMe(self):
        with open('./workoutData/user_readme.txt', mode='w+') as csv_file:
            csv_reader = csv.writer(csv_file)
            csv_reader.writerow(["Name","Age","Starting Weight","Height", "Starting BMI","Bicep","Chest","Shoulder","Back"])
            csv_reader.writerow([self.name,self.age,self.weight,self.height,self.bmi,self.bicep,self.chest,self.shoulder,self.back])

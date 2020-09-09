#Class file for new user inititation
import csv

#Get User Name
class Person:

    "This is a persons data class"
    def __init__(self,name,age,weight):
        self.userData = []
        self.name = name
        self.age = age
        self.weight = weight
        self.intro = "Thank you for using our workout tool. This Software allows you to track your workout data over a period of time and analyze the data for optimal results"
        self.instructions = "To achieve optimal workout results, utilize this tool for tracking your Cardio, Pushups and Pullups Data over any amount of time."


    #Write Inital Data of individual being tracked
    def updatereadMe(self):
        with open('./workoutData/user_readme.txt', mode='w+') as csv_file:
            csv_reader = csv.writer(csv_file)
            csv_reader.writerow([self.intro])
            csv_reader.writerow([self.instructions])
            """ csv_reader.writerow(self.name)
            csv_reader.writerow(self.age)
            csv_reader.writerow(self.weight) """
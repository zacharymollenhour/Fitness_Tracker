#Main File for creating a new person object
from firstTimeUser import Person


def main():

    #Prompt User for their information
    name = input("Enter in your name: ")
    age = input("Enter in your age: ")
    weight = input("Enter in your weight (in lbs): ")
    height = input("Enter in your height (in inches): ")
    bicepsize = input("Enter in your bicep size (in inches): ")
    chestsize = input("Enter in your chest size (in inches): ")
    shouldersize = input("Enter in your shoulder size (in inches): ")
    backsize = input("Enter in your back size (in inches): ")

    Weight = float(weight)
    Height = float(height)

    #BMI
    bmi = (((Weight)/(Height**2)) * 703)
    print(bmi)

    #Create a Object with data
    person = Person(name,age,weight,height,bmi,bicepsize,chestsize,shouldersize,backsize)

    #Push instructions and read me data to txt file
    person.updatereadMe()

main()
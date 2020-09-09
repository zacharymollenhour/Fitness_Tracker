#Main File for creating a new person object
from firstTimeUser import Person


def main():

    #Prompt User for their information
    name = input("Enter in your name: ")
    age = input("Enter in your age: ")
    weight = input("Enter in your weight: ")

    #Create a Object with data
    person = Person(name,age,weight)

    #Push instructions and read me data to txt file
    person.updatereadME()

main()
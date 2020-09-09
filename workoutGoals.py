



def main():
    days = []
    workoutGoal = {
        'Cardio': "1 mile",
        'Pushups': 100,
        "Pullups": 100
    }
    for i in range(30):
        tempVar = "Day " + str(i+1)
        days.append(tempVar)
        print('\n',tempVar)
        for key,value in workoutGoal.items():
            print(key,':',value)


main()
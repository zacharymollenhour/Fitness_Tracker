
from datetime import timedelta, date


def main():
    days = []
    workoutGoal = {
        'Cardio': "1 mile",
        'Pushups': 100,
        "Pullups": 100
    }

    for single_date in daterange(start_date, end_date):
        print(single_date.strftime("%Y-%m-%d"))
        tempVar = "Day " + single_date
        days.append(tempVar)
        print('\n',tempVar)
        for key,value in workoutGoal.items():
            print(key,':',value)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)

main()
from workoutDriver import Workout
import os

def main():
    #Output Title
    width = os.get_terminal_size().columns
    cstr = " Workout Tracker "
    print(cstr.center(40,'#'),'\n')

    #Create a workout object
    workout = Workout()

    #Call Menu Function
    val = workout.menu()

main()
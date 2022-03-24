# Main Program
# Project 1 Fitness Tracking
#
# Name: Joanna Chou
# Section: 07
# Date: 1/15/2022

from fitnessTrackerFuncs import *
def main():
    welcome()
    name = input_name()
    age = input_age()
    height = input_height()
    weight = input_weight()
    duration = input_duration()
    exercise_type = input_exercise_type()
    kg_weight = convert_lb_to_kg(weight)
    met_value = compute_MET(exercise_type)
    bmi = compute_BMI(weight, height)
    category = BMI_category(bmi)
    miles = compute_equivalent_miles(height, exercise_type, duration)
    calorie_burned = compute_calorie_burned(duration, kg_weight, met_value)

    print_info(name, age, height, weight, calorie_burned, bmi, category, miles)

    ans = input("Do you want to apply fitness tracking for another user (y/n)? \n")
    while ans == "y":
        welcome()
        name = input_name()
        age = input_age()
        height = input_height()
        weight = input_weight()
        duration = input_duration()
        exercise_type = input_exercise_type()
        kg_weight = convert_lb_to_kg(weight)
        met_value = compute_MET(exercise_type)
        bmi = compute_BMI(weight, height)
        category = BMI_category(bmi)
        miles = compute_equivalent_miles(height, exercise_type, duration)
        calorie_burned = compute_calorie_burned(duration, kg_weight, met_value)
        print_info(name, age, height, weight, calorie_burned, bmi, category, miles)
        
        ans = input("Do you want to apply fitness tracking for another user (y/n)? \n")


if __name__ == '__main__':
    main()



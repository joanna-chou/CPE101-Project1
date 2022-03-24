# Project 1 Fitness Tracking
#
# Name: Joanna Chou
# Section: 07
# Date: 1/15/2022

# purpose: This function prints a welcome statement and calls all of the other functions.
# signature: None -> None
def welcome():
    print(" Welcome to Fitness Tracker Application! \n")
    print("\tTo begin you must specify the participant's name, age, height (in inches),")
    print("\tweight (in lb), exercise duration (in minutes), and exercise type (1-4)!")
    print("\tNow you can compute the burned calories and BMI.")


# purpose: This function allows the user to enter their name.
# signature: str -> str
def input_name():
    name = input("Enter the name: ")
    return name
    
# purpose: This function allows the user to enter a valid age.
# signature: int -> int
def input_age():
    age = int(input("Enter age: "))
    while (age <= 0):
        print("Error: age must be an integer > 0!")
        age = int(input("Enter age: "))
    return age 
        
# purpose: This function allows the user to enter a valid height.
# signature: int -> int
def input_height():
    height = int(input("Enter height in inches: "))
    while (height <= 0):
        print("Error: height must be greater than 0!")
        height = int(input("Enter height: "))
    return height 

# purpose: This function allows the user to enter a valid weight.
# signature: int -> int
def input_weight():
    weight = int(input("Enter weight in lb: "))
    while (weight <= 0):
        print("Error: weight must be greater than 0!")
        weight = int(input("Enter weight in pounds: "))
    return weight 

# purpose: This function allows the user to enter a valid exercise duration.
# signature: int -> int
def input_duration():
    duration = int(input("Enter duration of exercise in minutes: "))
    while (duration <= 0):
        print("Error: duration must be greater than 0!")
        duration = int(input("Enter duration of exercise in minutes: "))
    return duration

# purpose: This function allows the user to choose one out of four exercise types.
# signature: int -> int
def input_exercise_type():
    exercise_type = int(input("Enter exercise type: 1) low-impact 2) high-impact  3) slow-paced  4) fast-paced "))
    while exercise_type > 4 or exercise_type < 1:
        print("Error: exercise type must be an integer between [1,4]!")
        exercise_type = int(input("Enter exercise type [1,4]: "))
    return exercise_type

# purpose: This function prints all of the information the user has entered in an orderly fashion.
# signature: None -> None
def print_info(name, age, height, weight, calorie_burned, bmi, category, miles):
    print("           Name :", name)
    print("            Age : ", age)
    print("         Height :  {:0.2f}".format(height), "inches")
    print("         Weight : {:0.2f}".format(weight), "lb")
    print("          Miles :   {:0.2f}".format(miles))
    print("Burned Calories : {:0.2f}".format(calorie_burned))
    print("            BMI :  {:0.2f}".format(bmi))
    print("   BMI Category :", category)

# purpose: This function takes the user's weight in pounds and converts it to kilograms.
# signature: int -> float
def convert_lb_to_kg(weight):
    kg_weight = weight * 0.45359237
    return kg_weight

# purpose: This function takes the activity code and returns the METs’ number as an integer number.
# signature: int -> int
def compute_MET(exercise_type):
    if exercise_type == 1:
        met_value = 5
    if exercise_type == 2:
        met_value = 7
    if exercise_type == 3:
        met_value = 3
    if exercise_type == 4:
        met_value = 4
    return met_value

# purpose: This function takes the user's duration in minutes, weight in (kg), and the MET value, and computes the number of calories burned.
# signature: int float int -> float
def compute_calorie_burned(duration, kg_weight, met_value):
    calorie_burned = duration * ((met_value * 3.5 * kg_weight)/200)
    return calorie_burned

# purpose: This function takes the user's weight and height and computes the BMI.
# signature: int int -> float
def compute_BMI(weight, height):
    bmi = 703 * weight / (height ** 2)
    return bmi

# purpose: This function categorizes the user's BMI into four categories.
# signature: int -> str
def BMI_category(bmi):
    if bmi < 18.59:
        category = "Underweight"
    if 18.59 <= bmi < 25:
        category = "Normal Weight"
    if 25 <= bmi < 30:
        category = "Over Weight"
    if bmi >= 30:
        category = "Obesity"
    return category

# purpose: This function takes height, the exercise type, and duration of the exercise to compute the number of miles.
# signature: int int int -> int
def compute_equivalent_miles(height, exercise_type, duration):
    if exercise_type == 1:
        steps_in_min = 120
    if exercise_type == 2:
        steps_in_min = 227
    if exercise_type == 3:
        steps_in_min = 100
    if exercise_type == 4:
        steps_in_min = 152
    num_steps = steps_in_min * duration
    step_distance = (0.413 * height)/12
    miles = (num_steps * step_distance)/5280
    return miles
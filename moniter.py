def check_health_status(gender):
    # define safe ranges for each parameter
    safe_ranges = {
        'age': (1, 120),
        'weight': (50, 250),
        'height': (1.5, 2.5),
        'oxygen_level': (90, 100),
        'blood_pressure': (90, 120),
        'blood_sugar': (70, 110),
        'body_temp': (97, 99),
        'pulse': (60, 100),
        'red_blood_cells': (4.0, 5.9) if gender == 'male' else (3.8, 5.2),
        'white_blood_cells': (3.5, 10.5),
        'platelets': (150, 450),
        'hemoglobin': (13.2, 16.6)if gender == 'male' else (11.6, 15),
        'glucose': (70, 110),
        'calcium': (8.5, 10.2),
        'sodium': (135, 145),
        'potassium': (3.6, 5.2),
        'bicarbonate': (22, 29),
        'chloride': (96, 106),
        'blood_urea_nitrogen': (6, 24),
        'creatinine': (0.74, 1.35)if gender == 'male' else (0.59,1.04),
    }
    # take user input for each parameter
    inputs = {}
    for param in safe_ranges.keys():
        try:
            inputs[param] = float(input(f'Enter {param}: '))
        except ValueError:
            print(f'Invalid input for {param}, it should be a number')
    # check if each parameter falls within its safe range
    for param, range in safe_ranges.items():
        if param in inputs:
            if range[0] <= inputs[param] <= range[1]:
                print(f'{param} is within safe range')
            else:
                print(f'{param} is NOT within safe range, it is {inputs[param] - range[0]} units out of range')
        else:
            print(f'No input provided for {param}')

# call the function with gender as an argument
gender=input("enter gender: ")
check_health_status(gender)

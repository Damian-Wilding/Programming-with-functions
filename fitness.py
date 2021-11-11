from datetime import datetime
def find_age(birth):
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birthday.year 
    if birthday.month > today.month or birthday.month == today.month and birthday.day >= today.day:
        age -= 1
    return age

def kilograms_from_pounds(pounds):
    kilograms = pounds * 0.453592
    return kilograms

def centimeters_from_inches(inches):
    centimeters = inches * 2.54
    return centimeters

def body_mass_index(weight, height):
    bmi = weight / height / height * 10000
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == 'f':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
        return bmr
    elif gender.lower() == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        return bmr
    else:
        return("bruh you didn't specify your gender correctly")


def main():
    gender = input('What is the gender? (enter "m" or "f"')
    birthday = input('When is your birthday? (Enter in YYYY-MM-DD format. Ex: 1999-03-18')
    pounds = float(input('What is your weight in pounds?'))
    height = float(input('What is your height in inches?'))
    age = find_age(birthday)
    print(f'Age (years): {age:.0f}')
    weight_in_kg = kilograms_from_pounds(pounds)
    print(f'Weight (kg): {weight_in_kg:.1f}')
    height_in_cm = centimeters_from_inches(height)
    print(f'Height (cm): {height_in_cm:.1f}')
    bmi = body_mass_index(weight_in_kg, height_in_cm)
    print(f'Body mass index: {bmi:.1f}')
    bmr = basal_metabolic_rate(gender, weight_in_kg, height_in_cm, age)
    print(f'Basal metabolic rate (kcal/day): {bmr:.0f}')

main()

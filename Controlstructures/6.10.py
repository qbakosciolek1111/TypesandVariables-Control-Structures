###
# Calculates a dog's age in dog's years
#

age = int(input("Enter the dog's age in human years: "))

if age < 0:
    print('Incorect age')
elif age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 21 + (age - 2) * 4

if age >= 0:
    print(f"The dog's age in dog's years is {dog_age:g} years.")

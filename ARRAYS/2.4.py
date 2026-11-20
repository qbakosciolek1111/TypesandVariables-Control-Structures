###
# Prints the weekly meal plan along with the day name
#
# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]  # typ: list zawierająca 7 elementów, a każdy z nich to list z 3 elementami typu str; to lista dwuwymiarowa: wiersz to dzień, kolumna to posiłek

# Returns a week day name
def weekday(n):  # funkcja własna; parametr n to int (numer dnia 1-7), zwraca str (nazwę dnia)
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]  # typ: list zawierająca elementy typu str
    return weekdays[n - 1]  # indeksy listy zaczynają się od 0, a numery dni od 1, więc odejmuję 1

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):  # funkcja własna; parametry: lista list (list) i numer dnia (int), zwraca str
    return ', '.join(meal_plan[day_number - 1])  # meal_plan[day_number - 1] to jeden wiersz (list z trzema str); join() to metoda napisu, która skleja elementy listy w jeden napis, wstawiając ', ' pomiędzy nimi

# Prints weekly meal plan
print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
for day_number in range(1, 8):  # range() to funkcja wbudowana; daje numery dni 1-7 (8 nie wchodzi do zakresu)
    print(f'{weekday(day_number)}: {day_meal_plan(meal_plan, day_number)}')  # f-string wstawia nazwę dnia (str) i posiłki (str) do jednej linii
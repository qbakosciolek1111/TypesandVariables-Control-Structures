###
# Finds which expense category was the most expensive
#
categories = ["Food", "Transport", "Rent", "Entertainment"]  # typ: list zawierająca elementy typu str (nazwy kategorii)
expenses = [500, 150, 1000, 200]  # typ: list zawierająca elementy typu int (kwoty); kwota na pozycji i należy do kategorii na tej samej pozycji i

max_expense = max(expenses)  # max() to funkcja wbudowana; zwraca największy element listy (typ int)
index = expenses.index(max_expense)  # index() to metoda listy; zwraca pozycję (int) pierwszego wystąpienia podanej wartości; ta pozycja pasuje też do listy categories, bo obie listy są ułożone w tej samej kolejności

print(f'The most expensive category: {categories[index]} ({max_expense})')  # categories[index] to element typu str; f-string wstawia str i int do napisu
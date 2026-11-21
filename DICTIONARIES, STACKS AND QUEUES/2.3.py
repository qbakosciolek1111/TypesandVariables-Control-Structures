all_students = {"Alice", "John", "Sara", "Bob"}  # zbiór wszystkich uczniów
attended_students = {"Alice", "Bob"}  # zbiór uczniów obecnych
absent_students = all_students - attended_students  # różnica zbiorów: uczniowie, których nie ma wśród obecnych
print(absent_students)  # wypisuje nieobecnych
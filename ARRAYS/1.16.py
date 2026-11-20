###
# Sorts data using the built-in sorted() function
#
# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]  # typ: list zawierająca elementy typu int
sorted_distances = sorted(distances_traveled)  # sorted() to funkcja wbudowana; zwraca NOWĄ posortowaną listę i nie zmienia oryginału; domyślnie sortuje rosnąco
print(sorted_distances)  # print() to funkcja wbudowana

# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]  # typ: list zawierająca elementy typu int
sorted_temperatures = sorted(daily_temperatures, reverse=True)  # reverse=True to parametr nazwany typu bool; odwraca kolejność, więc wynik jest malejący; wartości powtarzające się (np. dwa razy 18) zostają obie
print(sorted_temperatures)

# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]  # typ: list zawierająca elementy typu str (napisy)
sorted_file_names = sorted(file_names)  # napisy sortuje alfabetycznie, litera po literze; "photo" jest przed "presentation", bo drugą literą jest h, a h jest przed r
print(sorted_file_names)
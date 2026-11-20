###
# The weather station report
#
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]  # typ: list zawierająca 30 elementów typu int (temperatury w stopniach, także ujemne)

# number of measurements
measurements = len(temperatures)  # len() to funkcja wbudowana; zwraca liczbę elementów listy (typ int)

# calculates average temperature
temp_total = 0  # typ int; suma temperatur, zaczynam od 0
for temp in temperatures:  # pętla for bierze po kolei każdy element listy; temp w każdym obrocie jest typu int
    temp_total = temp_total + temp
avg_temp = temp_total / measurements  # operator / zawsze zwraca float (liczbę zmiennoprzecinkową), nawet gdy wynik byłby całkowity

# calculates min and max temperatures
min_temp = min(temperatures)  # min() to funkcja wbudowana; zwraca najmniejszy element listy
max_temp = max(temperatures)  # max() to funkcja wbudowana; zwraca największy element listy

# calculates number of days with negative temp
negative_temp = 0  # typ int; licznik dni z temperaturą poniżej zera
i = 0  # typ int; indeks, który w while trzeba ustawić ręcznie przed pętlą
while i < len(temperatures):  # pętla działa, dopóki indeks mieści się w liście (od 0 do 29)
    if temperatures[i] < 0:  # temperatures[i] to element typu int; zero nie jest ujemne, więc nie jest liczone
        negative_temp += 1
    i += 1  # bez zwiększania indeksu pętla zapętliłaby się w nieskończoność

# prints out month report
print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', measurements)
print('Average temperature in the month:', round(avg_temp, 2))  # round() to funkcja wbudowana; drugi argument 2 oznacza dwa miejsca po przecinku
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)
###
# Prints vehicle registration numbers from Krakow
#
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]  # typ: list zawierająca 12 elementów typu str (napisy)
counter = 1  # typ int; numer, który wypiszę przed następnym znalezionym numerem
for car_number in polish_license_plates:  # pętla for bierze po kolei każdy element listy; car_number w każdym obrocie jest typu str
    if car_number.startswith(('KR', 'KK')):  # startswith() to metoda napisów, zwraca bool (True/False); krotka ('KR', 'KK') w środku oznacza "zaczyna się od KR LUB od KK", więc nie trzeba pisać dwóch warunków z or
        print(counter, car_number)  # print() to funkcja wbudowana; wypisuje int i str
        counter += 1  # zwiększam numerację tylko przy trafieniu, dzięki czemu numery idą po kolei 1, 2, 3..., a nie według pozycji na liście
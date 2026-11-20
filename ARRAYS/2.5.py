###
# Cinema seating: counts seats and checks the status of a seat
#
# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]  # typ: list zawierająca 5 elementów, a każdy z nich to list z 5 elementami typu str ('A' lub 'B'); to lista dwuwymiarowa: wiersz to rząd w kinie, kolumna to miejsce w rzędzie

def seats_total(seats):  # funkcja własna; parametr to list list, zwraca int
    total = 0  # typ: int; licznik wszystkich miejsc
    for row in seats:  # pętla bierze po kolei każdy rząd; row jest typu list
        total += len(row)  # len() to funkcja wbudowana; zwraca liczbę miejsc w rzędzie (int), więc nie trzeba ręcznie liczyć każdego miejsca
    return total

def seats_available(seats):  # funkcja własna; zwraca int
    count = 0  # typ: int; licznik wolnych miejsc
    for row in seats:  # pętla zewnętrzna: po rzędach
        for seat in row:  # pętla wewnętrzna: po miejscach w rzędzie; seat jest typu str
            if seat == 'A':  # porównanie str z str zwraca bool; 'A' oznacza wolne miejsce
                count += 1
    return count

def seats_booked(seats):  # funkcja własna; zwraca int
    return seats_total(seats) - seats_available(seats)  # zajęte miejsca to wszystkie minus wolne, więc nie trzeba trzeciej pętli; funkcja korzysta z dwóch wcześniej zdefiniowanych

def seat_status(seats, row, place):  # funkcja własna; parametry: list list i dwa int (numery liczone od 1), zwraca str
    if seats[row - 1][place - 1] == 'A':  # seats[row - 1] to cały rząd (list), a [place - 1] to jedno miejsce w nim (str); odejmuję 1, bo numery rzędów i miejsc zaczynają się od 1, a indeksy od 0
        return 'available'
    return 'booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
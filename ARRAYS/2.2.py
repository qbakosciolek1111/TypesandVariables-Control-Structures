###
# Prints a Tic-Tac-Toe board
#
# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]  # typ: list zawierająca 3 elementy, a każdy z nich to też list z 3 elementami typu str (jedna litera lub spacja); to właśnie lista dwuwymiarowa, czyli lista list

for row in tic_tac_toe_board:  # pętla zewnętrzna bierze po kolei każdy wiersz; row w każdym obrocie jest typu list (np. ['X', 'O', 'X'])
    for cell in row:  # pętla wewnętrzna bierze po kolei każde pole wiersza; cell jest typu str
        print(cell, end=" ")  # print() to funkcja wbudowana; end=" " to parametr nazwany, który zamiast przejścia do nowej linii wypisuje spację, więc pola jednego wiersza stoją obok siebie
    print()  # pusty print() kończy bieżący wiersz i przechodzi do następnego
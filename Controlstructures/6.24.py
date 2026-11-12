###
# Prints a pattern of stars: growing from 1 to 5, then shrinking back to 1
#
for i in range(1, 6):  # pierwsza połowa: wiersze z 1, 2, 3, 4, 5 gwiazdkami; i to jednocześnie numer wiersza i liczba gwiazdek w nim
    print('* ' * i)  # mnożenie napisu przez liczbę powtarza go, np. '* ' * 3 daje '* * * '; dzięki temu nie trzeba pętli zagnieżdżonej

for i in range(4, 0, -1):  # druga połowa: 4, 3, 2, 1; trzeci argument -1 każe liczyć w dół, a 0 jest wyłączone z zakresu, więc kończy się na 1
    print('* ' * i)  # największy wiersz (5 gwiazdek) wypisał się już w pierwszej pętli, dlatego tu zaczynam od 4, a nie od 5
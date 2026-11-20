###
# Calculates monthly expenses by category, by week and in total
#
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]  # typ: list zawierająca 4 elementy, a każdy z nich to list z 3 elementami typu int; to lista dwuwymiarowa: wiersz to tydzień, kolumna to kategoria

# Calculates expenses
category_totals = [0, 0, 0]  # typ: list z trzema int; na pozycji 0 będzie suma jedzenia, na 1 transportu, na 2 opłat
week_totals = []  # typ: pusta list; dołożę do niej po jednej sumie na każdy tydzień
month_total = 0  # typ: int; suma całego miesiąca

for week in monthly_expenses:  # pętla zewnętrzna bierze po kolei każdy wiersz; week w każdym obrocie jest typu list (np. [200, 50, 100])
    week_sum = 0  # zerowanie sumy tygodnia na początku każdego tygodnia; bez tego sumy by się kumulowały
    for i in range(len(week)):  # len() to funkcja wbudowana (zwraca 3), range() daje indeksy 0-2; indeks jest potrzebny, żeby wiedzieć, do której kategorii dodać kwotę
        category_totals[i] += week[i]  # kwota z kolumny i trafia do sumy kategorii i, więc kolumny sumują się "w pionie"
        week_sum += week[i]  # ta sama kwota trafia też do sumy tygodnia, więc wiersze sumują się "w poziomie"
    week_totals.append(week_sum)  # append() to metoda listy; dopisuje element na koniec
    month_total += week_sum

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', month_total)
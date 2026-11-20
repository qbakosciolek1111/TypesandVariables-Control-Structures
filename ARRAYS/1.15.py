###
# Bubble sort
#
def bubble_sort(arr):  # funkcja własna; parametr arr to list z liczbami (int lub float), zwraca tę samą listę po posortowaniu
    n = len(arr)  # len() to funkcja wbudowana; zwraca liczbę elementów (int)
    for i in range(n):  # w szablonie było "for i in n", ale n to int, a pętla for potrzebuje czegoś, po czym można iterować, więc trzeba range(n)
        for j in range(n - i - 1):  # wewnętrzna pętla porównuje sąsiadów; n - i - 1, bo ostatnie i elementów jest już na swoich miejscach, a indeks j + 1 nie może wyjść poza listę
            if arr[j] > arr[j + 1]:  # lewy sąsiad większy od prawego, więc są w złej kolejności
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # zamiana miejscami w jednej linii; prawa strona jest liczona przed przypisaniem, więc nie trzeba zmiennej pomocniczej
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]  # typ: list zawierająca elementy typu float
print(car_fuel_consumption)  # print() to funkcja wbudowana
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)  # funkcja zwraca listę (list)
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]  # typ: list zawierająca elementy typu int (ujemne to wydatki, dodatnie wpływy)
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)
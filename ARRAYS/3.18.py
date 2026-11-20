###
# Functions that operate on an array of numbers (module MyArrays in one file)
# without the built-in max(), min(), sorted() and sum() functions
#
def sorted_copy(arr):  # funkcja pomocnicza własna; parametr to list, zwraca NOWĄ posortowaną list; nie ma jej w poleceniu, ale druga największa i mediana potrzebują uporządkowanych liczb
    result = arr[:]  # [:] to wycinek obejmujący całą listę, czyli kopia; dzięki niej sortowanie nie zmienia listy przekazanej do funkcji
    n = len(result)  # len() to funkcja wbudowana; zwraca liczbę elementów (int)
    for i in range(n):  # sortowanie bąbelkowe: każdy obrót zewnętrznej pętli wypycha jedną największą wartość na koniec
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:  # lewy sąsiad większy od prawego, więc są w złej kolejności
                result[j], result[j + 1] = result[j + 1], result[j]  # zamiana miejscami w jednej linii, bez zmiennej pomocniczej
    return result

def second_largest(arr):  # 1. funkcja własna; zwraca int (drugi największy element)
    ordered = sorted_copy(arr)  # w liście rosnącej druga największa wartość stoi na przedostatnim miejscu
    return ordered[len(ordered) - 2]  # indeks przedostatni liczę jako długość minus 2; przy powtórzeniach (np. [8, 8, 3]) powtórzona wartość liczy się osobno

def difference(arr):  # 2. funkcja własna; zwraca int (największa minus najmniejsza)
    smallest = arr[0]  # zaczynam od pierwszego elementu, a nie od 0, bo przy samych liczbach ujemnych zero byłoby błędnym rekordem
    largest = arr[0]
    for value in arr:  # pętla for bierze po kolei każdy element; value jest typu int
        if value > largest:
            largest = value
        if value < smallest:  # osobny if, a nie elif, bo każdą liczbę sprawdzam pod kątem obu rekordów
            smallest = value
    return largest - smallest

def median(arr):  # 3. funkcja własna; zwraca int albo float
    ordered = sorted_copy(arr)  # mediana to środkowa wartość w UPORZĄDKOWANYM ciągu, więc najpierw sortuję
    n = len(ordered)
    if n % 2 == 1:  # nieparzysta liczba elementów, więc jest jeden środkowy
        return ordered[n // 2]  # // to dzielenie całkowite: dla 5 elementów 5 // 2 daje indeks 2
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2  # parzysta liczba elementów, więc mediana to średnia dwóch środkowych; / zwraca float

def smallest_and_largest(arr):  # 4. funkcja własna; zwraca list z dwoma elementami [najmniejszy, największy]
    smallest = arr[0]
    largest = arr[0]
    for value in arr:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    return [smallest, largest]

def to_string(arr, separator):  # 5. funkcja własna; parametry: list i str, zwraca str; zamiast join() skleja elementy pętlą
    text = ''  # pusty napis na start
    for i in range(len(arr)):  # indeks jest potrzebny, żeby wiedzieć, który element jest pierwszy
        if i > 0:  # separator dopisuję PRZED każdym elementem poza pierwszym, żeby nie zostawał na początku ani na końcu
            text += separator
        text += str(arr[i])  # str() zamienia liczbę (int) na napis, bo inaczej Python nie dodałby liczby do napisu
    return text

numbers = [7, 3, 8, 5, 2]  # typ: list zawierająca 5 elementów typu int
print('Numbers:', to_string(numbers, ','))  # print() to funkcja wbudowana
print('Second largest number:', second_largest(numbers))
print('Difference between largest and smallest:', difference(numbers))
print('Median:', median(numbers))
print('Smallest and largest number:', to_string(smallest_and_largest(numbers), ','))
print('Numbers as a string:', to_string(numbers, '-'))
mobile = {  # tworzy słownik, czyli pary klucz: wartość
    "OS": "Android",  # system operacyjny (napis)
    "brand": "Samsung",  # marka (napis)
    "model": "Galaxy S23",  # model (napis)
    "screen_size": 6.1,  # przekątna ekranu w calach (liczba z ułamkiem)
    "memory_gb": 128,  # pamięć w GB (liczba całkowita)
    "5G": True  # czy telefon obsługuje 5G (wartość logiczna)
}
for key, value in mobile.items():  # items() daje kolejne pary, a pętla rozpakowuje je na klucz i wartość
    print(f"{key} : {value}")  # wypisuje klucz i wartość w jednej linii
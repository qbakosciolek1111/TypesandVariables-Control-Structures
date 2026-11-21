hotels_in_Krakow = [  # lista słowników: nazwa hotelu i cena
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(hotels):  # zwraca nazwy hoteli rozdzielone przecinkami
    names = []  # pusta lista na nazwy
    for hotel in hotels:  # bierze po kolei każdy hotel
        names.append(hotel["name"])  # dopisuje nazwę hotelu do listy
    return ','.join(names)  # skleja nazwy w jeden napis z przecinkami

def avg_price(hotels):  # zwraca średnią cenę pokoju zaokrągloną do liczby całkowitej
    total = 0  # suma cen, na start 0
    for hotel in hotels:  # bierze po kolei każdy hotel
        total += hotel["price"]  # dodaje cenę hotelu do sumy
    return round(total / len(hotels))  # dzieli sumę przez liczbę hoteli i zaokrągla

krakow_avg = avg_price(hotels_in_Krakow)  # liczy średnią dla Krakowa
sopot_avg = avg_price(hotels_in_Sopot)  # liczy średnią dla Sopotu
print('Hotels in Krakow:', hotel_list(hotels_in_Krakow))  # wypisuje hotele w Krakowie
print('Average hotel price in Krakow:', krakow_avg)  # wypisuje średnią cenę w Krakowie
print('Hotels in Sopot:', hotel_list(hotels_in_Sopot))  # wypisuje hotele w Sopocie
print('Average hotel price in Sopot:', sopot_avg)  # wypisuje średnią cenę w Sopocie
if krakow_avg < sopot_avg:  # porównuje średnie ceny
    print('Cheaper hotels in: Krakow')  # tańsze są hotele w Krakowie
elif sopot_avg < krakow_avg:
    print('Cheaper hotels in: Sopot')  # tańsze są hotele w Sopocie
else:
    print('Hotels cost the same in both cities')  # ceny są równe
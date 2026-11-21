import queue  # wczytuje moduł z kolejkami

customers = queue.Queue()  # kolejka numerków klientów (FIFO)
ticket_number = 0  # ostatnio wydany numerek

while True:  # pętla menu działa, dopóki nie przerwiesz jej przez break
    print('1. New customer')  # opcja: nowy klient
    print('2. Serve next customer')  # opcja: obsłuż następnego
    print('0. Quit')  # opcja: wyjście
    menu = input('Select an option: ')  # pobiera wybraną opcję

    if menu == '1':  # przyszedł nowy klient
        ticket_number += 1  # nadaje kolejny numerek
        customers.put(ticket_number)  # dodaje klienta na koniec kolejki
        print(f'Your ticket number is {ticket_number}')  # informuje klienta o numerku
    elif menu == '2':  # urzędnik chce obsłużyć następnego klienta
        if not customers.empty():  # sprawdza, czy ktoś czeka
            print(f'Now serving customer with ticket number {customers.get()}')  # zdejmuje klienta z początku kolejki
        else:
            print('No customers waiting.')  # nikt nie czeka
    elif menu == '0':  # użytkownik chce wyjść
        break  # kończy program
###
# Checks the PIN code entered in a payment terminal;
# the card is blocked after three unsuccessful attempts
#
correct_pin = '0805'  # PIN jako tekst, a nie liczba: int() zgubiłby zero z początku (0805 zmieniłoby się w 805) i nigdy nie pasowałby do wpisanego kodu
attempts = 0  # licznik nieudanych prób
pin_ok = False  # flaga: czy użytkownik podał poprawny PIN; po pętli na jej podstawie decyduję, co wypisać

while attempts < 3 and not pin_ok:  # pętla działa, dopóki zostały próby ORAZ PIN nie został jeszcze zgadnięty; obie części są potrzebne, żeby pętla zatrzymała się w obu sytuacjach
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == correct_pin:
        pin_ok = True  # ustawienie flagi kończy pętlę przy następnym sprawdzeniu warunku
    else:
        attempts += 1  # licznik zwiększam tylko przy błędnym PIN-ie
        print('Incorrect...')

if pin_ok:  # po pętli sprawdzam, dlaczego się skończyła: trafieniem czy wyczerpaniem prób
    print('PIN code correct. Payment accepted.')
else:
    print('Sorry, your payment card has been blocked.')
###
# Returns time as a string in 24-hour or 12-hour format
#
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'  # :02d dopisuje zero z przodu do dwóch cyfr, więc 8 godzin i 3 minuty dają '08:03', a nie '8:3'
    else:
        if hours >= 12:  # od 12:00 do 23:59 jest po południu, więc pm
            suffix = 'pm'
        else:
            suffix = 'am'
        hours_12 = hours % 12  # reszta z dzielenia przez 12 sprowadza 13-23 do 1-11, np. 19 % 12 = 7
        if hours_12 == 0:  # 0 i 12 dają resztę 0, a w formacie 12-godzinnym mają się wypisać jako 12 (północ i południe)
            hours_12 = 12
        return f'{hours_12}:{minutes:02d}{suffix}'  # godzina bez zera z przodu (7:30am), a minuty zawsze z zerem (7:02pm)

# Reads time from the keyboard and prints it in the chosen format
hours = int(input('Enter hours (0..23): '))  # int(), bo input() zwraca tekst, a funkcja liczy na liczbach
minutes = int(input('Enter minutes (0..59): '))
time_format = input('Enter format (12 or 24): ')  # zostaje tekstem, bo funkcja porównuje z napisami '24' i '12'

print('Time:', time_string(hours, minutes, time_format))
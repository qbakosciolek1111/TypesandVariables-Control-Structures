import queue  # wczytuje moduł z kolejkami

# creates a queue of files to print
files_to_print = queue.Queue()  # tworzy zwykłą kolejkę (FIFO), czyli pierwszy dodany plik jest drukowany pierwszy

while True:  # pętla menu działa, dopóki nie przerwiesz jej przez break
   print('1. Add file to print')  # wypisuje opcję dodania pliku
   print('2. Print file')  # wypisuje opcję drukowania pliku
   print('0. Quit')  # wypisuje opcję wyjścia
   menu = input('Select an option: ')  # pobiera wybraną opcję jako tekst

   if menu == '1':  # użytkownik chce dodać plik
      file_name = input('Enter file name to print: ')  # pobiera nazwę pliku
      files_to_print.put(file_name)  # dodaje plik na koniec kolejki

   elif menu == '2':  # użytkownik chce drukować
      if not files_to_print.empty():  # sprawdza, czy w kolejce jest jakiś plik
         file_to_print = files_to_print.get()  # zdejmuje plik z początku kolejki
         print(f'File {file_to_print} is currently being printed. Please wait!')  # informuje, który plik jest drukowany
      else:
         print('There are no files in the print queue.')  # informuje, że kolejka jest pusta

   elif menu == '0':  # użytkownik chce wyjść
      break  # przerywa pętlę i kończy program
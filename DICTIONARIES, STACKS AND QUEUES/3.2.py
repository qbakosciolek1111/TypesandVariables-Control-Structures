import queue  # wczytuje moduł z kolejkami i stosami

# create a visited_websites
visited_websites = queue.LifoQueue()  # tworzy stos (LIFO), czyli ostatnio dodany element wychodzi pierwszy

# some previously visited websites
visited_websites.put('instagram.com')  # kładzie stronę na stos
visited_websites.put('uek.krakow.pl')  # kładzie kolejną stronę na stos
visited_websites.put('microsoft.com')  # ta strona jest na wierzchu stosu

current = None  # strona, którą teraz oglądasz; na początku jeszcze żadnej

while True:  # pętla działa, dopóki nie przerwiesz jej przez break
   website = input('Enter website name (0 for back): ')  # pobiera nazwę strony albo 0

   if website == '0':  # użytkownik chce wrócić
      if visited_websites.empty():  # sprawdza, czy na stosie nie ma już żadnej strony
         break  # nie ma dokąd wracać, więc kończy program
      else:
         print('<-- Going back to a previously visited website')  # informuje o powrocie
         website = visited_websites.get()  # zdejmuje stronę z wierzchu stosu i zapisuje ją jako oglądaną
         current = website  # zapamiętuje, że teraz oglądasz tę stronę
   elif website != "":  # użytkownik wpisał nową stronę (pusty tekst jest pomijany)
      if current is not None:  # jeśli już coś oglądałeś
         visited_websites.put(current)  # kładzie na stos stronę, którą opuszczasz, żeby dało się do niej wrócić
      current = website  # nowa strona staje się oglądaną
   else:  # pusty tekst
      continue  # wraca na początek pętli bez wypisywania

   # print name of website you are currently viewing
   print('You are currently viewing:', website)  # wypisuje stronę, którą oglądasz
   print()  # wypisuje pustą linię
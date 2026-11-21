emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}  # zbiór otrzymanych adresów
spam_list = {"spam1@example.com", "spam2@example.com"}  # zbiór adresów ze spamu
spam_emails = emails_received & spam_list  # część wspólna zbiorów: adresy, które są w obu
print("Spam emails:", spam_emails)  # wypisuje znalezione adresy spamu
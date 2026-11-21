contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}  # pierwsza lista kontaktów
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}  # druga lista kontaktów
merged_contacts = contacts_A | contacts_B  # suma zbiorów: wszystkie adresy bez powtórzeń
print("Merged contacts:", merged_contacts)  # wypisuje połączoną listę
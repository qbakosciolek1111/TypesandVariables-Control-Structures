import json


def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']


def count_rooms(reservations):
    # a set keeps only unique room numbers
    return len({r['room_number'] for r in reservations})


def count_by_payment(reservations, paid):
    return sum(1 for r in reservations if r['paid'] == paid)


def total_value(reservations, paid):
    return sum(r['nights'] * r['price_per_night']
               for r in reservations if r['paid'] == paid)


reservations = load_reservations('reservations.json')

print(f"Number of rooms: {count_rooms(reservations)}")
print(f"Paid reservations: {count_by_payment(reservations, True)}")
print(f"Unpaid reservations: {count_by_payment(reservations, False)}")
print(f"Total value of paid reservations: {total_value(reservations, True):.2f}")
print(f"Total value of unpaid reservations: {total_value(reservations, False):.2f}")
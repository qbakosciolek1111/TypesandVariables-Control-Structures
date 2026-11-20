def f(binary_number):
    if binary_number == "":
        return False
    for char in binary_number:
        if char != '0' and char != '1':
            return False
    return True

print(f("101101"))   #True
print(f("1311a10100"))   #False
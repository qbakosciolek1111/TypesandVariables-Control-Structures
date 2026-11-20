def f(amount_to_pay):
    coins_5 = amount_to_pay //5
    rest = amount_to_pay % 5
    coins_2 = rest // 2
    coins_1 = rest % 2
    return coins_5 + coins_2 + coins_1

print(f(23)) 
print(f(8))
print(f(2))
print(f(0))

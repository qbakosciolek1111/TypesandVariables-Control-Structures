###
# To use the functions available in an external module,
# you must include that module in your program.
import math

square_root = math.sqrt(7)  # funkcje z modułu wywołuję z przedrostkiem math., bo sam import nie wprowadza ich do programu pod krótką nazwą
print('A square root of 7 is', square_root)

logarithm = math.log(5)  # math.log() bez drugiego argumentu liczy logarytm NATURALNY (przy podstawie e), a nie dziesiętny; dziesiętny to math.log10()
print('A natural logarithm of 5 is', logarithm)

sine = math.sin(math.radians(90))  # math.sin() przyjmuje kąt w RADIANACH, a nie w stopniach; math.sin(90) dałoby 0.89..., czyli zły wynik, więc najpierw zamieniam 90° na radiany funkcją math.radians()
print('The sine of 90 degrees is', sine)
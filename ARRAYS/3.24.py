###
# Draws a line in a diagram from position (1, 3) to position (8, 10)
#
import subprocess  # moduł wbudowany w Pythona; pozwala uruchomić polecenie systemowe z poziomu programu
import sys  # sys.executable to ścieżka do DOKŁADNIE tego Pythona, który uruchamia program, więc biblioteka zainstaluje się we właściwym miejscu

try:
    import matplotlib.pyplot as plt  # próbuję zaimportować bibliotekę
except ModuleNotFoundError:  # jeśli jej nie ma, Python zgłasza ten błąd, a try/except pozwala go przechwycić zamiast przerwać program
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])  # instaluje bibliotekę tak samo jak polecenie python -m pip install matplotlib
    import matplotlib.pyplot as plt  # po instalacji importuję jeszcze raz

xpoints = [1, 8]  # współrzędne x początku i końca linii
ypoints = [3, 10]  # współrzędne y początku i końca linii

plt.plot(xpoints, ypoints)  # rysuje linię przez punkty (1, 3) i (8, 10)
plt.show()  # otwiera okno z wykresem
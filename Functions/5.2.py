def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    return n / 2.54  # 1 cal to dokładnie 2,54 cm, więc centymetry dzielę przez 2,54

def feet_inches_to_cm(feet, inches):
    return (feet * 12 + inches) * 2.54  # 1 stopa to 12 cali, więc najpierw zamieniam wszystko na cale, a dopiero potem na centymetry

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'254cm = {cm_to_inches(254)}in')
    print(f'6ft 0in = {feet_inches_to_cm(6, 0)}cm')
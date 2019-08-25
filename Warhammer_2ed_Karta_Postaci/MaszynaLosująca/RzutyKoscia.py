import random


def rzuc_koscia_10(self=1):
    wysokosc_rzutu = 0
    for licz_kosci in range(0, self):
        wysokosc_rzutu += random.randint(1, 10)
    return wysokosc_rzutu


def rzuc_koscia_100(self=1):
    wysokosc_rzutu = 0
    for licz_kosci in range(0, self):
        wysokosc_rzutu += random.randint(1, 100)
    return wysokosc_rzutu


def rzuc_koscia_wieloscienna(wybrana_ilosc_scianek=None, self=1):
    wysokosc_rzutu = 0
    for licz_kosci in range(0, self):
        wysokosc_rzutu += random.randint(1, wybrana_ilosc_scianek)
    return wysokosc_rzutu

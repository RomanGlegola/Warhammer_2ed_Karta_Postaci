from Warhammer_2ed_Karta_Postaci.MaszynaLosująca import RzutyKoscia
from Warhammer_2ed_Karta_Postaci.Postać import Kalendarium, \
    Imiona, \
    Nazwiska

Kalendarz = Kalendarium.Kalendarium

print(f"Imię i nazwisko: {Imiona.wybierz_imie_czlowiek_mezczyzna()} {Nazwiska.nazwisko_czlowiek()} \n"
      f"Znak Gwiezdny: {Kalendarz.znak_gwiezdny()[0]} - {Kalendarz.znak_gwiezdny()[1]}\n"
      f"Data urodzenia: {Kalendarz.data_urodzenia_postaci()[1]} roku Sigmara \n"
      f"\t\t\t\t{Kalendarz.data_urodzenia_miesieczna()[0]} {Kalendarz.data_urodzenia_miesieczna()[1]}")

cechy_glowne = {
    1: ["Walka Wręcz", RzutyKoscia.rzuc_koscia_10(2) + 20],
    2: ["Umiejętności Strzeleckie", RzutyKoscia.rzuc_koscia_10(2) + 20],
    3: ["Krzepa", RzutyKoscia.rzuc_koscia_10(2) + 20],
    4: ["Odporność", RzutyKoscia.rzuc_koscia_10(2) + 20],
    5: ["Zręczność", RzutyKoscia.rzuc_koscia_10(2) + 20],
    6: ["Inteligencja", RzutyKoscia.rzuc_koscia_10(2) + 20],
    7: ["Siła Woli", RzutyKoscia.rzuc_koscia_10(2) + 20],
    8: ["Ogłada", RzutyKoscia.rzuc_koscia_10(2) + 20]
}

drugorzedne = lambda x: int(x / 10)

cechy_drugorzedne = {
    1: ["Atak", 1],
    2: ["Żywotność", "PlaceHolder"],
    3: ["Siła", drugorzedne(cechy_glowne[3][1])],
    4: ["Wytrzymałość", drugorzedne(cechy_glowne[4][1])],
    5: ["Szybkość", "PlaceHolder"],
    6: ["Magia", "PlaceHolder"],
    7: ["Punkty Obłędu", "PlaceHolder"],
    8: ["Punkty Przeznaczenia", "PlaceHolder"]
}
print(f"{cechy_glowne[1]} \t\t\t {cechy_drugorzedne[1]}")
print(f"{cechy_glowne[2]} {cechy_drugorzedne[2]}")
print(f"{cechy_glowne[3]} \t\t\t\t\t {cechy_drugorzedne[3]}")
print(f"{cechy_glowne[4]} \t\t\t\t {cechy_drugorzedne[4]}")
print(f"{cechy_glowne[5]} \t\t\t\t {cechy_drugorzedne[5]}")
print(f"{cechy_glowne[6]} \t\t\t {cechy_drugorzedne[6]}")
print(f"{cechy_glowne[7]} \t\t\t\t {cechy_drugorzedne[7]}")
print(f"{cechy_glowne[8]} \t\t\t\t\t {cechy_drugorzedne[8]}")

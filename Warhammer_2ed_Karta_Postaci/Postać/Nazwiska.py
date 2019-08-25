from Warhammer_2ed_Karta_Postaci.MaszynaLosująca import RzutyKoscia

"""
aby wylosować nazwisko czlowieka wpisz:
    nazwisko_czlowiek()
    
aby wylosowac nazwisko elfa wpisz:
    nazwisko_elf_mezczyzna()
lub
    nazwisko_elf_kobieta()
    
aby wylosowac nazwisko krasnoluda wpisz:
    nazwisko_krasnolud_mezczyzna()
lub
    nazwisko_krasnolud_kobieta()
    
aby wylosowac nazwisko niziolka wpisz:
    nazwisko_niziolek()
"""

def nazwisko_czlowiek(self=RzutyKoscia.rzuc_koscia_100()):
    nazwisko = ["początek listy", "Adelhof", "Albrecht", "Allenstag", "Altmann", "Atzwig", "Bacher", "Baer",
                "Baumann", "Becker", "Behn", "Betz", "Beyer", "Bischof", "Boehm", "Brietenbach", "Breuer",
                "Dahmbach", "Delfholt", "Drakenhof", "Drauwulf", "Durrbein", "Ehrhard", "Eisenhauer",
                "Eschlimann", "Falkenheim", "Fehr", "Fiegler", "Feischer", "Frohlich", "Frueh", "Fuchs",
                "Gaffwig", "Gaertner", "Gebauer", "Godtgraf", "Grunenwald", "Guth", "Haintz", "Herz",
                "Herzog", "Hirtzel", "Hoch", "Hoefer", "Hofstetter", "Jaeger", "Jochutz", "Jutzenbach",
                "Kalb", "Kaltenbach", "Kraemer", "Krebs", "Kuhn", "Kummel", "Konig", "Konigsamen",
                "Fang", "Lankdorf", "Liess", "Lebengut", "Lutzen", "Manholt", "Meusmann", "Meyer", "Mohr",
                "Muller", "Nachtmann", "Naubhof", "Netzhoch", "Neumann", "Niederlitz", "Nuhr", "Oberholtzer",
                "Ohrsten", "Otzlowe", "Reichert", "Reifsneider", "Riese", "Rohrig", "Reiss", "Schaffer",
                "Schaumer", "Scherer", "Schultz", "Schleiermacher", "Schreiber", "Schwalb", "Steiner",
                "Tabbeck", "Teuber", "Tolzen", "Trachsel", "Weber", "Wechsler", "Wirtz", "Widmann", "Widmer",
                "Veit", "Vogt", "Vogel", "Zumwald"]
    return nazwisko[self]


def nazwisko_elf_mezczyzna(self=RzutyKoscia.rzuc_koscia_100()):
    nazwisko = ["początek listy", "Białowłosy", "Błękit Pióry", "Błękit Skrzydły", "Błysk Klingi",
                "Błysk Pioruna", "Błysk Stali", "Bystrooki", "Ciemnowłosy", "Cienista Dolina",
                "Czarne Drzewo", "Czarny Kurhan", "Czysty Zdrój", "Dech Lasu", "Dębowy Konar",
                "Dotyk Nocy", "Dzikie Serce", "Gwiazda Wieczorna", "Gwiazda Zaranna",
                "Gwiezdne Oko", "Gwiezdny Ogień", "Gwiezdny Pył", "Jasna Gwiazda", "Jasnooki",
                "Jastrzębie Oko", "Jaśniejący", "Jeleni Skok", "Kieł Wilka", "Korona Słońca",
                "Krzyk Puchacza", "Księżycowy Blask", "Księżycowy Mrok", "Kwiat Młodości",
                "Lot Sokoła", "Lśniąca Góra", "Lśniący Grot", "Lśniący Księżyc", "Mądre Serce",
                "Mądrość Klanu", "Mężne Serce", "Młody Liść", "Moc Dębu", "Moc Korzeni",
                "Moc Różdżki", "Morska Fala", "Morska Piana", "Mroczne Ostrze", "Nocny Łowca",
                "Oko Wilka", "Oko Wizji", "Oko Zieleni", "Opadający Liść", "Opoka Siły",
                "Orzeł Mroku", "Ostre Ostrze", "Ostry Grot", "Pajęcza Nić", "Patrzący w Dal",
                "Podmuch Wichury", "Poranna Rosa", "Półksiężyc", "Promyk Słońca",
                "Przyjaciel Zwierząt", "Radosne Serce", "Różany Kwiat", "Ryk Burzy", "Silnoręki",
                "Smoczy Brat", "Smukłe Ostrze", "Smukły Grot", "Spokój Fal", "Spokój Kamienia",
                "Spokój Lasu", "Srebrnowłosy", "Srebrny Liść", "Srebrny Świt", "Strzała Mocy",
                "Szybki Grot", "Szybkie Ostrze", "Śnieżny Puch", "Śpiew Dzikości", "Śpiew Wiatru",
                "Ukryty w Cieniu", "Uśmiech Wiatru", "Wartki Strumyk", "Wędrowiec", "Wiatr Wśród Traw",
                "Wiatroskrzydły", "Wieża Mądrości", "Wodny Wir", "Wschodzące Słońce", "Wszechwidzący",
                "Wyniosły Dąb", "Wysoki Brzeg", "Zachodzące Słońce", "Zieleń Pióra", "Zieleń Skrzydły",
                "Zielona Dolina", "Złocisty Obłok", "Złota Struga", "Złotowłosy"]
    return nazwisko[self]


def nazwisko_elf_kobieta(self=RzutyKoscia.rzuc_koscia_100()):
    nazwisko = ["początek listy", "Białowłosa", "Błękit Pióra", "Błękit Skrzydła", "Błysk Klingi",
                "Błysk Pioruna", "Błysk Stali", "Bystrooka", "Ciemnowłosa", "Cienista Dolina",
                "Czarne Drzewo", "Czarny Kurhan", "Czysty Zdrój", "Dech Lasu", "Dębowy Konar",
                "Dotyk Nocy", "Dzikie Serce", "Gwiazda Wieczorna", "Gwiazda Zaranna", "Gwiezdne Oko",
                "Gwiezdny Ogień", "Gwiezdny Pył", "Jasna Gwiazda", "Jasnooka", "Jastrzębie Oko",
                "Jaśniejąca", "Jeleni Skok", "Kieł Wilka", "Korona Słońca", "Krzyk Puchacza",
                "Księżycowy Blask", "Księżycowy Mrok", "Kwiat Młodości", "Lot Sokoła", "Lśniąca Góra",
                "Lśniący Grot", "Lśniący Księżyc", "Mądre Serce", "Mądrość Klanu", "Mężne Serce",
                "Młody Liść", "Moc Dębu", "Moc Korzeni", "Moc Różdżki", "Morska Fala", "Morska Piana",
                "Mroczne Ostrze", "Nocna Łowczyni", "Oko Wilka", "Oko Wizji", "Oko Zieleni",
                "Opadający Liść", "Opoka Siły", "Orzeł Mroku", "Ostre Ostrze", "Ostry Grot",
                "Pajęcza Nić", "Patrząca w Dal", "Podmuch Wichury", "Poranna Rosa", "Półksiężyc",
                "Promyk Słońca", "Przyjaciółka Zwierząt", "Radosne Serce", "Różany Kwiat", "Ryk Burzy",
                "Silnoręka", "Smocza Siostra", "Smukłe Ostrze", "Smukły Grot", "Spokój Fal",
                "Spokój Kamienia", "Spokój Lasu", "Srebrnowłosa", "Srebrny Liść", "Srebrny Świt",
                "Strzała Mocy", "Szybki Grot", "Szybkie Ostrze", "Śnieżny Puch", "Śpiew Dzikości",
                "Śpiew Wiatru", "Ukryty w Cieniu", "Uśmiech Wiatru", "Wartki Strumyk", "Wędrowiec",
                "Wiatr Wśród Traw", "Wiatroskrzydła", "Wieża Mądrości", "Wodny Wir", "Wschodzące Słońce",
                "Wszechwidząca", "Wyniosły Dąb", "Wysoki Brzeg", "Zachodzące Słońce", "Zieleń Pióra",
                "Zieleń Skrzydła", "Zielona Dolina", "Złocisty Obłok", "Złota Struga", "Złotowłosa"]

    return nazwisko[self]


def nazwisko_krasnolud_mezczyzna():
    from Warhammer_2ed_Karta_Postaci.Postać import Imiona
    return Imiona.wybierz_imie_krasnolud_mezczyzna() + "son"


def nazwisko_krasnolud_kobieta():
    from Warhammer_2ed_Karta_Postaci.Postać import Imiona
    return Imiona.wybierz_imie_krasnolud_kobieta() + "sdotr"


def nazwisko_niziolek(self=RzutyKoscia.rzuc_koscia_100()):
    nazwisko = ["początek listy", "Altannik", "Badylarz", "Beczułka", "Bielinek", "Brzeżek",
                "Brzuchacz", "Byliniak", "Cichobieg", "Cierniak", "Długonos", "Długouch",
                "Drapal", "Drewniak", "Dudziarz", "Dziwaczek", "Figlarz", "Futrzak", "Glistnik",
                "Głuptak", "Groszek", "Drzechotek", "Grzywacz", "Gwizdawek", "Iglarz", "Jabłecznik",
                "Jagódka", "Jaskółka", "Kaczeniec", "Kasztanek", "Kędziorek", "Kociak", "Kociołek",
                "Kogut", "Kolcownik", "Koniczynka", "Koralik", "Kosturek", "Kotlarz", "Kret",
                "Kręciołek", "Kruczek", "Krupnik", "Kulawik", "Kwietniak", "Łazik", "Łąkołaz",
                "Łodyżek", "Marudniak", "Mieszek", "Młynek", "Morwa", "Mroczek", "Niemysł",
                "Okruszek", "Opijus", "Otoczak", "Owsianniak", "Pagórek", "Paluch", "Piaszczak",
                "Piwniak", "Piwosz", "Podpłomyk", "Popiołek", "Przebiśnieg", "Radośnik", "Robaczek",
                "Rogaś", "Ryjek", "Rzęsiawik", "Sknerus", "Skoblik", "Skórniak", "Słomnik", "Stoczek",
                "Stopowiąz", "Stopowłaz", "Sucharek", "Szarak", "Szarlotek", "Śnieżynka", "Trzęsiawiec",
                "Warkoczyk", "Wąsacz", "Wąwoźnik", "Wesołek", "Węgielek", "Wiatrownik", "Wierzbek",
                "Wietrzyk", "Wilczomlecz", "Wilkowyj", "Wodniak", "Wstążka", "Zagórnik", "Zawijas",
                "Zieleniak", "Złocisz", "Żarnik", "Żniwiarz"]
    return nazwisko[self]

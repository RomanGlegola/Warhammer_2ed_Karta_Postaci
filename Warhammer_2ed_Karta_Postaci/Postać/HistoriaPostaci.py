from Warhammer_2ed_Karta_Postaci.MaszynaLosująca import RzutyKoscia


def liczba_rodzenstwa(self=RzutyKoscia.rzuc_koscia_10()):
    if 1 == self:
        return 1
    elif 2 <= self <= 3:
        return 2
    elif 4 <= self <= 5:
        return 3
    elif 6 <= self <= 7:
        return 4
    elif 8 <= self <= 9:
        return 5
    elif 10 == self:
        return 6


def wrozba_losu(self=RzutyKoscia.rzuc_koscia_100()):
    if 1 <= self <= 3:
        return "Zguba twa nadejdzie w mroku."
    elif 4 <= self <= 6:
        return "Strzeż się zwierza z pól. I czerwonej bestii."
    elif 7 <= self <= 9:
        return "Słowo pisane twą zgubę przypieczętuje."
    elif 10 <= self <= 12:
        return "Umrzesz gdy tchu ci zabraknie."
    elif 13 == self:
        return "Trzy razy po trzy razy i raz jeszcze trzy - to znak twojej śmierci."
    elif 14 <= self <= 16:
        return "Duszę twą pożre Bestia Mosiężna."
    elif 17 <= self <= 22:
        return "W strawie swej ptaka nie ujrzysz ani ryby ościstej."
    elif 23 <= self <= 28:
        return "Zemsta bogów dosięgnie cię!"
    elif 29 <= self <= 34:
        return "W łożu umrzesz choć nie swoim."
    elif 35 <= self <= 38:
        return "Blask Morrslieba poprowadzi cię do bram umarłych."
    elif 39 <= self <= 44:
        return "Zgubą twą woda będzie. Strzeż się wody!"
    elif 45 <= self <= 85:
        return "Dobroć twoja złem podszyta. Męstwo twe to śmiech głupca."
    elif 49 <= self <= 53:
        return "Nie wachaj się, by tajemnicę na skraju przepaści poznać."
    elif 54 <= self <= 58:
        return "Zguba twa z góry na cię spadnie."
    elif 59 <= self <= 65:
        return "Ciało twe pożre mroczny pomór."
    elif 66 <= self <= 68:
        return "Kres wieszczą płomienie przed okiem ukryte."
    elif 69 <= self <= 72:
        return "Duma twym losem. Próżność kresem."
    elif 73 <= self <= 75:
        return "I spożywać będziesz jadło z misy zepsucia."
    elif 76 <= self <= 78:
        return "Losem twym zaćmiony wzrok."
    elif 79 <= self <= 85:
        return "Kto mieczem wojuje, po ostrzu jego krew spłynie."
    elif 86 <= self <= 88:
        return "Umrzesz po trzykroć przeklęty."
    elif 89 <= self <= 92:
        return "Srebrne ostrze powita cię na progu śmierci."
    elif 93 <= self <= 95:
        return "Strzeż się zieleni..."
    elif 96 <= self <= 97:
        return "Nie zaznasz łaski Ranalda."
    elif 98 <= self <= 99:
        return "Czas poznasz gdy posłańca Morra dojrzysz."
    elif 100 == self:
        return "Bogowie skrywają swe zamiary wobec ciebie."


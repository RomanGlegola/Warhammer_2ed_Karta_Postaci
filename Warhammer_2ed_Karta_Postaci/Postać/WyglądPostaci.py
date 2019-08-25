from Warhammer_2ed_Karta_Postaci.MaszynaLosująca import RzutyKoscia


class WygladPostaci:

    def waga(self=RzutyKoscia.rzuc_koscia_wieloscienna(12)):
        if self == 1:
            return 1
        elif 2 <= self <= 10:
            return 2
        elif 11 <= self <= 20:
            return 3
        elif 21 <= self <= 30:
            return 4
        elif 31 <= self <= 40:
            return 5
        elif 41 <= self <= 50:
            return 6
        elif 51 <= self <= 60:
            return 7
        elif 61 <= self <= 70:
            return 8
        elif 71 <= self <= 80:
            return 9
        elif 81 <= self <= 90:
            return 10
        elif 91 <= self <= 99:
            return 11
        elif 100 == self:
            return 12

    def wiek(self=RzutyKoscia.rzuc_koscia_wieloscienna(20)):
        return self

    def wzrost(self=RzutyKoscia.rzuc_koscia_10(2)):
        return self

    def kolor_wlosow(self=RzutyKoscia.rzuc_koscia_10()):
        return self

    def kolor_oczu(self=RzutyKoscia.rzuc_koscia_10()):
        return self

    def znaki_szczegolne(self=RzutyKoscia.rzuc_koscia_100()):
        if 1 <= self <= 5:
            return 1
        elif 6 <= self <= 10:
            return 2
        elif 11 <= self <= 15:
            return 3
        elif 16 <= self <= 20:
            return 4
        elif 21 <= self <= 25:
            return 5
        elif 26 <= self <= 29:
            return 6
        elif 35 <= self <= 35:
            return 7
        elif 36 <= self <= 39:
            return 8
        elif 40 <= self <= 45:
            return 9
        elif 46 <= self <= 50:
            return 10
        elif 51 <= self <= 55:
            return 11
        elif 56 <= self <= 60:
            return 12
        elif 61 <= self <= 65:
            return 13
        elif 66 <= self <= 70:
            return 14
        elif 71 <= self <= 75:
            return 15
        elif 76 <= self <= 80:
            return 16
        elif 81 <= self <= 84:
            return 17
        elif 85 <= self <= 89:
            return 18
        elif 90 <= self <= 94:
            return 19
        elif 95 <= self <= 98:
            return 20
        elif 99 <= self <= 100:
            return 21



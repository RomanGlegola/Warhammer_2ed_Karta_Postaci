from Warhammer_2ed_Karta_Postaci.MaszynaLosująca import RzutyKoscia


class Kalendarium:
    """
    aby wywołać wiek postaci wypisz:
        print(data_urodzenia_postaci()[0])
    aby wywołać opis znaku gwiezdnego wpisz:
        print(data_urodzenia_postaci()[1])
    """

    def data_urodzenia_postaci(self=2522, wiek=RzutyKoscia.rzuc_koscia_100()):
        data_urodzenia = self - wiek

        return wiek, data_urodzenia

    """ 
    aby wywołać nazwę znaku gwiezdnego wpisz:
        print(znak_gwiezdny()[0])
    aby wywołać opis znaku gwiezdnego wpisz:
        print(znak_gwiezdny()[1])
    aby wywołać przybliżoną datę znaku gwiezdnego wpisz:
        print(znak_gwiezdny()[2])
    aby wywołać wynik rzutu na wybór znaku gwiezdnego wpisz:
        print(znak_gwiezdny()[3])
    """

    def znak_gwiezdny(self=RzutyKoscia.rzuc_koscia_wieloscienna(20)):
        # Kolejność Znaków Gwiezdnych jest podana w kolejności w jakich po sobie następują.
        znaki_gwiezdne = {
            0: ["Błąd, znak gwiezdny z początku", "błąd, znak gwiezdny z początku", "błąd, znak gwiezdny z początku"],
            1: ["Wymund Pustelnik",     "Znak wytrzymałości.",              "11 Przedwiedźmia - 30 Przedwiedźmia"],
            2: ["Wielki Krzyż",         "Znak czystości.",                  "31 Przedwiedźmia - 16 Powiedźmia."],
            3: ["Wół Gnuthus",          "Znak dokładności.",                "17 Powiedźmia - 4 Zmiany Roku."],
            4: ["Sznur Limnera",        "Znak wiernej służby.",             "5 Zmiany Roku - 10 Czasu Orki."],
            5: ["Smok Dragomas",        "Znak odwagi.",                     "11 Czasu Orki - 30 Czasu Orki."],
            6: ["Gwiazda Uroku",        "Znak tajemnicy i iluzji.",         "31 Czasu orki - 17 Czasu Sigmara."],
            7: ["Pas Grungiego",        "Znak sprawności wojennej.",        "18 Czasu Sigmara - 4 Czasu Letniego."],
            8: ["Mędrzec Mammit",       "Znak mądrości.",                   "5 Czasu Letniego - 24 Czasu Letniego."],
            9: ["Głupiec Mummit",       "Znak instynktu.",                  "25 Czasu Letniego - 10 Przed Tajemnicą."],
            10: ["Dwa byki",            "Znak płodności i rzemiosła.",      "11 Przed Tajemnicą - 30 Przed Tajemnicą."],
            11: ["Tancerka",            "Znak miłości i pożądania.",        "31 Przed Tajemnicą - 16 Po Tajemnicy."],
            12: ["Bębniarz",            "Znak zabawy i radości.",           "17 Po Tajemnicy - 4 Czasu Zbiorów."],
            13: ["Dudy",                "Znak oszustwa.",                   "5 Czasu Zbiorów - 24 Czasu Zbiorów."],
            14: ["Vobist Ulotny",       "Znak ciemności i niepewności.",    "25 Czasu Zbiorów - 10 Czasu Warzenia."],
            15: ["Rozbity Wóz",         "Znak dumy.",                       "11 Czasu Warzenia - 30 Czasu Warzenia."],
            16: ["Tłusty Kozioł",       "Znak ukrytej namiętności.",        "31 Czasu Warzenia - 17 Czasu Mrozów."],
            17: ["Kocioł Rhyi",         "Znak łaski, śmierci i tworzenia.", "18 Czasu Mrozów - 4 Czasu Ulryka."],
            18: ["Złoty Kogut",         "Znak kupców i bogactwa.",          "5 Czasu Ulryka - 24 Czasu Ulryka."],
            19: ["Lancet",              "Znak nauki i talentu.",            "25 Czasu Ulryka - 2 Przedwiedźmia."],
            20: ["Gwiazda Wieczorna",   "Znak magii.",                      "3 Przedwiedźmia - 10 Przedwiedźmia. "],
            21: ["Błąd, znak gwiezdny z końca", "błąd, znak gwiezdny z końca", "błąd, znak gwiezdny z końca"]}

        znaki_gwiezdne_nazwa = znaki_gwiezdne[self][0]
        znaki_gwiezdne_opis = znaki_gwiezdne[self][1]
        znaki_gwiezdne_przyblizona_data = znaki_gwiezdne[self][2]
        wynik_na_kosci = self

        return znaki_gwiezdne_nazwa, znaki_gwiezdne_opis, znaki_gwiezdne_przyblizona_data, wynik_na_kosci

    """
    * Przedwiedźmie     33
    * Hexennacht       1
    * Powiedźmie       32
    * Zmiany Roku      33
    * Równonoc         1
    * Czas Orki        33
    * Czas Sigmara     33
    * Czas Letni       33
    * Let Przesilenie  1
    * Przed Tajemnicą  33
    * Tajemnica        1
    * Po Tajemnicy     32
    * Czas Zbiorów     33
    * Równonoc         1
    * Czas Warzenia    33
    * Czas Mrozów      33
    * Czas Ulryka      33
    * Zim Przesilenie  1
    
    *1. Wymund Pustelnik     11 Przedwiedźmia - 30 Przedwiedźmia     20 dni    
    *2. Wielki Krzyż         31 Przedwiedźmia - 16 Powiedźmia        20 dni!   
    *3. Sznur Limnera        17 Powiedźmia - 4 Zmiany Roku           20 dni    
    *4. Wół Gnuthus          5 Zmiany Roku - 10 Czasu Orki           40 dni!   
    *5. Smok Dragomas        11 Czasu Orki - 30 Czasu Orki           20 dni    
    *6. Gwiazda Uroku        31 Czasu Orki - 17 Czasu Sigmara        20 dni    
    *7. Pas Grungiego        18 Czasu Sigmara - 4 Czasu Letniego     20 dni    
    *8. Mędrzec Mammit       5 Czasu Letniego - 24 Czasu Letniego    20 dni    
    *9. Głupiec Mummit       25 Czasu Letniego - 10 Przed Tajemnicą  20 dni!   
    *10 Dwa byki             11 Przed Tajemnicą - 30 Przed Tajemnicą 20 dni    
    *11 Tancerka             31 Przed Tajemnicą - 16 Po Tajemnicy    20 dni!   
    *12 Bębniarz             17 Po Tajemnicy - 4 Czasu Zbiorów       20 dni    
    *13 Dudy                 5 Czasu Zbiorów - 24 Czasu Zbiorów      20 dni    
    *14 Vobist Ulotny        25 Czasu Zbiorów - 10 Czasu Warzenia    20 dni!   
    *15 Rozbity Wóz          11 Czasu Warzenia - 30 Czasu Warzenia   20 dni    
    *16 Tłusty Kozioł        31 Czasu Warzenia - 17 Czasu Mrozów     20 dni    
    *17 Kocioł Rhyi          18 Czasu Mrozów - 4 Czasu Ulryka        20 dni    
    *18 Złoty Kogut          5 Czasu Ulryka - 24 Czasu Ulryka        20 dni    
    *19 Lancet               25 Czasu Ulryka - 2 Przedwiedźmia       12 dni!   
    *20 Gwiazda Wieczorna    3 Przedwiedźmia - 10 Przedwiedźmia      8 dni     
    """

    """ 
    aby wywołać dzień miesiąca wpisz: 
        print(data_urodzenia_miesieczna()[0])
    aby wywołać nazwę miesiąca wpisz:
        print(data_urodzenia_miesieczna()[1])
    aby wywołać dzień i nazwę miesiąca wpisz:
        print(data_urodzenia_miesieczna())
    """

    def data_urodzenia_miesieczna(self=znak_gwiezdny()[3]):
        # Wypisuje dokładną miesięczną datę urodzin.
        data_miesieczna_8_dni = RzutyKoscia.rzuc_koscia_wieloscienna(1, 8)
        data_miesieczna_12_dni = RzutyKoscia.rzuc_koscia_wieloscienna(1, 12)
        data_miesieczna_20_dni = RzutyKoscia.rzuc_koscia_wieloscienna(1, 20)
        data_miesieczna_40_dni = RzutyKoscia.rzuc_koscia_wieloscienna(1, 40)

        if self == 1:
            return data_miesieczna_20_dni + 10, "dnia Przedwiedźmia"
        elif self == 2:
            if 1 <= data_miesieczna_20_dni <= 3:
                return (data_miesieczna_20_dni + 30), "dnia Przedwiedźmia"
            elif data_miesieczna_20_dni == 4:
                return "w Hexennacht"
            elif 5 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 4, "dnia Powiedźmia"
        elif self == 3:
            if 1 <= data_miesieczna_20_dni <= 16:
                return data_miesieczna_20_dni + 16, "dnia Powiedźmia"
            elif 17 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 16, "dnia Zmiany Roku"
        elif self == 4:
            if 1 <= data_miesieczna_40_dni <= 29:
                return data_miesieczna_40_dni + 4, "dnia Zmiany Roku"
            elif data_miesieczna_40_dni == 30:
                return "w Wiosenną Równonoc"
            elif 31 <= data_miesieczna_40_dni <= 40:
                return data_miesieczna_40_dni - 30, "dnia Czasu Orki"
        elif self == 5:
            return data_miesieczna_20_dni + 10, "dnia Czasu Orki"
        elif self == 6:
            if 1 <= data_miesieczna_20_dni <= 3:
                return data_miesieczna_20_dni + 30, "dnia Czasu Orki"
            elif 4 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni + 4, "dnia Czasu Sigmara"
        elif self == 7:
            if 1 <= data_miesieczna_20_dni <= 16:
                return data_miesieczna_20_dni + 17, "dnia Czasu Sigmara"
            elif 17 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 16, "dnia Czasu Letniego"
        elif self == 8:
            return data_miesieczna_20_dni + 4, "dnia Czasu Letniego"
        elif self == 9:
            if 1 <= data_miesieczna_20_dni <= 9:
                return data_miesieczna_20_dni + 24, "dnia Czasu Letniego"
            elif data_miesieczna_20_dni == 10:
                return "w Letnie Przesilenie"
            elif 11 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 10, "dnia Przed Tajemnicą"
        elif self == 10:
            return data_miesieczna_20_dni + 10, "dnia Przed Tajemnicą"
        elif self == 11:
            if 1 <= data_miesieczna_20_dni <= 3:
                return data_miesieczna_20_dni + 30, "dnia Przed Tajemnicą"
            elif 4 == data_miesieczna_20_dni:
                return "w dniu Tajemnicy"
            elif 5 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 4, "dnia Po Tajemnicy"
        elif self == 12:
            if 1 <= data_miesieczna_20_dni <= 16:
                return data_miesieczna_20_dni + 16, "dnia Po Tajemnicy"
            elif 17 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 16, "dnia Czasu Zbiorów"
        elif self == 13:
            return data_miesieczna_20_dni + 4, "dnia Czasu Zbiorów"
        elif self == 14:
            if 1 <= data_miesieczna_20_dni <= 9:
                return data_miesieczna_20_dni + 24, "dnia Czasu Zbiorów"
            elif 10 == data_miesieczna_20_dni:
                return "w Równonoc Jesienną"
            elif 11 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 10, "dnia Warzenia"
        elif self == 15:
            return data_miesieczna_20_dni + 10, "dnia Warzenia"
        elif self == 16:
            if 1 <= data_miesieczna_20_dni <= 3:
                return data_miesieczna_20_dni + 30, "dnia Warzenia"
            elif 4 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 3, "dnia Czasu Mrozów"
        elif self == 17:
            if 1 <= data_miesieczna_20_dni <= 16:
                return data_miesieczna_20_dni + 17, "dnia Czasu Mrozów"
            elif 17 <= data_miesieczna_20_dni <= 20:
                return data_miesieczna_20_dni - 16, "dnia Czasu Ulryka"
        elif self == 18:
            return data_miesieczna_20_dni + 4, "dnia Czasu Ulryka"
        elif self == 19:
            if 1 <= data_miesieczna_12_dni <= 9:
                return data_miesieczna_12_dni + 24, "dnia Czasu Ulryka"
            elif 10 == data_miesieczna_12_dni:
                return "w Zimowe Przesilenie"
            elif 11 <= data_miesieczna_12_dni <= 12:
                return data_miesieczna_12_dni - 10, "dnia Przedwiedźmia"
        elif self == 20:
            return data_miesieczna_8_dni + 2, "dnia Przedwiedźmia"
        else:
            print("Error")


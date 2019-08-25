from Warhammer_2ed_Karta_Postaci.MaszynaLosująca import RzutyKoscia

"""
aby wylosować imie człowieka wpisz:
    wybierz_imie_czlowiek_mezczyzna()
lub
    wybierz_imie_czlowiek_kobieta()

aby wylosowac imie elfa wpisz:
    wybierz_imie_elf_mezczyzna()
lub
    wybierz_imie_elf_kobieta()

aby wylosowac imie krasnoluda wpisz:
    wybierz_imie_krasnolud_mezczyzna()
lub
    wybierz_imie_krasnolud_mezczyzna()
    
aby wylosowac imie niziolka wpisz:
    wybierz_imie_krasnolud_mezczyzna()
lub
    wybierz_imie_krasnolud_kobieta()

"""

def wybierz_imie_czlowiek_mezczyzna(self=RzutyKoscia.rzuc_koscia_100()):
    if 1 <= self <= 33:
        return imie_czlowiek_mezczyzna_1()
    elif 34 <= self <= 66:
        return imie_czlowiek_mezczyzna_2()
    elif 67 <= self <= 100:
        return imie_czlowiek_mezczyzna_3()


def wybierz_imie_czlowiek_kobieta(self):
    if 1 <= self <= 33:
        return imie_czlowiek_kobieta_1()
    elif 34 <= self <= 66:
        return imie_czlowiek_kobieta_2()
    elif 67 <= self <= 100:
        return imie_czlowiek_kobieta_3()


def wybierz_imie_elf_mezczyzna():
    return (imie_elf_1_czlon() +
            imie_elf_lacznik() +
            imie_elf_mezczyzna_2_czlon())


def wybierz_imie_elf_kobieta():
    return (imie_elf_1_czlon() +
            imie_elf_lacznik() +
            imie_elf_kobieta_2_czlon())


def wybierz_imie_krasnolud_mezczyzna():
    return (imie_krasnolud_1_czlon() +
            imie_krasnolud_mezczyzna_2_czlon())


def wybierz_imie_krasnolud_kobieta():
    return (imie_krasnolud_1_czlon() +
            imie_krasnolud_kobieta_2_czlon())


def wybierz_imie_niziolek_mezczyzna():
    return (imie_niziolek_1_czlon() +
            imie_niziolek_mezczyzna_2_czlon())


def wybierz_imie_niziolek_kobieta():
    return (imie_niziolek_1_czlon() +
            imie_niziolek_kobieta_2_czlon())


def imie_czlowiek_mezczyzna_1(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Abelard", "Abehelm", "Admund", "Adred", "Adric", "Agis",
            "Alaric", "Alberic", "Albrecht", "Aldebrand", "Aldred", "Aldric", "Alfreid",
            "Altmar", "Alric", "Andre", "Andred", "Andric", "Anshelm", "Anton", "Arne",
            "Arnulf", "Axel", "Axelbrand", "Baldred", "Baldric", "Baldwin", "Balthasar",
            "Barnabas", "Bart", "Bartolf", "Bartomar", "Bernolt", "Bertold", "Bertolf",
            "Boris", "Bruno", "Burgolf", "Calvin", "Casimir", "Caspar", "Cedred", "Conrad",
            "Corvin", "Dagmar", "Dantmar", "Dankred", "Dekmar", "Detlef", "Diebold", "Diel",
            "Dietfried", "Dieter", "Dietmar", "Dietmund", "Dietrich", "Dirk", "Donat", "Durnhelm",
            "Eber", "Eckel", "Eckhart", "Edgar", "Edmund", "Edwin", "Ehrhart", "Ehrl", "Ehrwig",
            "Eldred", "Elmeric", "Emil", "Engel", "Engelbert", "Engelbrecht", "Engelhart",
            "Eodred", "Eomund", "Erdman", "Erdred", "Erkenbrand", "Erasmus", "Erich", "Erman",
            "Ernst", "Erwin", "Eugen", "Eustasius", "Ewald", "Fabian", "Faustus", "Felix", "Ferdinand",
            "Fleugweiner", "Fosten", "Franz", "Frediger", "Fredric", "Friebald", "Friedrich", "Fulko"]
    return imie[self]


def imie_czlowiek_mezczyzna_2(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Gawin", "Gerber", "Gerhart", "Gerlach", "Gernar", "Gerolf", "Gilbrecht",
            "Gisbert", "Giselbrecht", "Gismar", "Goran", "Gosbert", "Goswin", "Gotfried", "Gothard",
            "Gottolf", "Gotwin", "Gregor", "Greimold", "Grimwold", "Griswold", "Guildo", "Gundolf",
            "Gundred", "Gunnar", "Gunter", "Gunther", "Gustaf", "Hadred", "Hadwin", "Hagar", "Hagen",
            "Haldred", "Halman", "Hamlyn", "Hand", "Harbrand", "Harman", "Hartmann", "Haug", "Heidric",
            "Heimar", "Heinfriem", "Heinman", "Heinrich", "Heinz", "Helmut", "Henlyn", "Hermann",
            "Herwin", "Hieronymus", "Hildebart", "Hildebrand", "Hildemar", "Hildemund", "Hildred",
            "Hildric", "Horst", "Hugo", "Igor", "Ingwald", "Jander", "Jekil", "Jodokus", "Johann",
            "Jonas", "Jorg", "Jorn", "Josef", "Jost", "Jurgen", "Karl", "Kaspar", "Klaus", "Kleber",
            "Konrad", "Konradin", "Kurt", "Lamprecht", "Lanfird", "Lanric", "Lanwin", "Leo", "Leopold",
            "Levin", "Liebert", "Liebrecht", "Liebwin", "Lienchart", "Linus", "Lodwig", "Lothar",
            "Lucius", "Ludwig", "Luitpold", "Lukas", "Lupold", "Lupus", "Luther", "Lutolf"]
    return imie[self]


def imie_czlowiek_mezczyzna_3(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Mandred", "Magnus", "Mandred", "Manfred", "Mathias", "Max", "Maximillian",
            "Meiner", "Meinhart", "Meinolf", "Mekel", "Merkel", "Nat", "Nathandar", "Nicodemus", "Odamar",
            "Odric", "Odwin", "Olbrecht", "Oldred", "Oldric", "Ortlieb", "Ortolf", "Orwin", "Oswald",
            "Osric", "Oswin", "Otfried", "Otto", "Otwin", "Paulus", "Prospero", "Ragen", "Ralf", "Rabrecht",
            "Randulf", "Ranulf", "Ranald", "Reikhard", "Rein", "Reiner", "Renhard", "Reinolt", "Reuban",
            "Rigo", "Roderic", "Rolf", "Ruben", "Rudel", "Rudgar", "Rudolf", "Rufus", "Rusprecht",
            "Sebastian", "Semund", "Sepp", "Sieger", "Siegfried", "Siegmund", "Sigismund", "Sigric",
            "Steffan", "Tankred", "Theoderic", "Tilmann", "Tomas", "Trubald", "Trubert", "Udo",
            "Ulli", "Ulfred", "Ulfman", "Ulman", "Uto", "Valdred", "Valdric", "Varl", "Viggo", "Viktor",
            "Vilmar", "Volker", "Volkhard", "Volkrad", "Volkin", "Voltz", "Walbrecht", "Waldor", "Waldred",
            "Walther", "Warmund", "Werner", "Wilbert", "Wilfried", "Wilhelm", "Woldred", "Wolfram",
            "Wolfhart", "Wolfgang", "Wulf", "Xavier"]
    return imie[self]


def imie_czlowiek_kobieta_1(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Abbie", "Abighild", "Abigund", "Abigunda", "Ada", "Ada", "Adel", "Adelind",
            "Adeline", "Adelyn", "Adelle", "Adelle", "Agathe", "Agnete", "Aldreda", "Alfreda", "Alicia",
            "Allane", "Althea", "Amalie", "Amalinde", "Amalyn", "Anhilda", "Annabella", "Anna", "Anthea",
            "Arabella", "Aver", "Bechilda", "Bella", "Bella", "Bellane", "Benedicta", "Berlinda", "Berlyn",
            "Bertha", "Berthilda", "Bess", "Bess", "Beth", "Broncea", "Brunhilda", "Camilla", "Carla",
            "Carlinda", "Carlotta", "Cilicia", "Cilie", "Clora", "Clothilda", "Connie", "Constance",
            "Constanza", "Cordelia", "Dema", "Demona", "Desdemona", "Dorthilda", "Drachena", "Drachilda",
            "Edhilda", "Edith", "Edyth", "Edythe", "Eleanor", "Eleanor", "Elinor", "Elisinda", "Elsina",
            "Ella", "Ellene", "Ellinde", "Eloise", "Elsa", "Elsa", "Elsbeth", "Elspeth", "Elyn", "Emagunda",
            "Emelia", "Emme", "Emmalyn", "Emmanuel", "Emerlinde", "Emerlyn", "Erica", "Ermina", "Erminlind",
            "Ermintrude", "Esmeralda", "Estelle", "Etheldreda", "Etherlind", "Ethelreda", "Fay", "Frieda",
            "Frieda", "Friedhilda", "Friedrun", "Friedrica"]
    return imie[self]


def imie_czlowiek_kobieta_2(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Gabby", "Gabby", "Gabriele", "Galina", "Gena", "Genevieve", "Genoveva",
            "Gerberga", "Gerda", "Gerlinde", "Gertie", "Gertrud", "Greta", "Greta", "Gretchen", "Grizelda",
            "Grunhilda", "Gudrun", "Gudryn", "Hanna", "Hedwig", "Heidi", "Heidrun", "Helga", "Herlinde",
            "Herwig", "Hilda", "Hilda", "Hildegart", "Hildegund", "Honoria", "Ida", "Ingrid", "Ingrun",
            "Ingrund", "Irmella", "Irmine", "Isabella", "Isadora", "Isolde", "Isolde", "Jocelin",
            "Johanna", "Josie", "Karin", "Katarine", "Katheryn", "Katharina", "Katherine", "Katherine",
            "Keterlind", "Keterlyn", "Kitty", "Kirsten", "Kirstena", "Kristyn", "Kirsten", "Kirsten",
            "Kirstyn", "Lavina", "Lavinia", "Leanor", "Leanora", "Leticia", "Letty", "Lena", "Lenora",
            "Lisa", "Lisbeth", "Lizzie", "Lorinda", "Lorna", "Lucinda", "Lucretia", "Lucie", "Ludmilla",
            "Mabel", "Madge", "Magdalyn", "Maggie", "Maghilda", "Maglind", "Maglyn", "Magunda", "Magreta",
            "Maida", "Marien", "Marietta", "Margaret", "Marget", "Margreta", "Marline", "Marlyn",
            "Mathilda", "Maude", "May", "Meg", "Melicent", "Miranda", "Moll"]
    return imie[self]


def imie_czlowiek_kobieta_3(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Nathilda", "Nellie", "Nellie", "Nora", "Nora", "Olga", "Olga", "Ophelia",
            "Ophelia", "Osterhild", "Osterhild", "Ostelle", "Ostelle", "Ostia", "Ostia", "Ottagunda",
            "Ottagunda", "Ottaline", "Ottaline", "Ottilda", "Ottilda", "Ottilyn", "Ottilyn", "Pertida",
            "Pertida", "Pergale", "Pergale", "Pergunda", "Pergunda", "Petronella", "Petronella",
            "Philomelia", "Philomelia", "Reikhilda", "Reikhilda", "Renata", "Renata", "Rosabel",
            "Rosabel", "Rosabella", "Rosabella", "Rosale", "Rosale", "Rosalia", "Rosalia", "Rosalin",
            "Rosalin", "Rosalinde", "Rosalinde", "Rosamunde", "Rosamunde", "Rosanne", "Rosanne", "Rose",
            "Rose", "Roz", "Roz", "Rozhilda", "Rozhilda", "Salina", "Salina", "Saltza", "Saltza",
            "Sigismunda", "Sigismunda", "Sigrid", "Sigrid", "Sigunda", "Sigunda", "Solla", "Solla",
            "Styrine", "Styrine", "Talima", "Talima", "Theodora", "Theodora", "Therese", "Therese",
            "Tilea", "Tilea", "Ursula", "Ursula", "Ulrica", "Ulrica", "Valeria", "Valeria", "Verena",
            "Verena", "Wilfrieda", "Wilfrieda", "Wilhelmina", "Wilhelmina", "Winifred", "Winifred",
            "Wolfhide", "Wolfhide", "Zomelda", "Zomelda", "Zena"]
    return imie[self]


def imie_elf_1_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Aed", "Ael", "Aelf", "Aen", "Aeth", "Alth", "An", "And", "Ar", "Arg", "Ast",
            "Ath", "Av", "Ban", "Bel", "Beth", "Cad", "Cael", "Caem", "Caeth", "Cal", "Cam", "Cel", "Cir",
            "El", "Eld", "Elth", "En", "End", "Er", "Ers", "Fand", "Fer", "Ferg", "Fim", "Fin", "Gal", "Gald",
            "Gaen", "Gaes", "Ged", "Gen", "Ges", "Geth", "Glor", "Has", "Hath", "Hel", "Heth", "Hith", "Ill",
            "Ind", "Ist", "Ith", "Iy", "Kor", "Ky", "Kyr", "La", "Lan", "Lil", "Lim", "Lith", "Loth", "Mal",
            "Mar", "Mas", "Math", "Me", "Mes", "Meth", "Men", "Mor", "Mort", "Nal", "Nar", "Nen", "Nor", "Norl",
            "Ri", "Riabb", "Riann", "Rid", "Riell", "Rien", "Ruth", "Ryn", "Tab", "Tal", "Tan", "Tar", "Teth",
            "Tel", "Tor", "Ty", "Ull", "Um", "Ur", "Yr", "Yv"]
    return imie[self]


def imie_elf_mezczyzna_2_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "baen", "baine", "baire", "bar", "bhir", "brier", "brior", "brin", "daen",
            "daine", "daire", "dar", "dhil", "dhir", "drel", "drir", "dror", "eorl", "eos", "eoth", "fil",
            "fin", "fir", "hil", "hin", "hir", "hor", "il", "in", "ion", "ir", "is", "ith", "lael", "laen",
            "laer", "laine", "laire", "lan", "las", "len", "les", "lil", "lin", "lir", "lis", "lor", "los",
            "mael", "maen", "mair", "main", "mal", "mar", "mil", "min", "mir", "nael", "naen", "naer",
            "nail", "nair", "nal", "nan", "nar", "neal", "nean", "near", "nil", "nin", "nir", "nis",
            "ran", "rea", "rel", "ril", "riol", "rion", "rior", "riorl", "riorn", "ril", "ryel", "taen",
            "tair", "tain", "than", "thar", "thel", "thil", "thir", "thin", "thril", "thrin", "thwe",
            "til", "tin", "tis", "we", "yan"]
    return imie[self]


def imie_elf_kobieta_2_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "a", "aine", "am", "ann", "arma", "arna", "arth", "ath", "beann", "bet",
            "beth", "brim", "brys", "deann", "det", "deth", "dys", "drian", "driel", "drys", "eann",
            "eanna", "earna", "earth", "elle", "eth", "eys", "eyth", "felle", "fionn", "flys", "fyll",
            "fynn", "fyr", "fys", "i", "ille", "ina", "ira", "isa", "ithi", "itt", "la", "lam", "lana",
            "larna", "lath", "leann", "leath", "lel", "lelle", "leth", "let", "lielle", "lieth", "lyann",
            "nelle", "nem", "neth", "ni", "niell", "niella", "nith", "nas", "reann", "rell", "relle",
            "rielle", "ris", "rith", "rys", "rar", "rath", "ser", "seth", "sir", "sith", "sor", "soth",
            "shar", "sher", "shir", "sys", "tar", "teal", "teann", "ter", "thea", "ther", "thi", "thryn",
            "thyn", "tir", "tor", "tos", "tryan", "trys", "yll", "yrs", "ys"]
    return imie[self]


def imie_elf_lacznik(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "a", "a", "al", "al", "an", "an", "ar", "ar", "as", "as", "e", "e", "el",
            "el", "en", "en", "er", "er", "es", "es", "fan", "fan", "fen", "fen", "fin", "fin", "i",
            "i", "il", "il", "in", "in", "ir", "ir", "is", "is", "o", "o", "ol", "ol", "on", "on", "or",
            "or", "os", "os", "ra", "ra", "ral", "ral", "ran", "ran", "re", "re", "rel", "rel", "ren",
            "ren", "ri", "ri", "ril", "ril", "rin", "rin", "ro", "ro", "rol", "rol", "ron", "ron", "ry",
            "ry", "sa", "sa", "sal", "sal", "san", "san", "se", "se", "sel", "sel", "sen", "sen", "si",
            "si", "sil", "sil", "sin", "sin", "so", "so", "sol", "sol", "son", "son", "u", "u", "ul", "ul"]
    return imie[self]


def imie_krasnolud_1_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Al", "Ath", "Athran", "Bal", "Bala", "Bara", "Bel", "Bela", "Ber", "Bok",
            "Bor", "Bur", "Da", "Dam", "Dora", "Drok", "Drong", "Dur", "Dwal", "El", "Ela", "Elan", "Elda",
            "Fa", "Far", "Fara", "Fim", "Fima", "Firen", "Fur", "Fura", "Ga", "Gim", "Gol", "Gollen",
            "Got", "Gota", "Grim", "Gro", "Grun", "Hak", "Haka", "Har", "Hega", "Hur", "Kad", "Kar", "Kata",
            "Kaz", "Kaza", "Krag", "Logaz", "Lok", "Lun", "Mo", "Mola", "Mor", "Mora", "No", "Nola", "Nor",
            "Noran", "Nun", "Oda", "Oka", "Olla", "Olf", "Oth", "Othra", "Ro", "Ror", "Roran", "Ska",
            "Skalla", "Skalf", "Skar", "Skor", "Skora", "Snor", "Snora", "Sven", "Thar", "Thor", "Thora",
            "Thron", "Thrun", "Thura", "Un", "Utha", "Ulla", "Vala", "Var", "Vara", "Zak", "Zaka", "Zakan",
            "Zar", "Zara", "Zam", "Zama"]
    return imie[self]


def imie_krasnolud_mezczyzna_2_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "bin", "bin", "bor", "bor", "dil", "din", "din", "dok", "dok", "dor",
            "dor", "drin", "drin", "fin", "fin", "gan", "gan", "gar", "gar", "gil", "gil", "gin",
            "gni", "gni", "grom", "grom", "grond", "grond", "groth", "groth", "grum", "grum", "grund",
            "grund", "grunt", "gon", "gon", "gor", "gor", "grim", "grim", "gron", "gron", "grom", "grom",
            "gul", "gul", "gun", "gun", "gund", "gund", "ki", "ki", "kin", "kin", "krag", "krag", "kri",
            "kri", "krin", "krin", "li", "li", "lin", "lin", "lik", "lik", "lok", "lok", "lun", "lun",
            "lin", "min", "mir", "mir", "nin", "nin", "nir", "nir", "rag", "ri", "ri", "rig", "rig",
            "rik", "rik", "rin", "rin", "run", "run", "skin", "tin", "tin", "tok", "tok", "trek", "trok",
            "zin", "zor", "zor"]
    return imie[self]


def imie_krasnolud_kobieta_2_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "bina", "bina", "bora", "bora", "dila", "dina", "dina", "dorkina", "dorkina",
            "dora", "dora", "drinella", "fina", "fina", "fya", "fya", "gana", "gana", "gara", "gara", "gella",
            "gella", "gina", "groma", "groma", "grondella", "grondella", "grotha", "grotha", "gruma",
            "gruma", "grunda", "grunda", "gruntina", "gruntina", "gona", "gora", "gora", "grimella",
            "grimella", "grina", "grina", "gromina", "gromina", "gula", "grunella", "grunella", "grundina",
            "grundina", "kina", "kina", "kragella", "kragella", "krina", "krina", "kya", "kya", "lina",
            "lina", "likina", "likina", "loka", "loka", "luna", "mina", "mina", "mira", "mira", "nina",
            "nina", "nira", "nira", "nya", "ragina", "ragina", "riga", "riga", "riga", "rika", "rika",
            "rina", "rina", "runa", "runa", "runella", "runella", "skina", "skina", "skinella", "skinella",
            "tina", "toka", "trekella", "trekella", "trekina", "trekina", "troka", "troka", "zina", "zora"]
    return imie[self]


def imie_niziolek_1_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "Bag", "Balf", "Berc", "Bill", "Bobb", "Bodg", "Bog", "Bom", "Bonn", "Brog",
            "Bulc", "Bull", "Bust", "Cam", "Cap", "Ced", "Chund", "Clog", "Clof", "Cob", "Cog", "Crum",
            "Crump", "Curl", "Dod", "Dog", "Dott", "Dram", "Drub", "Drog", "Dron", "Durc", "Elm", "Enn",
            "Ermin", "Ethan", "Falc", "Fald", "Falm", "Far", "Fild", "Flac", "Fogg", "Frit", "Ful", "Func",
            "Gaff", "Galb", "Gamm", "Gert", "Giff", "Gild", "Gon", "Grop", "Gudd", "Grump", "Ham", "Hal",
            "Hart", "Harp", "Jac", "Jas", "Jasp", "Joc", "Lac", "Lil", "Lob", "Lott", "Lud", "Lurc", "Mad",
            "Mag", "Man", "May", "Mer", "Mul", "Murc", "Murd", "Nag", "Nell", "Nobb", "Od", "Og", "Old",
            "Pipp", "Podd", "Porc", "Riff", "Rip", "Rob", "Sam", "Supp", "Taff", "Talb", "Talc", "Tay",
            "Tom", "Wald", "Watt", "Will"]
    return imie[self]


def imie_niziolek_mezczyzna_2_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "belly", "belly", "belly", "belly", "belly", "belly", "belly",
            "er", "er", "er", "er", "er", "er", "er", "er", "fast", "fast", "fast", "fast", "fast",
            "fast", "fast", "in", "in", "in", "in", "in", "in", "in", "it", "it", "it", "it", "it",
            "it", "it", "mutch", "mutch", "mutch", "mutch", "mutch", "mutch", "mutch", "o", "o",
            "o", "o", "o", "o", "o", "o", "odoc", "odoc", "odoc", "odoc", "odoc", "odoc", "odoc",
            "riadoc", "riadoc", "riadoc", "riadoc", "riadoc", "riadoc", "riadoc", "regar", "regar",
            "regar", "regar", "regar", "regar", "regar", "wick", "wick", "wick", "wick", "wick",
            "wick", "wick", "wise", "wise", "wise", "wise", "wise", "wise", "wise", "wit", "wit",
            "wit", "wit", "wit", "wit", "wit", "y", "y", "y", "y", "y", "y", "y"]
    return imie[self]


def imie_niziolek_kobieta_2_czlon(self=RzutyKoscia.rzuc_koscia_100()):
    imie = ["początek listy", "a", "a", "a", "a", "a", "adell", "adell", "adell", "adell", "adell",
            "alot", "alot", "alot", "alot", "alot", "apple", "apple", "apple", "apple", "apple",
            "bell", "bell", "bell", "bell", "bell", "berry", "berry", "berry", "berry", "berry",
            "eena", "eena", "eena", "eena", "eena", "ella", "ella", "ella", "ella", "ella", "era",
            "era", "era", "era", "era", "et", "et", "et", "et", "et", "ia", "ia", "ia", "ia", "ia",
            "flower", "flower", "flower", "flower", "flower", "lotta", "lotta", "lotta", "lotta",
            "lotta", "petal", "petal", "petal", "petal", "petal", "riella", "riella", "riella",
            "riella", "riella", "sweet", "sweet", "sweet", "sweet", "sweet", "trude", "trude",
            "trude", "trude", "trude", "rose", "rose", "rose", "rose", "rose", "willow", "willow",
            "willow", "willow", "willow", "y", "y", "y", "y", "y", ]
    return imie[self]


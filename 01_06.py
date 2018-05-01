zviratka = ['pes','kočka','králík','had']
zviratka2 = ['pes','kočka','kráva','krokodýl','slepice']


# úkol 01 -> fce, která vrací zvířata která jsou kratší než 5 písmen
def kratkeZvire(seznamZvirat):
    seznamKratkychZvirat = []
    for zvire in seznamZvirat:
        if len(zvire)<5:
            seznamKratkychZvirat.append(zvire)
    return(seznamKratkychZvirat)
print(kratkeZvire(zviratka))


# úkol 02 -> fce, která vrací zvířata začínající na 'k'
def zvireOdK(seznamZvirat):
    seznam = []
    for zvire in seznamZvirat:
        if zvire[0] == 'k':
            seznam.append(zvire)
    return(seznam)
print(zvireOdK(zviratka))


# úkol 03 -> fce, která testuje, zda je zadané slovo v seznamu domácích zvířat
def zjisti(slovo):
    if slovo in zviratka:
        return True
    else:
        return False
#zadaneSlovo = input('Zadej slovo: ')
print(zjisti('pes'))


# úkol 04 -> fce, která dostane dva seznamy a vrátí 3 seznamy
def seznamy(seznam1, seznam2):
    stejne = []
    pouzePrvni = []
    pouzeDruhy = []
    for zvire1 in seznam1:
        if zvire1 in seznam2: # zvířata se nacházejí v obou seznamech
            stejne.append(zvire1)
        if zvire1 not in seznam2: #zvířata, která jsou pouze v prvním seznamu
            pouzePrvni.append(zvire1)
    for zvire2 in seznam2: # zvířata pouze v druhém seznamu
        if zvire2 not in seznam1:
            pouzeDruhy.append(zvire2)
    return stejne, pouzePrvni, pouzeDruhy
print(seznamy(zviratka,zviratka2))

# úkol 06 -> fce, která seřadí slova v seznamu podle druhého písmene
def druhePismeno(slovo):
        return slovo[1]

def seradit(seznam):
    seznam.sort(key = druhePismeno)
    return seznam

pokus = ['had','pes','andulka','kočka','králík']
print(seradit(pokus))

from random import choice, randrange

# fce, která vytvoří prázdné mapové pole na základě parametrů od uživatele (počet řádků a počet sloupců)
def prazdnaMapa(y,x):
    mapa = []
    for radky in range(y):
        #pro každý řádek vytvoř seznam a vlož ho do mapy
        radekSeznam = []
        mapa.append(radekSeznam)
        for _ in range(x):
            mapa[radky].append('.')
    return mapa

#fce, která vykreslí mapu s aktuální polohou hada a ovoce
def vykresliMapu(had,vstupni_mapa,souradniceOvoce):
    for ovoce in souradniceOvoce:
        ovoceX = ovoce[0]
        ovoceY = ovoce[1]
        vstupni_mapa[ovoceY][ovoceX] = '?'
    for polozka in had:
        souradniceX = polozka[0]
        souradniceY = polozka[1]
        vstupni_mapa[souradniceY][souradniceX] = 'X'
    for i in vstupni_mapa:
        for j in i:
            print(j, end=' ')
        print('\n')

def pohyb(souradnicePohyb,strana,souradniceOvoce):
    souradniceX = souradnicePohyb[-1][0]
    souradniceY = souradnicePohyb[-1][1]
    if strana == 's':
        noveSouradnice = souradniceX,souradniceY-1
    elif strana == 'j':
        noveSouradnice = souradniceX,souradniceY+1
    elif strana == 'v':
        noveSouradnice = souradniceX+1,souradniceY
    elif strana == 'z':
        noveSouradnice = souradniceX-1,souradniceY
    # pokud had vyjede z mapy nebo narazí sám so sebe, tak je konec hry;
    if not(0 <= noveSouradnice[0]< x) or not(0 <= noveSouradnice[1] < y) or (noveSouradnice in souradnicePohyb):
        #print('blbý,no')
        raise ValueError('Game over!')
    souradnicePohyb.append((noveSouradnice))
    # ovoce - pokud had sezere ovoce, vygenerují se souřadnice nového ovoce (pomocí fce umisteniOvoce() a ze seznamu souřadnic ovoce se vymaže sežrané)
    if noveSouradnice in souradniceOvoce:
        souradniceOvoce.remove(noveSouradnice) # vymazání sežraného ovoce ze seznamu souřadnic ovoce
        print('ňamíííí')
        if not souradniceOvoce: #pokud je seznam ovoce prázdný, je umístěno nové ovoce
            umisteniOvoce(souradnicePohyb,souradniceOvoce) # umístění nového ovoce
    else: # pokud had nic nesežere, tak se umaže první souřadnice, celkový počet jeho článků/souřadnic zůstává stejný
        del souradnicePohyb[0]

# fce, která náhodně generuje pozici ovoce; v mapě je možné mít najednou víc ovoce
def umisteniOvoce(hadSouradnice,souradniceOvoce):
    while True: #vybraná pozice nesmí odpovídat pozici hada nebo už existujícího ovoce
        max_index_radku = y-1
        max_index_sloupce = x-1
        nahodnaY = randrange(0,max_index_radku)
        nahodnaX = randrange(0,max_index_sloupce)
        if (nahodnaX,nahodnaY) not in hadSouradnice:
            if (nahodnaX,nahodnaY) not in souradniceOvoce:
                #souradniceOvoce.append((randrange(0,max_index_sloupce),randrange(0,max_index_radku)))
                souradniceOvoce.append((nahodnaX,nahodnaY))
                #print(souradniceOvoce)
                break


had = [(0,0),(1,0),(2,0)]
souradniceOvoce = [(2,1)]
y = int(input('Velikost hrací plochy- počet řádků:'))
x = int(input('Velikost hrací plochy- počet sloupců:'))
n = 0 #pocet tahů


while True: # cyklus bude probíhat tak dlouho, než nastane Game Over!
    n = n + 1
    if n%30 == 0: #každé 30.kolo se přidá další ovoce
        umisteniOvoce(had,souradniceOvoce)
        print('další ovoce', n)
    mapa = prazdnaMapa(y,x)
    vykresliMapu(had,mapa,souradniceOvoce)
    while True: # ošetření, aby uživatel zadal správně směr
        strana = input ('Zadejte směr pohybu [s,j,v,z]: ')
        if (strana == 's') or (strana == 'j') or (strana == 'z') or (strana == 'v'):
            break
        print('Špatně zadaný směr !!!')
    pohyb(had,strana,souradniceOvoce)

cislice = ['0','1','2','3','4','5','6','7','8','9']

def kontrolaFormatu(RC):
    #rodneCislo = []
    #rodneCislo.extend(RC)
    if (RC[6] == '\\'):
        for cislo in RC[:6]+RC[7:]:
            if cislo not in cislice:
                print('Na', RC.index(cislo)+1, '. pozici se nenachází číslice')
                return False
                break
        delitelnostJedenacti(RC)
    else:
        print('Rodné číslo neobsahuje na 7. pozici lomítko(\)')

def delitelnostJedenacti(RC):
    cislo = int(RC[:6]+RC[7:])
    if cislo%11 == 0:
        print('Rodné číslo je dělitelné jedenácti.')
    else:
        print('Rodné číslo není dělitelné jedenácti!')

def datum(RC):
    rok = '19'+ RC[:2]
    if RC[2] == '5':
        mesic = '0'+ RC[3]
    elif RC[2] == '6':
        mesic = '1' + RC[3]
    else:
        mesic = RC[2:4]
    den = RC[4:6]
    print(rok, mesic, den)

def zjisteniPohlavi(RC):
    if (RC[2] == '6' or RC[2] == '5'):
        print('žena')
    else:
        print('muž')

zadaneRC = input('Zadejte rodné číslo: ')
kontrolaFormatu(zadaneRC)
datum(zadaneRC)
zjisteniPohlavi(zadaneRC)

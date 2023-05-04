def verificare_cuvant1( stare_initiala,cuvant ):
    global d
    global nr_stari_finale

    stare_curenta = stare_initiala
    
    for litera in cuvant:
        litera_gasita = 0
        for x in d[stare_curenta]:
        
            if x[1] == litera:
                stare_curenta = x[0]
                litera_gasita = 1
                
        if litera_gasita == 0: return False
    if stare_curenta in stari_finale: return True
    else: return False
                

def verificare_cuvant( cuvant,lista_stari_vizitate ):
    global d
    global stare_initiala
    global nr_stari_finale

    if stare_initiala not in lista_stari_vizitate:
        lista_stari_vizitate.append(stare_initiala)

    stare_curenta = stare_initiala
    
    for litera in cuvant:
        litera_gasita = 0
        for x in d[stare_curenta]:
        
            if x[1] == litera:
                stare_curenta = x[0]
                litera_gasita = 1
                if x[0] not in lista_stari_vizitate:
                    lista_stari_vizitate.append(x[0])
                
                
    

def bkt( k,cuvant,lista_cuvinte):
    global numar_stari,alfabet
    if k == numar_stari: 
        cuv = ""
        for litera in cuvant:
            cuv += litera
        lista_cuvinte.append(cuv)
    else:
        for litera in alfabet:
            cuvant.append(litera)
            bkt(k+1, cuvant,lista_cuvinte)
            cuvant.pop()

def stari_unreachable():
    global d, alfabet
    lista_cuvinte = []
    lista_stari_vizitate = []
    bkt(0,[],lista_cuvinte)
    for cuvant in lista_cuvinte:
        verificare_cuvant(cuvant,lista_stari_vizitate)
    
    lista = []

    for stare in d:
        if stare not in lista_stari_vizitate:
            lista.append(stare)

    return lista
    

def sterge_stare(stare):
    global d
    d[stare].clear()
    del d[stare]

def stari_moarte():
    global d,alfabet
    global stari_finale
    lista = []
    lista_cuvinte = []
    bkt(0,[],lista_cuvinte)
    for stare in d:
        ok = True
        if d not in stari_finale:
            ok = False
            for cuvant in lista_cuvinte:
                if verificare_cuvant1(stare, cuvant) == True:
                    ok = True
        if ok == False:
            lista.append(stare)
            
    return lista


def egalitate(stare1, stare2):
    global d
    if stare1 == stare2: return False
    if len(d[stare1]) != len(d[stare2]): return False
    for i in range(0, len(d[stare1])):
        if d[stare1][i][1] != d[stare2][i][1]: return False
        if d[stare1][i][0] != d[stare2][i][0]: return False
    return True

def uneste(stare1, stare2):
    global d
    nume_stare = str(stare1) + str(stare2)
    stare_noua = []
    for element in d[stare1]:
        stare_noua.append(element)
    sterge_stare(stare1)
    sterge_stare(stare2)
    d[nume_stare] = stare_noua
    for stare in d:
        for tranzitie in d[stare]:
            if str(tranzitie[0]) == str(stare1) or str(tranzitie[0]) == str(stare2):
                tranzitie[0] = str(nume_stare)



def minimization():
    global d
    global alfabet

    lista = stari_unreachable()
    for stare in lista:
        sterge_stare(stare)

    lista = stari_moarte()
    for stare in lista:
        sterge_stare(stare)

    while(True):
        variabila = False
        for stare1 in d:
            ok = True
            for stare2 in d:
                if egalitate(stare1, stare2) and stare1 < stare2:
                    uneste(stare1, stare2)
                    ok = True
                    variabila = True
                    break
            if ok == True: 
                break

        if variabila== False: 
            break
    
    

d = {}
alfabet = ""

f = open("input.txt", "r")

linie = f.readline()
linie = linie[:-1]
numar_stari = int(linie)

linie = f.readline()
linie = linie[:-1]
stari = [int(x) for x in linie.split()]

linie = f.readline()
linie = linie[:-1]
numar_muchii = int(linie)

for i in range(numar_muchii):
    linie = f.readline()
    linie = linie[:-1]
    linie = linie.split()
    nod_plecare = int(linie[0])
    nod_sosire = int(linie[1])
    litera = linie[2]
    if litera not in alfabet:
        alfabet += litera

    lista = []
    lista.append(nod_sosire)
    lista.append(litera)

    if nod_plecare not in d:
        d[nod_plecare] = []
        d[nod_plecare].append(lista)
    else:
        d[nod_plecare].append(lista)

linie = f.readline()
linie = linie[:-1]
stare_initiala = int(linie)

linie = f.readline()
linie = linie[:-1]
nr_stari_finale = int(linie)

linie = f.readline()
linie = linie[:-1]
stari_finale = [int(x) for x in linie.split()]

for stare in d:
    print(stare, d[stare])
print()
print()

minimization()

for stare in d:
    print(stare, d[stare])

""" 
Un exemplu de input:

8
1 2 3 4 5 6 7 8
14
1 2 a
1 3 b
2 2 a
2 4 b
3 2 a
3 3 b
4 2 a
4 5 b
5 2 a
5 1 b
6 2 a
6 7 b
7 8 a
8 7 a
1
1
5

Starea 6 este unreachable, deci o sterge
Starea 7 si 8 sunt stari "moarte", deci le sterge (am facut de fapt un ciclu infinit)
Starea 1 si 3 sunt echivalente deci le uneste
"""
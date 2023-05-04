
def completeaza(stare_de_plecare):
    global d,alfabet
    cifre = ""
    dict = {}
    for litera in alfabet:
        dict[litera] = []

    for cifra in str(stare_de_plecare):
        for tranzitie in d[int(cifra)]:
            for litera in alfabet:
                if tranzitie[1] == litera:
                    dict[litera].append(tranzitie[0])
    
    for litera in dict:
        reuniune = ""
        for nr in dict[litera]:
            if int(nr)>0 and str(nr) not in reuniune:
                reuniune+=str(nr)
        if reuniune == "":
            reuniune = dict[litera][0]
        d[stare_de_plecare].append([reuniune,litera])


def completare_stari():
    global d,alfabet
    global stari,cnt
    for stare in stari:
        if stare not in d:
            lista = []
            cnt -= 1
            for litera in alfabet:
                lista.append([cnt,litera])
            d[stare] = lista
            lista = []
            for litera in alfabet:
                lista.append([cnt, litera])
            d[cnt] = lista
        else:
            pos_cnt = cnt - 1
            ok1 = False
            for litera in alfabet:
                ok = False
                for tranzitie in d[stare]:
                    if tranzitie[1] == litera:
                        ok = True
                if ok == False:
                    ok1 = True
                    d[stare].append([pos_cnt,litera])
            lista = []
            for litera in alfabet:
                lista.append([pos_cnt, litera])
            d[pos_cnt] = lista
            if ok1 == True: cnt -=1


def gata():
    global d
    lungime = 0
    for el in d:
        lungime = len(d[el])
        if lungime>=2:
            for i in range(0,lungime-1,1):
                for j in range(i+1, lungime,1):
                    if d[el][i][1] == d[el][j][1] : return False
    for el in d:
        if d[el] == []:
            return False
    return True

def stare_noua(tranzitie1, tranzitie2):
    nume_stare = str(tranzitie1[0]) + str(tranzitie2[0])
    stare = [nume_stare, tranzitie1[1]]
    return stare


def mai_multe_litere(lista_tranzitii):
    for i in range(0,len(lista_tranzitii)-1):
        for j in range(i+1, len(lista_tranzitii)):
            if lista_tranzitii[i][1] == lista_tranzitii[j][1]:
                return i,j
    return 0,0
        

d = {}
alfabet = ""
cnt = 0

#citiere 

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

    lista = []
    lista.append(nod_sosire)
    lista.append(litera)

    if litera not in alfabet:
        alfabet+=litera

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
    print(stare,d[stare])


completare_stari()

print()
print()
print()


while gata() == False:
    
    for stare_de_plecare in d:
        if len(d[stare_de_plecare]) > 1:
            stare1,stare2 = mai_multe_litere(d[stare_de_plecare])
            if stare1 != stare2:
                stare = stare_noua(d[stare_de_plecare][stare1],d[stare_de_plecare][stare2])
                d[int(stare[0])] = []
                del d[stare_de_plecare][stare1]
                del d[stare_de_plecare][stare2-1]
                d[stare_de_plecare].append(stare)
                break
    

    for stare_de_plecare in d:
        if d[stare_de_plecare] == []:
            completeaza(stare_de_plecare)
                

lista = []
for stare in stari_finale:
    for stare_ in d:
        if int(stare) != int(stare_) and str(stare) in str(stare_):
            lista.append(stare_)
for el in lista:
    stari_finale.append(el)


for stare in d:
    print(stare,d[stare])


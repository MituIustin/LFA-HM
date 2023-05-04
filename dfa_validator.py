d = {}


def verificare_cuvant( cuvant ):
    global d
    global stare_initiala
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

linie = f.readline()
linie = linie[:-1]
nr_cuvinte = int(linie)

lista_cuvinte = []
for i in range(nr_cuvinte):
    linie = f.readline()
    if linie[-1] == "\n": 
        linie = linie[:-1]
    lista_cuvinte.append(linie)

f.close()


f = open("output.txt","w")
for cuvant in lista_cuvinte:
    if verificare_cuvant(cuvant) == True:
        f.write("DA\n")
    else:
        f.write("NU\n")
f.close()
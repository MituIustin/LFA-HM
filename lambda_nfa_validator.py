d = {}


def verificare_cuvant(cuvant,stare_curenta, poz):
    global d
    global stare_initiala
    global stari_finale
    global ok
    
    if poz == len(cuvant)-1 and stare_curenta in stari_finale: ok = True
    if poz< len(cuvant):

        litera = cuvant[poz]

        if stare_curenta in d:
            for x in d[stare_curenta]:
                if x[1] == litera:
                    verificare_cuvant(cuvant, x[0], poz+1)
                if x[1] == "λ":
                    verificare_cuvant(cuvant, x[0],poz)
    

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
ok = False
for cuvant in lista_cuvinte:
    ok = False
    verificare_cuvant(cuvant,stare_initiala, 0)
    if ok == True: f.write("DA\n")
    else: f.write("NU\n")

f.close()
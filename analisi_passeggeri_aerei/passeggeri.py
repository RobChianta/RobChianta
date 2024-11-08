dizVoliAerei = {}

# campi file csv
with open('passeggeri.txt','r',) as f:
    onerow = f.readline().strip()

    #print(onerow)

    header = onerow.split(',')
    count = sum(map(len, (s.split(',') for s in header)))
    #print("num colonne = ",count)

    # leggo il resto del file e lo carico in un dizionario
    index=1
    for line in f:
        #print("line : ",line.strip())
        dizVoliAerei.setdefault(index,[])
        #dizVoliAerei[index].append(line.strip())
        dizVoliAerei[index] = line.strip()
        index = index+1

#
#for k in dizVoliAerei.items():
    #print(k)

# loop nel dizionario dei voli per creare un nuovo dizionario dove la chiave e' la destinazione
# e come valore l' eta' media dei passeggeri
index = 1
dizCittaOrig = {}
for k,v in dizVoliAerei.items():
    pippo = v.split(',')
    #print(pippo[3])
    #print(pippo[1])

    test = False
    for v,k in dizCittaOrig.items():
        #print(k)
        if k == pippo[3]:
            test = True     # chiave gia' presente

    #print(test)
    if test == False:
        dizCittaOrig.setdefault(pippo[3],[])
        dizCittaOrig[pippo[3]].append(pippo[1])
        index = index + 1
    else :
        # in questo caso aggiungo il valore dell' eta a quello gia' esistente
        print("index = ", index, " pippo[1] : ", pippo[1]," pippo[3] : ", pippo[3])
        eta = pippo[1]
        dizCittaOrig.setdefault(pippo[3],[]).append(pippo[1])

#print(dizCittaOrig)
print("Media dell'età per ciascuna origine\r")
for k,v in dizCittaOrig.items():
    totale = sum(map(int,v))/len(v)
    print("\tOrigine : ",k, " Media eta' ", round(totale,1) )
    #print(v)
    #for valore in v:
        #print("key : ",k," valore : = ", valore)


dizNumVolo = {}
for k,v in dizVoliAerei.items():
    numv = v.split(',')

    test = False
    for v,k in dizNumVolo.items():
        #print(k)
        if k == numv[5]:
            test = True     # chiave gia' presente

    if test == False:
        dizNumVolo.setdefault(numv[5],[])
        dizNumVolo[numv[5]].append(numv[2])
        index = index + 1
    else :
        # in questo caso aggiungo il valore dell' eta a quello gia' esistente
        print("index = ", index, " numv[5] : ", numv[5])
        dizCittaOrig.setdefault(numv[5],[]).append(numv[2])

#print(dizNumVolo)
#print(max(dizNumVolo, key=dizNumVolo.get))
maxVolo = max(dizNumVolo, key=dizNumVolo.get)
#print(maxVolo)
value = dizNumVolo.get(maxVolo)
#print(value)
#print(value.count("M"))
#print(value.count("F"))

print("\nNumero di volo piu' popolare:\n\t\t",maxVolo,", Passeggeri M:",value.count("M")," / ",value.count("F"))

'''
# Leggere un file csv senza usare librerire esterne
#
def readParksFile(fileName="national_parks.csv"):
    with open(fileName) as infile:
        column_names = infile.readline()
        keys = column_names.split(",")
        number_of_columns = len(keys)
        list_of_dictionaries = []
        data = infile.readlines()
        list_of_rows = []
        for row in data:
            list_of_rows.append(row.split(","))
        infile.close()
        for item in list_of_rows:
            row_as_a_dictionary = {}
            for i in range(number_of_columns):
                row_as_a_dictionary[keys[i]] = item[i]
            list_of_dictionaries.append(row_as_a_dictionary)

    for i in range(len(list_of_dictionaries)):
        print(list_of_dictionaries[i])
'''

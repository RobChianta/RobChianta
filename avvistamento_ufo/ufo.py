import re


# input : 
#   separatore dati csv : char 
#   1) paese (integer : indica la posizione nel record csv)
#   2) durata (integer : indica il num di scondi dell' avvistamento)
#   3) descrizione (string : descrizione avvistamento)
#   4) forma (string : descrizione UFO)

debug = 0

# si deve inserire solo un carattere
while True:
    separatore = input("separatore dati csv : ")
    if (len(separatore) == 1):
        break
    print("un solo carattere")

# dati per censire le colonne del file csv
paese = input("colonna paese : ")
forma = input("colonna forma : ")
durata = input("colonna durata : ")
descr = input("colonna descrizione : ")

#if (debug == 1) :
    #print("[D] colonna paese : ",paese)
    #print("[D] colonna durata : ",durata)
    #print("[D] colonna descrizione : ",descr)
    #print("[D] colonna forma : ",forma)

# calcolo il numero di colonne : numero di occorrenze del separatore + 1
# leggo solo la prima riga del file
with open('ufo.csv', 'r') as f:
    contents = f.readline()

    #if (debug == 1) :
        #print("[D] riga : ",contents)

    nc = contents.count(separatore) + 1
    print("num colonne : ",nc);

f.close()

#if (debug == 1) :
    #value = contents.split(separatore)
    #print(value)

#stato = contents.split(separatore,3)[2]
#stato = contents.split(separatore,int(paese))[int(paese) - 1]   # base 0

# 1)
# ricerca dello Stato con il maggior numero di avvistamenti
# Utilizzo il valore in input : paese = input("colonna paese : ")
dizionario = {}

with open('ufo.csv', 'r') as f:
    for line in f:
        #stato = line.split(separatore,3)[2]
        stato = line.split(separatore,int(paese))[ int(paese) - 1 ]   # base 0
        if stato in dizionario:
            dizionario[stato] += 1
        else:
            dizionario[stato] = 1

f.close()

if (debug == 1) :
    print("Dizionario : ",dizionario)

maxStato = max(dizionario, key=dizionario.get)
print("Stato con il maggior numero di avvistamenti : ", maxStato)

# fine ricerca Stato


# 2)
# ricerca durata, avvistamento e forma

dizionario = []
maxDurata = 0

with open('ufo.csv', 'r') as f:
    for line in f:
        #print("riga : ",line)
        #tempo = line.split(separatore,5)[ 5 - 1 ]   # base 0
        tempo = line.split(separatore,int(durata))[ int(durata) - 1 ]   # base 0

        if int(tempo) > maxDurata:
            dizionario.clear()
            maxDurata = int(tempo)

            valForma = line.split(separatore,int(forma))[ int(forma) - 1 ]   # base 0
            valAvv = line.split(separatore,int(descr))[ int(descr) - 1 ]   # base 0

            dizionario.append({
                "durata":maxDurata,
                "forma":valForma,
                "avvistamento":valAvv
                })

f.close()

#print("Dizionario : ",dizionario)
#print("Avvistamento con durata piu' lunga : ", maxDurata)
print("Avvistamento con durata piu' lunga : ", dizionario[0]["avvistamento"], " (durata : ",dizionario[0]["durata"]," secondi, Forma : ",dizionario[0]["forma"], ")")



# split string
#date, time, event_name = ev.get_text(separator='@').split("@")

#texts = ["a __ b", "c__d__e", "f  __ g"]
#pattern = re.compile(r"\s*__\s*")
#[pattern.split(s) for s in texts]  
#output >>>> [['a', 'b'], ['c', 'd', 'e'], ['f', 'g']]

#   import numpy as np
#   arr = np.chararray((rows, columns))

#dict_example = {'a': 1, 'b': 2}
#
#print("original dictionary: ", dict_example)
#
#dict_example['a'] = 100  # existing key, overwrite
#dict_example['c'] = 3  # new key, add
#dict_example['d'] = 4  # new key, add
#
#print("updated dictionary: ", dict_example)



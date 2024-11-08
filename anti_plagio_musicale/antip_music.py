import sys
import operator

# Promemoria 
#
# Plagio : confronto riga con riga in modalita' stringa
# Copiatura : substring[4], si parte dall' inizio e poi si aggiorna la substring[] di una posizione
# Sospetto : trasposta in alto/basso, converto le note in integer e poi eseguo controllo come in copiatura

# Si confronta un brano con quello/i 'precedenti'. Quindi il primo brano NON ha precedente !??


current = ""
previous = ""
dizBrani = {}
index = 1

# carico il file in un dizionario key:value  (nome brano : note brano)
with open('brani.txt', 'r') as f:
    for line in f:
        nomeBrano = line.split(':')[0]
        noteBrano = line.split(':')[1]
        dizBrani.setdefault(index, [])
        dizBrani[index].append(nomeBrano)
        dizBrani[index].append(noteBrano)
        index = index + 1

#print("Tot brani : ",index)
#for k,v in dizBrani.items():
    #print(k)
    #print("nome : ",v[0])
    #print("note : ",v[1].rstrip())
    #break

# ciclo principale sul dizionario
for idx in range(2,index):
    #print("idx : ",idx)

    currentNome = dizBrani[idx][0]
    currentNote = dizBrani[idx][1]
    #print("currentNome : ", currentNome, " currentNote : ",currentNote)

    # si devono effettuare 3 controlli :
    # 1)    PLAGIO
    # adesso confronto 'current' con quelli precedenti.....
    #for ptr in range(idx-1, 0, -1):   # loop in reverse mode
    for ptr in range(1, idx):   # loop in reverse mode
        prevNome = dizBrani[ptr][0]
        prevNote = dizBrani[ptr][1]
        #print("back : ",ptr, " [prevNome : ",prevNome,"] [prevNote : ",prevNote.rstrip(),"]")
   
        if prevNote == currentNote:
            print(currentNome," PLAGIO di ",prevNome)
            continue    # se e' un Plagio non serve fare i controlli su Copiatura e Sospetto (e' 100% identica)

        # substring[4] da cercare nei brani precedenti (ciclo for reverse)

        # 2) COPIATURA
        currentNote.rstrip().strip()
        start = 0
        end = 5

        stop = 0

        # stringa da analizzare
        start1 = 1
        nc1 = 12

        # stringa campione
        start2 = 1
        nc2 = 12

        s2 = currentNote[:-1]
        s1 = prevNote[:-1]

        while stop == 0:
            temp2 = s2[start2:nc2]  # substring campione
            l2 = temp2.split(' ')

            if len(l2) < 4:
                #print("substring < 4")
                break

            # cerco substring[s2] in tutta la stringa s1
            start1 = 1

            while stop == 0:
                temp1 = s1[start1:nc1]  # substring da controllare
                l1 = temp1.split(' ')

                if l1 == l2:
                    #print(currentNome+" COPIATURA : traccia copiata = "+str(l2)+" da "+prevNome)
                    print(currentNome," e' una COPIATURA da",prevNome)
                    stop = 1    # trovato COPIATURA

                start1 = start1 + 3
                if start1 > len(s1):
                    break

                nc1 = nc1 + 3

            start2 = start2 + 3
            nc2 = nc2 + 3

            if start2 > len(s2):
                stop = 1


        # 3) SOSPETTO

        aa = currentNote[:-1]
        bb = prevNote[:-1]

        zeta = aa.strip().split(' ')
        kappa = bb.strip().split(' ')
        #print(currentNote)
        #print(zeta)
        #print(kappa)
        #print(len(b))

        # devo scorrere [b] a blocchi di 4 valori
        start1 = 0
        end1 = 4
        step = 4

        while end1 <= len(zeta):
            #print(zeta[start1:end1])
            substr1 = zeta[start1:end1]
            substr2 = kappa[start1:end1]

            #print("substr1 = ",substr1)
            #print("substr2 = ",substr2)
            #print("-----------------------------------")

            substr1int = list(map(int,substr1))
            substr2int = list(map(int,substr2))
            sottraz = (list(map(operator.sub,substr1int,substr2int)))
            summa = sum(sottraz)
            #print("sottraz : ",sottraz,"-->",summa)
            if summa == 0:
                break

            uguali = sottraz[1:] == sottraz[:-1]
            if uguali:
                print(currentNome," e' un SOSPETTO di ",prevNome)
                break

            start1 = start1 + step
            end1 = end1 + step

            if end1 > len(kappa):
                break

       # sys.exit()





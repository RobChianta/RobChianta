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

'''
print("Tot brani : ",index-1)
for k,v in dizBrani.items():
    print(k,")\tnome : ",v[0])
    print("\tnote : ",v[1].rstrip())

'''

# ciclo principale sul dizionario
for idx in range(2,index):
    #print("idx : ",idx)

    currentNome = dizBrani[idx][0]
    currentNote = dizBrani[idx][1]
    #print("currentNome : ", currentNome.strip(), " currentNote : ",currentNote.strip(),"  viene confrontato con :: ")
    #print("currentNome : ", currentNome.strip(), "  viene confrontato con :: ")

    #for ptr in range(idx-1, 0, -1):   # loop in reverse mode
    for ptr in range(1, idx):   # loop in reverse mode
        prevNome = dizBrani[ptr][0]
        prevNote = dizBrani[ptr][1]
        #print("back : ",ptr, " [prevNome : ",prevNome,"] [prevNote : ",prevNote.rstrip(),"]")
        #print(" [prevNome : ",prevNome,"]")
        if prevNote == currentNote:
            print(currentNome," PLAGIO di ",prevNome)
            continue    # se e' un Plagio non serve fare i controlli su Copiatura e Sospetto (e' 100% identica)

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
                    print(currentNome+" e' una COPIATURA di "+prevNome)
                    stop = 1    # trovato COPIATURA

                start1 = start1 + 3
                if start1 > len(s1):
                    break

                nc1 = nc1 + 3

            start2 = start2 + 3
            nc2 = nc2 + 3

            if start2 > len(s2):
                stop = 1


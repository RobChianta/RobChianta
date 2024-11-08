import sys

#s1 = " 72 71 69 67 65 64 62 60 72 71 69 67 65 64 62 60"
#s2 = " 60 62 64 65 67 69 71 72 71 69 67 65 64 62 60"

#s2 = " 72 71 69 67 65 64 62 60 72 71 69 67 65 64 62 60"
#s1 = " 60 62 64 65 67 69 71 72 71 69 67 65 64 62 60"

s2 = " 72 71 69 67 65 64 62 60 72 71 69 67 65 64 62 60"
s1 = " 60 60 60 60 60 60 60 60 60"


# ogni sottostringa[4] di s2 va cercata in tuttta s1
# la substring e' di 8 caratteri perche' ci sono anche i blank

#print("len s1[] : ", len(s1))
#print("len s2[] : ", len(s2))

stop = 0

# stringa da analizzare
start1 = 1
nc1 = 12

# stringa campione
start2 = 1
nc2 = 12

while stop == 0:
    temp2 = s2[start2:nc2]  # substring campione
    l2 = temp2.split(' ')
    print("l2 : ",l2)
    if len(l2) < 4:
        print("substring < 4")
        break

    # cerco substring[s2] in tutta la stringa s1
    start1 = 1
    while stop == 0:
        temp1 = s1[start1:nc1]  # substring da controllare
        l1 = temp1.split(' ')
        #print(temp1)

        if l1 == l2:
            print("copiatura : traccia copiata = ",l2)
            stop = 1    # trovato COPIATURA

        start1 = start1 + 3
        if start1 > len(s1):
            break

        nc1 = nc1 + 3

    start2 = start2 + 3
    nc2 = nc2 + 3

    #start1 = start1 + 12
    #nc1 = nc1 + 12
    #print("start : ",start)
    if start2 > len(s2):
        stop = 1


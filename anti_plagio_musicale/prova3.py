import sys
import operator


a1 = "60 60 60 60 60 60 60 60 60"
b1 = "79 69 79 49 69 69 69 69 69 69 69"
#b = ['69','79','89','99','19','29','39','49','59','69','79']

#print(len(a))
#print(len(b))

a = a1.split(' ')
b = b1.split(' ')

# devo scorrere [b] a blocchi di 4 valori
stop = 0
start = 0
nc = 4
while stop == 0:
    t = b[start:nc]
    if len(t) < 4:
        stop = 1
        break

    print("t = " + str(t))

    # adesso ho una substr[4], devo convertirla in INT, e poi scorrere a[] alla ricerca di 4 valori trasposti
    str2int = list(map(int,t))
    print("int : " + str(str2int))

    # per ogni substr str2int[] vado a controllare in a[] a blocchi di 4 elementi
    astart = 0
    anc = 4
    while stop == 0:
        aa = a[astart:anc]
        if len(aa) < 4:
            break

        #print("aa : " + str(aa))
        aa2int = list(map(int,aa))
        # adesso faccio sottrazione fra str2int[] e aa2int
        sottraz = (list(map(operator.sub,str2int,aa2int)))
        uguali = sottraz[1:] == sottraz[:-1]
        if uguali:
            print("SOSPETTO !!")
            stop = 1
            break

        astart = astart + 1
        anc = anc + 1

    start = start + 1
    nc = nc + 1
    #if start > len(b):
        #stop = 1

sys.exit()


#a = ['60','60','60','60','60','60','60']
#a = ['60','60','60','60']
a = ['69','69','69','69','69','69','69','69','69','69','69']

#b = ['65','65','65','65']
b = ['60','60','60','60','60','60','60']

aa = list(map(int,a))
bb = list(map(int,b))

px = 0
x = 0
uguale = 1
for i in range(len(bb)):
    x = (bb[i] - aa[i])
    if i != 0:
        if x != px:
            px = x
        else:
            uguale = uguale + 1

if uguale == 4:
    print("SOSPETTO")

    #print(bb[i] - aa[i])


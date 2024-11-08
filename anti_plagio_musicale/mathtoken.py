import operator

t = "72 74 76 77 79 81 83 84"
w = "60 62 64 65 67 69 71 72 71 69 67 65 64 62 60"

zeta = t.split()    # zeta[] e' la stringa da analizzare per capire se e' sospetta
kappa = w.split()   # kappa[] e' la stringa originale

#print(zeta)
#print(kappa)

start1 = 0
end1 = 4
step = 4

while end1 <= len(zeta):
    #print(zeta[start1:end1])
    substr1 = zeta[start1:end1]
    substr2 = kappa[start1:end1]

    print("substr1 = ",substr1)
    print("substr2 = ",substr2)
    print("-----------------------------------")

    substr1int = list(map(int,substr1))
    substr2int = list(map(int,substr2))
    sottraz = (list(map(operator.sub,substr1int,substr2int)))

    uguali = sottraz[1:] == sottraz[:-1]
    if uguali:
        print("SOSPETTO")
        break

    start1 = start1 + step
    end1 = end1 + step

    if end1 > len(kappa):
        break

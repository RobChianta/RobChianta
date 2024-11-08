import operator
a = [2,2,2]
b = [1,1,1]
c = map(operator.sub, a, b)

zeta = (list(map(operator.sub,a,b)))
print(zeta)

uguali = zeta[1:] == zeta[:-1]
print("check = " , uguali)

#print(list(map(operator.sub,a,b)))

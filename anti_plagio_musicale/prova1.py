import sys

s1 = " 72 71 69 67 65 64 62 60 72 71 69 67 65 64 62 60"
s2 = " 60 62 64 65 67 69 71 72 71 69 67 65 64 62 60"

# cerco sottostringa[4] di s2 in s1
# la substring e' di 8 caratteri perche' ci sono anche i blank

#print("len s1[] : ", len(s1))
#print("len s2[] : ", len(s2))

s3 = '12 34 56 78 12 34'

start = 0
end = 5
#temp = s3[0:3]
temp = s3[start:end]
l1 = temp.split(' ')
print(temp)
print(l1)

start = start + 3
end = end + 3
#temp = s3[3:6]
temp = s3[start:end]
print(temp)

start = start + 3
end = end + 3
#temp = s3[3:6]
temp = s3[start:end]
print(temp)

start = start + 3
end = end + 3
#temp = s3[3:6]
temp = s3[start:end]
l9 = temp.split(' ')
print(temp)


start = start + 3
end = end + 3
temp = s3[start:end]
l2 = temp.split(' ')
print(temp)
print(l2)

if l1 == l2:
    print("sono uguali")

if l1 == l9:
    print("sono uguali")
else:
    print("sono diversi")

sys.exit()

stop = 0

# stringa da analizzare
start1 = 0
nc1 = 12

# stringa campione
start2 = 0
nc2 = 12

while stop == 0:
    temp2 = s2[start2:nc2]  # substring campione
    print(temp2)

    temp1 = s1[start1:nc1]  # substring da controllare
    #print(temp1)

    if temp1 == temp2:
        print("copiatura")
        stop = 1    # trovato COPIATURA

    start2 = start2 + 12
    nc2 = nc2 + 12

    start1 = start1 + 12
    nc1 = nc1 + 12
    #print("start : ",start)
    if start2 > len(s2):
        stop = 1


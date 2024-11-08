def main():

# get the user msg
    print("this program tells you how many words are in your sentence.")
    a = "nome_passeggero,eta,sesso,origine,destinazione,numero_volo"
    b = a.split(',')
    #print(b)
    #a = ['je mange.',' je suis là au bain','gyu est là']

    count = sum(map(len, (s.split(',') for s in b)))

    print("count = ",count)

main()

from random import randint
a=randint(1,100)
b=0
while True:
    while b!=a:
        b=int(input("Choisez un nombre entre 1 et 100 : "))
        if b>a:
            print("Ton nombre est trop haut. Réessaye")
        elif b<a:
            print("Ton nombre est trop bas. Réssaye")
        print("Bravo tu as trouvé le bon nombre")
    c=input("Rejouez ? ")
    if c==True :
        print("Continuez")
    else:
        break
print("C'est fini!")
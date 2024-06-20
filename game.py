# 1st game in french seek and find the number
g=int(input("à quel jeu veut tu jouer ?"))
if g==1:
    while True:
        from random import randint
        r1=int(input("jusqu'à combien voulez vous cherchez ?"))
        try1=int(input("combien d'essaie voulez-vous faire ? "))
        try2=0
        a=randint(1,r1)
        b=0
        while b!=a & try1<=try2:
            b=int(input("Choisez un nombre entre 1 et ",r1," : "))
            try2=tyr2+1
            if b>a:
                print("Ton nombre est trop haut. Réessaye")
            elif b<a:
                print("Ton nombre est trop bas. Réssaye")
        if try1>try2:
            print("t'as ton compte d'essai")
        else:
            print("Bravo tu as trouvé le bon nombre")
        c=input("Rejouez ? ")
        if c==True :
            print("On continue")
        else:
            break
    print("C'est fini!")
else:
# 2nd game 
    while True:
        from random import randint
        r1=int(input("jusqu'à combien voulez vous cherchez ?"))
        try1=int(input("combien d'essaie voulez-vous faire ? "))
        try2=0
        a=randint(1,r1)
        b=0
        while b!=a & try1<=try2:
            b=int(input("Choisez un nombre entre 1 et ",r1," : "))
            try2=tyr2+1
            if b<r1+20 or b>r1-20:
                print("tu es proche")
            if b==a:
                print("bravo tu a touvé le bon nombre") 
        c=input("Rejouez ? ")
        if c==True :
            print("On continue")
        else:
            break
    print("C'est fini!")
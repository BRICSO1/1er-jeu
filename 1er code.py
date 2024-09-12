# # #exemple
# # A= float(input("Un nombre : "))
# # print(A)
# # B= input("Un autre nombre : ")
# # print(B)
# # M=(A+B/2)

# # # exercice 2

# # N=int(input("nombre de personne =" ))
# # if N < 5:
# #     P=N*220+800
# # else:
# #     P=N*180+800
# # print('le prix est de ',P)

# # # exercice 3

# N= int(input("nombre de jours ="))
# P= N*10+250 
# Q=N*5+300
# if Q==P:
#     print ("Les deux logements sont égaux")
# else : 
#     if P<Q:
#         print ('Le logement A est plus avatageux avec',(Q-P), '€ de différence avec le logement B')
#     else :
#         print ('Le logement B est plus avantageux avec',(P-Q),'€ de différence avec le logement A')

# # exercice 4

# x=(int(input("x=")))
# if x%3==0:
#     Y=x/3
# else:
#     Y=x-3
# print(Y)



# # #fiche 4



# # # exo 1

# # P=int(input("sur combien d'année voulez-vous l'augementation ?  "))
# # N=2300
# # NO=P*150
# # for i in range(P):
# #     N=N+150
# # print ("Il y a" ,N,"habiants et il y a ",NO,"nouveau habitants")

# # # exo 2

# # S=int(input("Combien de samedi d'etrainement? "))
# # D=25
# # T=25
# # if S>12:
# #     print("Le programme d'entrâinment est passé !")
# # else :
# #     for i in range(1,S):
# #         D=D+11
# #         T=T+D
# #     print("La distance que vous avez parcouru est de ",T,"km et la distance du jour est",D,"km.")

# # # exo 3

# # B1=int(input("Quel est votre budjet : "))
# # N=int(input("Au bout de combien d'année voulez vous voir votre budjet : "))
# # BT=B1
# # for i in range(N-1):
# #     B1=B1*(1-5/100)
# #     BT=B1+BT
# # print("Le budget du loisir est de ",B1,"€ et le budjet total est de ",BT,"€")

# # fiche 5

# # exemple
# # H=90
# # R=0
# # while H>=1:
# #         H=3/5*H
# #         R=R+1
# #         print(R,H)

# # exercice 1
# # S=3000
# # A=2014
# # while S<=3500:
# #         S=S*1.03
# #         A=A+1
# # print(A)

# # # exercice 2

# # L=8
# # N=0
# # while L<=12:
# #   L=L*1.05
# #   N=N+1
# # print (N)

# # exercice 3

# # M=int(input("jusqu'à combien d'euros voulez-vous écononomiser ? "))
# # E=float(input("combien d'euros avez vous gagné ? "))
# # T=E
# # A=2015
# # while T<M:
# #     E=E+5
# #     T=T+E
# #     A=A+1
# # print ("En ",A,", vous avez gagné ",E,"€ et vous aurait en stock",T,"€ de plus vous aurait",T-M,"€ de plus")

# # def g(x):
# #     y=0-2*(x**2)+(5*x)+3
# #     print(y)
# # g(-2)
# # def f(x):
# #     return 3*x**2+25*x-18
# # print(f(1))

# # def moyenne2 (x,y):
# #     z=(x+y)
# #     z=z/2
# #     print(z)

# # def moyenne3(a,b,c):
# #     d=a+b+c
# #     d=d/3
# #     return (d)

# # def min(M,N):
# #     if M>N:
# #         print(N)
# #     else:
# #         print(M)
# # def max(M,N):
# #     if M<N:
# #         print(N)
# #     else:
# #         print(M)

# def valeur_absolue(x):
#     if x<0:
#         x=x*(-1)
#         print(x)
#     else:
#         print(x)


# valeur_absolue(-879)

def image(x):
    y=4*(x**2)-5
    print(y)

image(4)

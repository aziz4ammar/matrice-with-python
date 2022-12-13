def saisir ():
    global n
    test=False
    while test==False:
        n=int(input("n="))
        test=2<n<10
def remplir(M,n):
    for i in range (n):
        for j in range (n):
            M[i,j]=int(input("M["+str(i)+","+str(j)+"]="))
def afficher(M,n):
    for i in range(n):
        for j in range(n):
            print(M[i,j],end="|")
        print("\n")























#p.p
import numpy as np
saisir()
M=np.array([[int()]*n]*n)
remplir(M,n)
afficher(M,n)

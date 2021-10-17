'''
Fait par Splyder, le 16/10/2021 
'''
#Conjecture de Syracuse
#ou Conjecture de Collatz
#ou Conjecture d'Ulam
#ou probleme 3x+1

#cette fonction permet de tester la conjecture de syracuse pour un nombre donne.

def syracuse(number:int,log:bool=True)->bool:
    z=0
    while number!=1 and number>1:
        if bin(int(number))[-1]=="0":
            if log==True:print(number,"/2=",number/2)
            number=number/2
            z+=1
        else:
            if log==True:print(number,"*3+1=",number*3+1)
            number=number*3+1
            z+=1
    if z<10000:return True
    else:return False

#fonction qui permet de tester la fonction ci-dessus.
def test(n1:int,n2:int)->None:
    for i in range(n1,n2):
        x=syracuse(i,False)
        if x==True:
            print(i)

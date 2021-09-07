from random import *

#generateur de nombre aléatoire enre deux bornes
print("Choisissez le minimum et le maximum (compris entre 1 et 36")

verifmin=0
verifmax=0
inf=1
sup=36

while verifmin==0:
    min=int(input())
    if (min > inf) and (min < sup):
        verifmin=1
    else:
        print("Nombre invalide veuillez ressaisir le minimum")
    


while verifmax==0:
    max=int(input())
    if (max < sup) and (max > inf):
        verifmax=1
    else:
        print("Nombre invalide veuillez ressaisir le maximum")

if min>max:
    temp=min
    min=max
    max=temp



nombre = randint(min,max)
print (nombre)

# je n'ai' pas compris ce que vous attendiez en indiquant range.
import math
C=int(input("A"))
D=int(input("B"))
E= C/D
if E-math.floor(E)==0:
    print('A is divisible over B')
else:
    print('A not  divisible over B')
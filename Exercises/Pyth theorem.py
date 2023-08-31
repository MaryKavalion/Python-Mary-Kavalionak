print ("Please insert the values for cathesis och hypothenusa. Assign 0 to the side you want to compute ")
cath1 = int (input ("Cathetus 1 = "))
cath2 = int (input ("Cathetus 2 = "))
hyp = int (input ('Hypothenuse = '))

import math

def FindCath (cath, hyp):
    cathetus = math.sqrt(hyp**2 - cath**2)
    print (f"If hypothenuse is {hyp} and one of the cathetis is {cath}, then the other cathetus is {'%.1f' % cathetus}")

if hyp == 0:
    hypot = math.sqrt(cath1**2 + cath2**2)
    print (f"If cathetus 1 is {cath1} and cathetus 2 is {cath2}, the hypothenuse is {hypot}")
elif cath1 == 0:
    FindCath (cath2, hyp)
elif cath2 == 0:
    FindCath (cath1, hyp)
else:
    print ("Wrong input")
    

    
# -*- coding: utf-8 -*-

import math
x = int(input("ingresar valor de x"))
print("\n1.seno\n2.coseno\n3.tangente")
opcion = int(input("\t\tIngresar opcion: "))
while(opcion !=7):
  if(opcion==1):
    print("el seno de x!:" + str(math.sin(x)))
  elif(opcion==2):
    print("el coseno de x!" + str(math.cos(x)))
  elif(opcion==3):
    print("la tangente de x!" + str(math.tan(x)))
  else:
    break
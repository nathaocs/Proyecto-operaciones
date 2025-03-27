import math
def logaritmo (a):
    operacion=math.log(a)
    return operacion
def logaritmo2 (a, b):
    operacion1=math.log(a, b)
    return operacion1
a=int(input("ingrese valor:"))
b=int(input("ingrese valor:"))
print("el logaritmo en base 10 es",logaritmo(a))
print("el logaritmo es",logaritmo2(a,b))
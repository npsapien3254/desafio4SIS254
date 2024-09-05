import math
#Valor a estimar
x = 3
#Valor-punto base
a = 1
#Diferencia
h = x-a
#Variable para almacenar la suma
s = 0
#Valor real
valorReal = 25*x**3-6*x**2+7*x-88 
#vector para almacenar funciones derivadas evaluadas en a
res = [0]*5
#funcion evaluada: 25x^3-6x^2+7x-88
res[0] = 25*a**3-6*a**2+7*a-88
#primera derivada: 75x^2-12x+7
res[1] = 75*a**2-12*a+7
#segunda derivada: 150x-12
res[2] = 150*a-12
#tercera derivada: 150
res[3] = 150
#cuarta derivada: 0
res[4] = 0
""" Iteracion en el vector y operar cada valor con su respectiva
potencia y factorial """
print(f'Valor obtenido | Error relativo porcentual')
for i in range(0, len(res)):
    s+=((res[i])/math.factorial(i))*h**i
    e = abs(((s-valorReal)/valorReal)*100)
    print(f'{s} | {e}')

print(f'Valor estimado obtenido: {s}')
print(f'Valor real: {valorReal}')

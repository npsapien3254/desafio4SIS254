import sympy as sp
#Declarando variables de la funcion
n, B, H, s = sp.symbols('n B H s', real=True, positive = True)
#Valores de las variables
nv = 0.03
sv = 0.0003
Bv = 20
Hv = 0.3
#Funcion
Q = (1/n)*((B*H)**(5/3))/((B+(2*H))**(2/3))*(s**(1/2))
#Resultado de Q
rQ = (1/nv)*((Bv*Hv)**(5/3))/((Bv+(2*Hv))**(2/3))*(sv**(1/2))
#Derivadas parciales respecto a cada variable n, s
dn = sp.diff(Q,n).subs({n:nv, s:sv, B:Bv, H:Hv})
ds = sp.diff(Q,s).subs({n:nv, s:sv, B:Bv, H:Hv})
#rango de error para ambas varibles
re = 1/10
#error de las variables
en = nv*re
es = sv*re
#Calculo del error
eQ = (dn*en)+(ds*es)
#Muestra del rango de Q
print(f'Valor calculado de Q: {rQ}')
print(f'Rango de Q: {rQ-eQ}, {rQ+eQ}')
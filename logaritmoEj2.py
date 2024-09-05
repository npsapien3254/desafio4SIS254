#Importar biblioteca que permite derivar funciones
import sympy as sp
#Valor a estimar
x = 2.5
#Valor-punto base
a = 1
#Diferencia
h = x-a
#Variable para almacenar la suma
s = 0

#Definir la variable a evaluar
exp = sp.symbols('x', real=True)
#Definir la función
f_exp = sp.log(exp)
#Valor real del valor estimado en la funcion
vR = sp.log(2.5)

print(f'N°| Valor estimado | Error relativo porcentual (%)')
for i in range(0, 8):
    #Derivamos la funcion y se la evalua con el valor de a
    dfe = sp.diff(f_exp, exp, i).subs(exp,a)
    #Se calcula con la diferencia entre x-a y se divide por el factorial correspondiente
    res = (dfe/sp.factorial(i))*h**i
    s+=res
    #Calculo del error relativo para cada valor estimado
    e = abs(((s-vR)/vR)*100)
    print(f'{i} | {s} | {e}')
    
print("""Conclusión: 
      Conforme se vayan incrementando iteraciones, lo que 
      conlleva a seguir derivando la función, el valor estimado se va alejando del
      valor real esperado. Se puede notar que en 2da y 4ta iteracion el valor se acerca un poco al valor real estimado""")

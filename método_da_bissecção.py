# Método da Bissecção #

import math
e = 2.71828

E = float(input("E = ").replace(",",".")) # O resultado da aproximação será o mais perto de "E"

def f(x): # Coloque a função f(x) depois de return
    ####################################

    return 
    # Exemplo: return x**2*e**-x+math.sin(x)-x**3

    ####################################

a = float(input("a = ").replace(",","."))
b = float(input("b = ").replace(",","."))
k = round((math.log(b-a) - math.log(E) / math.log(2.0)))
lista_a, lista_b, lista_x, lista_fa, lista_fb, lista_fx= [],[],[],[],[],[]

for i in range(k+1):
    x=(a+b)/2

    lista_a.append(a)
    lista_b.append(b)
    lista_x.append(x)
    lista_fx.append(f(x))
    lista_fa.append(f(a))
    lista_fb.append(f(b))

    if (f(a)<0 and f(x)<0) or (f(a)>=0 and f(x)>=0):
        a=x
    else:
        b=x

print(f"  ||    a   ||    b   ||    x   ||   f(x)  ||   f(a)  ||   f(b)  ||\n"," ||--------||--------||--------||---------||---------||---------||")
for i in range(len(lista_x)):
    if i!=len(lista_x)-1 and i>0 and abs(lista_fx[i])==min([abs(fx) for fx in lista_fx]):
        print(f"{i} || {lista_a[i]:.8f} || {lista_b[i]:.8f} || ({lista_x[i]:.8f}) ||  ({lista_fx[i]:.8f}) ||  {lista_fa[i]:.8f} || {lista_fb[i]:.8f} ||") 
        print(f"Solução aproximada = {lista_x[i]} | (f(x) = {lista_fx[i]:.8f})")
        print()
        break
    elif i==len(lista_x)-1:
        print(f"{i} || {lista_a[i]:.8f} || {lista_b[i]:.8f} || {lista_x[i]:.8f} ||  ({lista_fx[i]:.8f}) ||  {lista_fa[i]:.8f} || {lista_fb[i]:.8f} ||") 
        print(f"Solução aproximada = {lista_x[i]} | (f(x) = {lista_fx[i]})")
        print()
    else:
        print(f"{i} || {lista_a[i]:.8f} || {lista_b[i]:.8f} || {lista_x[i]:.8f} ||  ({lista_fx[i]:.8f}) ||  {lista_fa[i]:.8f} || {lista_fb[i]:.8f} ||") 


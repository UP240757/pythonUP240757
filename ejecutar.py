
#Ejercicio 5
#Join A with B and B with A
print("Ejercicio 5:")
A = {19, 22, 24, 20, 25, 26}
B ={19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
B.update(A)
print("A Y B juntos son:", A)
print("B y A juntos es:", B)

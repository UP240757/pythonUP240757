print("Ejercicios de Nivel 1:")
#Ejerciciios de nivel 1:
#Explain the difference between map, filter, and reduce.
print("Ejercicio 1:")
print("La diferencia entre map, filter y reduce es que:")
#map: aplica una funcion a cada elemento de una lista y devuelve una nueva lista con los valores transformados. 
#se usa para modificar elementos.
#ejemplo:
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Lista original:", numeros)
print("Lista de cuadrados:", cuadrados)
#filter: filtra los elementos de una lista segun una condicion, devolviendo solo aquellos que cumplen con el criterio.
#se usa para seleccionar elementos especificos.
#ejemplo:
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Lista original:", numeros)
print("Lista de pares:", pares)
#reduce: aplioca una operacion acumulativa sobre los elementos de una lista, reduciendolo a un solo valor.
#se usa para calcular resultados agregados.
#ejemplo:
from functools import reduce
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print("Lista original:", numeros)
print("Producto de la lista:", producto)




#Ejercicio 2:
#Explain the difference between higher order function, closure and decorator.
print("Ejercicio 2:")
print("La diferencia entre higher order function, closure y decorator es que:")
#higuer order function: funciones que reciben otras funciones como argumentos o que te devuelven una funcion como resultado.
#se usan para escribir codigo mas flexible y reutilizable.
#ejemplo:
def aplicar_funcion(funcion, valor):    
    return funcion(valor)
doble = lambda x: x * 2
resultado = aplicar_funcion(doble, 5)
print("Resultado de aplicar la funcion doble:", resultado)
#closure: funcion que recuerda el entorno en el que se creo, incluso cuando se ejecuta fuera de ese entorno.
# se usa para permitir mantener estados sin necesidad de usar variables globales. 
#ejemplo:
def crear_multiplicador(factor):
    def multiplicador(numero):
        return numero  * factor
    return multiplicador
multiplica_por_3 = crear_multiplicador(3)
print("Resultado de la closure:", multiplica_por_3(5))
#decorator: funcion que modifica el comportamiento de otra funcion sin cambiar su codigo.
#se usa mucho para extender funcionalidades en Python.
#ejemplo:
def decorador(funcion):
    def nueva_funcion():
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")
        return nueva_funcion
@decorador
def saludar():
    print("Hola!")







#Ejercicio 3:
#Define a call function before map, filter or reduce, see examples.
print("Ejercicio 3:")
print("Ejemplo de uso de call function antes de map, filter o reduce:")
#map:
#ejemplo:
names = ['Sandra', 'Aaron', 'Sofia', 'Janize', 'Vanessa']  

def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print("El ejemplo que se uso con map es:", list(names_upper_cased))

#filter:
#ejemplo:








    
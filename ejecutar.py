#Ejercicio 18
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("EJERCICIO 18: ")
def crear_acronimo(frase): 
    palabras = frase.split()
    acronimo= ''.join([palabra[0].upper()for palabra in palabras])
    return acronimo 
frase = "Python For Everyone"
acronimo = crear_acronimo(frase)
print(f"El acronimo de '{frase}' es: {acronimo}")







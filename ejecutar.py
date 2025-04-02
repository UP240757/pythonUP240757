# 1
idiomas_unicos = set()

for pais in paises_dat:
    idiomas_unicos.update(pais['languages'])
print("Numero total de idiomas sin reperir: ", len(idiomas_unicos))

print(" ")

# 2
idiomas = []

for pais in paises_dat:
    idiomas.extend(pais['languages'])    # Este loop recorre todos los paises y añade sus idiomas a una lista llamada "idiomas" usando el operados "extend"

conteo_idiomas = {}   # Creamos un diccionario vacio para guardar los idiomas como claves

for idioma in idiomas:
    if idioma not in conteo_idiomas:     # El "if" aqui pregunta si "idioma" ya esta en el diccionario y el "else" si aun no que lo agrege
        conteo_idiomas[idioma] = 1
    else:
        conteo_idiomas[idioma] += 1

mas_hablados = sorted(conteo_idiomas.items(), key=lambda x: x[1], reverse=True)[:10]

print("Los 10 idiomas mas hablados son: ")
for idioma, frecuencia in mas_hablados:
    print(f"{idioma}: {frecuencia} paises lo tienen cono idioma oficial")


# "conteo_idiomas.items()" nos devuelve una lista en tupla de cada idiuoma y su frecuencia se ve algo asi [('Inglés', 4), ('Árabe', 3), ('Español', 2)] una lista con su "key" y su valor
# "key=lambda x: x[1]" este coso le indica a  que ordene los pares usando el segundo elemento de cada tupla osea el valor, que representa la "frecuencia" en este caso x[0] seria el idioma (key) y x[1] seria la frecuencia (value) en la tupla
# "reverse=True" esto le indica a "sorted()" que ordene en orden descendente (de mayor a menor frecuencia)
# "[:10]" con esto seleccionamos los 10 primeros elementos de la lita ordenada que son los idiomas con mayor frcuencia

print(" ")

# 3
paises_mas_poblados = sorted(paises_dat, key = lambda x: x['population'], reverse = True)[:10]
for pais in paises_mas_poblados:
    print(f"{pais['name']}: {pais['population']} habitantes")

# Usamos la misma logica que el anterior para este codigo


        













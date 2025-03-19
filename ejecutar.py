import paises as p

paises = p.paises
acum = 0

for pais in paises :
    acum = pais['population'] = acum 
    print(pais)
    print(type(pais))
    print(pais['name'])

    print(pais['population'])
print("somos:", acum)
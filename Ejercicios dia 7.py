#Ejercicios Nivel 1
print("Ejercicios Nivel 1:")
#Ejercicio 1
#Find the length of the set it_companies
print("Ejercicio 1:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
longitud_set = len(it_companies)
print("La longitud de set companies es:", longitud_set)

#Ejercicio 2
#Add 'Twitter' to it_companies
print("Ejercicio 2:")
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('Twitter')
print(it_companies)

#Ejercicio 3
#Insert multiple IT companies at once to the set it_companies
print("Ejercicio 3:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter'}
new_companies = {'Instagram', 'Tik Tok', 'WhatsAp', 'Spotify'}
it_companies.update(new_companies)
print("Las multiples companies agregadas son:", it_companies)


#Ejercicio 4
#Remove one of the companies from the set it_companies
print("Ejercicio 4:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'Instagram', 'Tik Tok', 'WhatsAp', 'Spotify'}
it_companies.remove("Facebook")
print("El conjunto de companies sin una es:", it_companies)

#Ejercicio 5
#What is the difference between remove and discard
print("Ejercicio 5:")
#Ejemplo
it_companies = {'Facebook', 'Google', 'Microsoft'}
it_companies.remove('Google') #Eliminar ggogle (funciona)
#remove : elimina el elemento del conjunto. Este es para cuando estas eguro de que este.
# si el elemento no esta genera error.
print("remove: se usa cuando estas seguro de que algo si este y poder eliminarlo")
 #Ejemplo:
it_companies = {'Facebook', 'Google', 'Microsoft'}
it_companies.discard('Google')
it_companies.discard('Tiktok') #Este no xiste en esta lista.
#discard : Este tambien elimina elementos del conjunto.
#Tambien si el elemento no se encuentra no hace nada y no marcara error, 
#lo cual es mas seguro cuando no estas seguro de si existe o no.
print("discard: se usa cuando no estas seguro y evitar errores")




#Exercises: Level 2
print("Ejercicios nivel 2:")
#Ejercicio 1
#Join A and B
print("Ejercicio 1:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print("La union de A Y B es:", A)



#Ejercicio 2
#Find A intersection B
print("Ejercicio 2:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
int_a_b = A.intersection(B)
print("La interseccion de A y B es:", int_a_b)


#Ejercicio 3
#Is A subset of B
print("Ejercicio 3:")


#Ejercicio 4
#Are A and B disjoint sets
print("Ejercicio 4:")


#Ejercicio 5
#Join A with B and B with A
print("Ejercicio 5:")


#Ejercicio 6
#What is the symmetric difference between A and B
#Delete the sets completely
print("Ejercicio 6:")



#Ejercicios Nivel 3
print("Ejercicios nivel 3:")

#Ejercicio 1
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print("Ejercicio 1:")

#Ejercicio 2
#Explain the difference between the following data types: string, list, tuple and set
print("Ejercicio 2:")

#Ejercicio 3
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print("Ejercicio 3:")

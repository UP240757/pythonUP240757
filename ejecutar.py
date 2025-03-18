
#Ejercicio 5
#What is the difference between remove and discard
print("Ejercicio 5:")
#Ejemplo
it_companies = {'Facebook', 'Google', 'Microsoft'}
it_companies.remove('Google') #Eliminar ggogle (funciona)
#remove : elimina el elemento del conjunto. Este es para cuando estas eguro de que este.
# si el elemento no esta genera error.
print("remove se usa cuando estas seguro de que algo si este y poder eliminarlo")
 #Ejemplo:
it_companies = {'Facebook', 'Google', 'Microsoft'}
it_companies.discard('Google')
it_companies.discard('Tiktok') #Este no xiste en esta lista.
#discard : Este tambien elimina elementos del conjunto.
#Tambien si el elemento no se encuentra no hace nada y no marcara error, 
#lo cual es mas seguro cuando no estas seguro de si existe o no.
print("discard se usa cuando no estas seguro y evitar errores")

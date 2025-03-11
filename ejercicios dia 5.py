#Ejercicio 1
#Declare an empty list
print("Ejercicio 1:")
mi_list = [] #No tiene nada mi lista.
print(len(mi_list))

#Ejercicio 2
#Declare a list with more than 5 items
print("Ejercicio 2:")
lista_de_frutas = ['Fresa', 'Guayaba','Kiwi', 'Mandarina', 'Sandia', 'Manzana','Pera', 'Mango']
print("lista_de_frutas:", lista_de_frutas)


#Ejercicio 3
#Find the length of your list
print("Ejercicio 3:")
print("Ejercicio 2:")
lista_de_frutas = ['Fresa', 'Guayaba','Kiwi', 'Mandarina', 'Sandia', 'Manzana','Pera', 'Mango']
print("lista_de_frutas:", lista_de_frutas)
longitud_lista = len(lista_de_frutas)
print("La longitud de la lista es:", longitud_lista)


#Ejercicio 4
#Get the first item, the middle item and the last item of the list
print("Ejercicio 4:")
lista_de_frutas = ['Fresa', 'Guayaba','Kiwi', 'Mandarina', 'Sandia', 'Manzana','Pera', 'Mango']
primer_item = lista_de_frutas[0]
mitad_item = lista_de_frutas[len(lista_de_frutas) // 2]
ultimo_item = lista_de_frutas[-1]
print("Primer item:", primer_item)
print("mitad item:", mitad_item)
print("ultimo item:", ultimo_item)


#Ejercicio 5
#Declare a list called mixed_data_types, put your
# (name, age, height, marital status, address)
print("Ejercicio 5:")
mixed_data_types_lista=['Sandra', '18', '50 kg', 'soltera', 'Av. Paseos de la Asuncion 5300 int. 89']
print(mixed_data_types_lista)


#Ejercicio 6
#Declare a list variable named it_companies and assign initial values 
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print("Ejercicio 6:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('it_companies_lista:', it_companies_lista)
print('Numero de compañias:',len(it_companies_lista))


#Ejercicio 7
#Print the list using print()
print("Ejercicio 7:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies_lista)



#Ejercicio 8
#Print the number of companies in the list
print("Ejercicio 8:")
print('Numero de compañias:',len(it_companies_lista))


#Ejercicio 9
#Print the first, middle and last company
print("Ejercicio 9:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
primer_item = it_companies_lista[0]
mitad_item = it_companies_lista[len(it_companies_lista) // 2]
ultimo_item = it_companies_lista[-1]
print("Primer item:", primer_item)
print("mitad item:", mitad_item)
print("ultimo item:", ultimo_item)


#Ejercicio 10
#Print the list after modifying one of the companies
print("Ejercicio 10:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista[0] = 'Instagram'
print(it_companies_lista)


#Ejercicio 11
#Add an IT company to it_companies
print("Ejercicio 11:")
it_companies_lista=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista.append('Tiktok')
print(it_companies_lista)


#Ejercicio 12
#Insert an IT company in the middle of the companies list
print("Ejercicio 12:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies_lista) // 2
it_companies_lista.insert(middle_index, 'Netflix')
print(it_companies_lista)


#Ejercicio 13
#Change one of the it_companies names to uppercase (IBM excluded!)
print("Ejercicio 13:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista[0]= it_companies_lista[0].upper()
it_companies_lista[1]= it_companies_lista[1].upper()
it_companies_lista[2]= it_companies_lista[2].upper()
it_companies_lista[3]= it_companies_lista[3].upper()
it_companies_lista[4]= it_companies_lista[4].upper()
it_companies_lista[5]= it_companies_lista[5].upper()
it_companies_lista[6]= it_companies_lista[6].upper()
print(it_companies_lista)


#Ejercicio 14
#Join the it_companies with a string '#;  '
print("Ejercicio 14:")


#Check if a certain company exists in the it_companies list.

#Sort the list using sort() method

#Reverse the list in descending order using reverse() method

#Slice out the first 3 companies from the list

#Slice out the last 3 companies from the list

#Slice out the middle IT company or companies from the list

print("Ejercicios de nivel 1:")
#Ejercicios de Nivel 1:
#Ejercicio 1
#Filter only negative and zero in the list using list comprehension
print("Ejercicio 1:")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("La lista con solo negativos y cero es:", negative_and_zero)







#Ejercicio 2
#Flatten the following list of lists of lists to a one dimensional list :
print("Ejercicio 2:")
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("La dimensional list es:", flattened_list)








#Ejercicio 3
#Using list comprehension create the following list of tuples:
print("Ejercicio 3:")
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("La lista tuple es:", tuples_list)









#Ejercicio 4:
#Flatten the following list to a new list:
print("Ejercicio 4:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for (country, capital) in sublist]
print("La nueva lista es:", flattened_countries)









#Ejercicio 5:
#Change the following list to a list of dictionaries:
print("Ejercicio 5:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

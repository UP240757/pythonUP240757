#Ejercicio 1.
#Concatenate the string 'Thirty', 'Days', 'Of', 
# 'Python' to a single string, 'Thirty Days Of Python'.
palabra = 'Thirty '
palabrados = 'Days '
palabratres = 'of '
palabracuatro = 'Python '
print(palabra,)
print(palabrados,)
print(palabratres,)
print(palabracuatro,)
secuencia = palabra + "" "" + palabrados + "" "" + palabratres + "" "" + palabracuatro
print(secuencia)

#Ejercicio 2
#Concatenate the string 'Coding', 'For' , 'All' 
# to a single string, 'Coding For All'.
print("Ejercicio 2: ")
palabra = 'Coding, For, All'
print(palabra)
palabrauno = 'Coding '
palabrados= 'For '
palabratres = 'All'
secuencia = palabrauno + "" "" + palabrados + "" "" + palabratres
print(secuencia)

#Ejercicio 3
#Declare a variable named company and assign it to an initial value "Coding For All".
print("Ejercicio 3:")
company = 'Coding for all'
print ("este se usara en los siguientes ejercicios")
print (company)

#Ejercicio 4
#Print the variable company using print().
print ("Ejercicio 4:")
print(company)

#Ejercicio 5 
#Print the length of the company string using len() method and print().
print("Ejercicio 5: ")
longitud = len(company)
print ("la longitud de la cadena 'company´ es :" , longitud)

#Ejercicio 6
#Change all the characters to uppercase letters using upper() method.
print("Ejercicio 6:")
company = 'coding for all'
company_upper = company.upper()
print("Los caracteres en uppercase son:", company_upper)

#Ejercicio 7
#Change all the characters to lowercase letters using lower() method.
print ("Ejercicio 7:" )
company = 'CODING FOR ALL'
company_lower = company.lower ()
print ("Los caracteres en lowercase son:", company_lower)

#Ejercicio 8
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("Ejercicio 8: ")
company= 'Coding For All'
company_capitalized = company.capitalize()
company_titled = company.title()
company_swapcased = company.swapcase()
print('original:', company)
print('capitalize:', company_capitalized)
print('title:', company_titled)
print('swapcase:', company_swapcased)

#Ejercicio 9 
#Cut(slice) out the first word of Coding For All string.
print ("Ejercicio 9:")
company = "Coding For All"
palabras = company.split()
newcompany = ' '.join(palabras[1:])
print ( "El resultado de cut (slice) es:", newcompany)

#Ejercicio 10
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print ("Ejercicio 10: ")
print("Este es el primer metodo index:")
string = "Coding For All"
index = string.index("Coding")
if "Coding" in string:
    print(f"La palabra 'Coding' se encuentra e el string.")
else : 
    print("La palabra 'Coding'no se encuentra en el string.")





#Ejercicio 11
#Replace the word coding in the string 'Coding For All' to Python.
print ("Ejercicio 11:")
challenge = 'Coding For All'
print(challenge.replace('Coding' , 'Python')) 

#Ejercicio 12 
#Change Python for Everyone to Python for All using the replace method or other methods.
print ("Ejercicio 12: ")
challenge = 'Python for Everyone'
print(challenge.replace('Everyone' , 'All'))

#Ejercicio 13
#Split the string 'Coding For All' using space as the separator (split()) .
print ("Ejercicio 13: ")
challenge = 'Coding For All'
split_words = challenge.split()
print(split_words)


#Ejercicio 14
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print ("Ejercicio 14: ")
companies = "Facebook, Google, microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")
print(split_companies)

#Ejercicio 15 
#What is the character at index 0 in the string Coding For All.
print ("Ejercico 15: ")
string = "Coding For All"
first_character = string[0]
print (first_character)

#Ejercicio 16
#What is the last index of the string Coding For All.
print("Ejercicio 16: ")
string = "Coding For All"
last_index = len(string) - 1 
print(last_index)

#Ejercicio 17 
#What character is at index 10 in "Coding For All" string.
print ("Ejercicio 17: ")
string = "Coding For All"
character_at_index_10 = string[10]
print(character_at_index_10) #Output: A
sub_string = "For"
index_of_substring = string.index(sub_string)
print(index_of_substring) #Output: 7
try : 
    print(string. index(sub_string, 8))
except ValueError as e : 
    print ("e")

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


  


















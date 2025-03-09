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






#Exercises: Level 1
#Ejercicio 1
#Create an empty tuple
empty_tutle = ()
empty_tutle = tuple()




#Ejercicio 2
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers= ("Junior, Felipe, Daniel,")
sisters = ("Veronica")
print("Los hermanos son:", brothers)
print("Las hermanas son:", sisters)


#Ejercicio 3
#Join brothers and sisters tuples and assign it to siblings
allbrothers = brothers +  sisters
print ("Mis hermanos son:", allbrothers)


#Ejercicio 4
#How many siblings do you have?
hermanos =("Junior, Felipe, Daniel, Veronica,")
print("Yo tengo estos hermanos:")
print(len(["Junior","Felipe","Daniel","Veronica",]))



#Ejercicio 5
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members.
hermanos = "Junior, Felipe, Daniel, Veronica,"
padres =  "Mama Evelia, Papa Hector"
family_members = hermanos +  padres 
print( "Mi familia completa es: ", family_members)

#Exercises: Level 2
#Ejercicio 1
#Unpack siblings and parents from family_members
family_members ='Junior', 'Felipe', 'Daniel', 'Veronica', 'Mama Evelia', 'Papa Hector'
print("Los hermanos son:",family_members[:4])
print("Los padres son:", family_members[4:])


#Ejercicio 2
#Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
frutas =  "Fresa", "Sandia", "Manzana", "Melon","Naranja" 
vegetales = "Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria"  
productos_animal = "Leche", "Huevos","Queso"
food_stuff_tp = frutas + vegetales + productos_animal
print( "la variable food_stuff_tp:", food_stuff_tp)



#Ejercicio 3
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = "Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso"
food_stuff_lt = list(food_stuff_tp)
print( "La food_stuff_lt es:",  food_stuff_lt)



#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = "Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso"


#Slice out the first three items and the last three items from food_staff_lt list


#Delete the food_staff_tp tuple completely


#Check if an item exists in tuple:


#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in  nordic_countries:
    print('Estonia esta en:', nordic_countries('Estonia'))
else: 
    print('No esta')
print("'Estonia' no esta")


#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Iceland' in nordic_countries:
    print('Iceland esta en nordic_countries')
else:
    print ('No esta')





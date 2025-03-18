#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = ("Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso")
food_stuff_lt = list(food_stuff_tp)
longitud = len(food_stuff_tp)
items_middle_tp = food_stuff_tp[(longitud - 1) //2 :  longitud // 2 + 1]
items_middle_lt = food_stuff_lt[(longitud - 1) // 2 : longitud // 2 + 1]
print("Los items del miedo en el tuple son:", items_middle_tp)
print("Los items del medio en el list son:", items_middle_lt)



#Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = ("Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso")
longitud = len(food_stuff_lt)
primeros_tres_items = food_stuff_lt[:3]
ultimos_tres_items = food_stuff_lt[-3:]
print("Los primeros tres items son:", primeros_tres_items)
print("Los ultimos tres elementos son:", ultimos_tres_items)



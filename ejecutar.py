#then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full = front_end + back_end
insert_index = full.index('Redux') + 1
full[insert_index:insert_index] = ['Python', 'SQL']
print(full)

#Ejercicio 28
#The following is a list of 10 students ages:
print("Ejercicio 28:")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.insert()
ages.insert(ages)
print(ages[0], "," ,ages[len(ages)-1])
print(p.countries.index('Mexico'))


unpack = ('China', 'Russia', 'USA')
scandic_countries =('Finland', 'Sweden', 'Norway', 'Denmark')
print("Los primeros 3:", unpack)
print("Los scandic countries son: ", scandic_countries)
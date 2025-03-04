age = 18 
hight = 1.65
numcom = 8j
print (type(age), age)
print (type(hight), hight)
print (type(numcom), numcom)

#Program 4
# Write a script that prompts the user to enter base and height 
# of the trianngle and calculate an area of this triangle
# (area = 0.5 x b x h). 
base = float(input ("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
area = print ("El area del triangulo es: ", base*altura/2)

#Ahora esto
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#  Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = float (input("Ingresar el valor de sideA")) 
sideB = float (input("Ingresar el valor de sideB"))
sideC = float (input('Ingresar el valor de sideC'))
perimeter= print ("El valor del perimetro del triangulo es:", sideA + sideB + sideC )

#Get length and width of a rectangle using prompt.
#  Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
largo = float (input("ingresa el largo del rectangulo"))
ancho = float(input("ingresa el ancho del triangulo"))
Area = print("El area del triangulo es de:", largo * ancho)
perimeter = print("El perimetro del triangulo es de:",2 * (largo + ancho))

#Get radius of a circle using prompt.
#  Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = float (input("ingresa el valor del radio"))
Area = print("El area del circulo es de :", pi * r * r )
circunferencia = print("La circunferencia del circulo es de :", 2 * pi * r)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
pendiente = 2
interceptY = -2
interceptX = interceptY / pendiente
print("la pendiente de la recta es de :", pendiente)
print("La interseccion en el eje Y es:", interceptY)
print(" La interseccion en el eje X es:", interceptX)

#Slope is (m = y2-y1/x2-x1).
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math 
x1, y1  = (2,2) 
x2, y2 = (6,10)
slope = (y2 - y1) / (x2 - x1)
print("La pendiente (m) es:, " "slope")
distancia = (math.sqrt(x2 - x1) ** 2 + (y2-y1) ** 2)
print("la distancia euclinada es:", distancia)


#Compara el slope del ejercico 8 y 9.
#ejercicio 8.
if slope == pendiente:
    print("pendientes iguales")

elif slope > pendiente:
    print("la primer pendiente es mayor")

else:
    print("la segunda pendiente es mayor")




#Calculate the value of y (y = x^2 + 6x + 9).
#Try to use different x values and figure out at what x value y is going to be 0.
# Definir la función
x= int(input("Ingresar el valor de x:" ))
y= ((x**2)+(6*x)+9)
print ("El valor de y es :", " ", y)
if y==0: 
    print ("y es igual a 0.")
else: 
    print ("y no es igual a 0.")


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Finding the length of 'python' and 'dragon'
length_python = len('python')
length_dragon = len('dragon')
print("Length of python:", length_python )
print("Length of dragon:", length_dragon)
#falsa comparacion 
print("length of python is not equal to length of dragon:", length_python!= length_dragon )

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

cadena1 = "pyton"
cadena2 = "dragon"
resultado = ("on" in cadena1 and "on" in cadena2) 
print (resultado) 

#I hope this course is not full of jargon.
#  Use in operator to check if jargon is in the sentence.
sentence = "jargon"
resultado = ("jargon" in sentence)
print(resultado)

#There is no 'on' in both dragon and python.
cadena1 = "dragon"
cadena2= "python"
resultado = ("no 'on' " in cadena1 and " no 'on'" in cadena2 )
print (resultado)

#Find the length of the text python and convert the value to float and convert it to string.
texto = "python"
longitud = len("python")
longitud_float = float (longitud)
longitud_string = str (longitud_float)
print("python: , python ")
print("longitud: , longitud")
print ("longitud(float):", longitud_float)
print("longitud (string):", longitud_string) 

#Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
print("el numero es par")
numero = int(input("definir un numero"))
es_par = numero % 2 == 0 
print (f"el numero {numero} es par: {es_par}")




























# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio

#ingresando datos, nombre completo

print("¿como se llama?")
nombre_completo = input()
print(f"me alego de conocerlo, {nombre_completo}")

#ingresando datos, DNI

print("ingrese su numero de DNI")
DNI = input()
print("sus datos fueron aprobados")
print(f"compruebe si los datos, {nombre_completo}, y {DNI}, son validos")

#ingresando edad

print("ahora ingrerse su edad en numeros")
edad = input()
print(f"la edad ingresada es, {edad}")

#ingresando altura

print("por favor, por ultimo ingrese su altura")
altura = input()
print(f"la altura ingrasada es, {altura}")

#lineas de datos ingresados

print(f"los datos ingresados son, {nombre_completo}, con {DNI}")
print(f"bienvenido a inove, {nombre_completo}, su edad es {edad}, y su altura {altura}")
print("gracias por confiar en nosotros")















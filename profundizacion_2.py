# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero1 = int(input('ingrese un numero entero:\n'))
numero2 = int(input('ingrese el segundo numero entero:\n'))
numero3 = int(input('ingrese el tercer numero entero:\n'))

if (numero1 % 2) == 0:
    print('par')
elif (numero1 % 2) == 1:
    print('impar')
elif (numero2 % 2) == 0:
    print('par')
elif (numero2 % 2) == 1:
    print('impar')
elif (numero3 % 2) == 0:
    print('par')
elif (numero3 % 2) == 1:
    print('impar')
    



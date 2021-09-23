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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero1 = int(input('ingrese el primer numero:\n'))
numero2 = int(input('ingrese el segundo numero:\n'))


if numero1 > numero2:
    print(numero1, 'es mayor a', numero2,)
elif numero2 > numero1:
    print(numero2, 'es mayor a', numero1)
elif numero1 == numero2:
    print(numero1, 'y', numero2, 'son iguales')
    




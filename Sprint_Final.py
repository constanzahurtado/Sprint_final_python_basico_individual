# SPRINT DE ENTREGA: Se solicita como entregable de este Sprint la implementación final de todos los 
# conceptos vistos durante el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:

# ● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu 
# aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
# ● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
# ● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con 
# los siguientes criterios: mayúsculas, minúsculas y números.
# ● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
# ● Por cada cuenta debe pedir un número telefónico para contactarse.
# ● El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un 
# número de contacto asignado.
# ● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
# ● Se debe guardar como un string.

import random
import time

#creamos un diccionario que peritirá almacenar los usuarios y sus datos

diccionario_usuarios = {'Juan':[],
                        'Ana':[],
                        'Esteban':[],
                        'Luis':[],
                        'Francisco':[],
                        'Sara':[],
                        'Roberto':[],
                        'Gabriela':[],
                        'Lucía':[],
                        'Sergio':[]
                        }

# Estas listas están relacionadas con los caracteres especificados para la generación de una contraseña

numeros =['0','1','2','3','4','5','6','7','8','9']
mayusculas= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Para generar una contraseña, se crea la siguiente función: 

def password():
    password_usuario = [] # En esta lista se almacenarán los caracteres de la contraseña. 
    for i in range(8): # Con un ciclo for, establecemos la cantidad de caracteres en la contraseña.
        # Luego, se crean variables que permitan seleccionar caracteres de las listas mencionadas, y con random.choice
        # esta selección es al azar entre todas las listas. 
        password = random.choice(numeros) + random.choice(mayusculas) + random.choice(minusculas) 
        # Con la función append se integran los caracteres en la lista password_usuario.
        password_usuario.append(random.choice(password))
        # El valor retornado son los caracteres sin separación de comas. 
    return "".join(password_usuario)

# Las cuentas de usuario se crean con la siguiente función: 

def creacion_cuenta(diccionario:dict): #Argumento cuya variable es un diccionario.
    for clave in diccionario.keys(): # Este ciclo for permite recorrer las clves de cada usuario (nombre).
        diccionario[clave] = password() # A cada nombre se le asigna una contraseña, invocando la fución password().
    print(diccionario) # Mostramos como queda el diccionario. 


#Los contactos telefónicos se agregan con la siguientes funciones en cadena:

def validacion_contacto(): #Definición de un valor booleano.
    valido=False
    return valido

def ingreso(diccionario:dict): #Se crea un ciclo while con valores booleanos, para asegurar el ingreso correcto de los contactos
    while True: 
        contacto = input("Ingrese su número de contacto: ")
        valido = validacion_contacto() # Mientras se falso, se cumple con las siguientes funciones:
        if len(contacto) < 8  or len(contacto) > 8: # El contacto no debe tener menos o más de 8 caracteres.  
                print("El número de contacto debe tener al 8 dígitos") # Se imprime el error, y se repite el ciclo.
        else: # Si se ingresa correctamente el contacto, su valor es verdadero y se agrega el contacto a cada usuario.
            valido != validacion_contacto()
            for clave in diccionario.keys(): #Ciclo for que permite recorrer el diccionario
                diccionario[clave] = [password(),contacto] # Se agrega el contacto.
            break # Se termina el ciclo para el usuario.

def ingreso2(diccionario:dict):
    i = 1
    while i <= len(diccionario): # Con este ciclo while, la anterior función se limita al número de usuarios. 
        ingreso(diccionario) # Se llama a la función anterior. 
        i += 1 #Contador ciclo.
    return diccionario

   
# Con la siguiente fución, mostramos los datos de cada usuario.               
def mostrar_usuarios(diccionario:dict): #Argumento cuya variable es un diccionario.
    for clave, valor in diccionario.items(): # Recorremos todo los ítems del diccionario. 
        time.sleep(3) # Como los usuarios se muestran rápidamente, se agrga un delay de 3 segundos. 
        print(f"Usuario: {clave} ")
        print(f"Contraseña: {valor[0]}")
        print(f"Contacto: {valor[1]} ")
        print("----------------------------------------------------------------------")

# FInalmente, llamamos a las funciones que son parte del programa final. 

print("----------------------------------------------------------------------")
print("Asignación de Contraseñas")
print("----------------------------------------------------------------------")
creacion_cuenta(diccionario_usuarios)   
print("----------------------------------------------------------------------")
print("Ingreso Contacto Telefónico Usuarios")
ingreso2(diccionario_usuarios)
print("----------------------------------------------------------------------")
print("Información de Usuarios Registrados")
mostrar_usuarios(diccionario_usuarios)
 
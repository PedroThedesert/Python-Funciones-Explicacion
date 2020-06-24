# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:59:46 2020

@author: Pedro Gutiérrez
"""


# F U N C I O N  A R G U M E N T O S  P O R  N O M B R E - P O R  D E F E C T O 
#    U  S  A  R    E  S  T  A 



def resta (a=30,b=10): # valores que se reciben
# Función Argumentos por nombre / Argumentos por defecto
# Sin embargo es posible evadir el orden de los parámetros si indicamos 
#durante la llamada que valor tiene cada parámetro a partir de su nombre

# print (funcionesCurso.resta(a=3,b=5)) # out: -2"
# print (funcionesCurso.resta()) # out: 20
# print (funcionesCurso.resta(5,3)) # out: 2

    return a-b


# F U N C I O N    C O N T R O L   E R R O R E S -  P A R A M E T R O S  P O R   D E F E C T O 
#    U  S  A  R    E  S  T  A 

def Control_de_Errores_resta(a=None, b=None):
# Funciones: Parámetros por defecto (CONTROL DE ERRORES) **** IMPORTANTE ****  BUENAS PRÁCTICAS	"# Funciones: Parámetros por defecto (CONTROL DE ERRORES) **** IMPORTANTE ****  BUENAS PRÁCTICAS
# Podemos asgignar unos valores por defecto nulos a los parámetros, de esa forma podríamos hacer una comprobación antes de ejecutar el código de la función

#funcionesCurso.Control_de_Errores_resta() # out: Error, debes enviar dos números a la función
#print(funcionesCurso.Control_de_Errores_resta(a=5,b=2)) # out: 3

    if a==None or b == None: 
        print("Error, debes enviar dos números a la función")
        return # indicamos el final de la función aunque no devuelva nada
    return a-b


# I N D E N T A C I O N   D E  F U N C I O N E S
#    U  S  A  R    E  S  T  A 

def long_function_name(
    var_one=None, var_two=None, var_three=None,
    var_four=None):

    # Further indentation required as indentation is not distinguishable.
    #print (funcionesCurso.long_function_name(var_one=1, var_two=2, var_three=3, var_four=4))
    
    print(var_one, var_two, var_three, var_four)





# F U N C I O N E S   Q U E   N O   D E V U E L V E N
def escribe(texto):
    # texto ="Nine Inch Nails es una gran banda"
    # funcionesCurso.escribe(texto)
    print (texto)


# F U N C I O N E S   P A S O   P O R    V A L O R - VALOR SOLO CAMBIA EN LA FUNCIÓN

def doblar_valor (numero):
#Funciones: Ejemplo de paso por valor ' TIPOS SIMPLES - VALOR SOLO CAMBIA EN LA FUNCIÓN'	"# Ejemplo de paso por valor ' TIPOS SIMPLES - VALOR SOLO CAMBIA EN LA FUNCIÓN'
# Crea una copia dentro de la función, por eso no les afecta externamente lo que hagamos con ellos

# n = 10
# funcionesCurso.doblar_valor(n)
# print (n)    
    
        numero *=2
        print (numero)
        
# F U N C I O N E S   P A S O   P O R    R E F E R E N C I A - VALOR CAMBIA AFUERA

def doblar_valores(numeros):
#Funciones: Ejemplo de paso por referencia - TIPOS COMPUESTOS - VALOR CAMBIA AFUERA	"# Ejemplo de paso por referencia - TIPOS COMPUESTOS - VALOR CAMBIA AFUERA
# Sin embargo las listas u otras colecciones, al ser tipos compuestos se pasan por referencia y si las modificamos dentro de la función estaremos modificándolas también fuera

# ns=[10,50,100]
# funcionesCurso.doblar_valores(ns) # out:20,100,200
# print (ns)

# # Podemos evitar la modificación realizando una copia

# ns =[10,50,100]
# funcionesCurso.doblar_valores(ns[:]) # una copia al vuelo de una lista con [:]
# print(ns) # out: [10, 50, 100]


        for i, n in enumerate (numeros):
            numeros[i] *=2


# F U N C I O N E S  G L O B A L - para cambiar el valor de una variable externa dentro de una función y que cuando salga tenga el valor inicial


def test_var_global_externa():
# Funciones variable global: para cambiar el valor de una variable externa 
# dentro de una función y conservarlo al valor original cuando sales de la función	

# o = 10
# print(o)
# funcionesCurso.test_var_global_externa()
# print(o)


    global o # variable que hace referencia  a la o externa
    o = 5
    print (o)            
            
            
#F U N C I O N  R E T O R N O  Y  A S I G N A C I O N  D E  R E T O R N O  A  U N A  V A R I A B L E

def test_retorno_asignacion_a_variables():
# Función: Retorno y asignación de retorno a una variable

# print (funcionesCurso.test_retorno_asignacion_a_variables()) # out: [1, 2, 3, 4, 5]
# print (funcionesCurso.test_retorno_asignacion_a_variables()[-1]) # out: 5
# print (funcionesCurso.test_retorno_asignacion_a_variables()[1:4]) # out: [2, 3, 4]

# lista = funcionesCurso.test_retorno_asignacion_a_variables() # out: [1, 2, 3, 4, 5]
# print (lista[-1])  # out: 5"
    
        return [1,2,3,4,5]            
    


# F U N C I O N E S   Q U E    D E V U E L V E N   V A L O R E S
def introduce_numero_usuario():
    #numeroUsuario = funcionesCurso.introduce_numero_usuario ()
    numeroUsuario = int(input("introduce un numero entre 1 y 9\n"))
    print ("el numero de usuario introducido es ", numeroUsuario)
    return numeroUsuario

def conversion_a_integer():
    #numeroUsuario = funcionesCurso.conversion_a_integer ()
    numeroUsuario = int(input("introduce un numero entre 1 y 9\n"))
    print ("el numero de usuario introducido es ", numeroUsuario)
    return numeroUsuario

def asignar_a_nulo():
    #asignar unos valores por defecto nulos	"#asignar unos valores por defecto nulos
    #numeroUsuario = funcionesCurso.asignar_a_nulo ()
    numeroUsuario =None
    print (numeroUsuario)
    return numeroUsuario

# F U N C I O N E S  C O N  P A R A M E T R O S
def nombre_funcion( b, c ):
    #resultado = funcionesCurso.nombre_funcion( 5, 5 )
    #print (resultado)
    a = b + c
    return a


# F U N C I O N E S  C O N  P A R A M E T R O S   O P C I O N A L E S 

def func_param_opcionales(param_enviado, param_opcional = 2):
    # print(funcionesCurso.func_param_opcionales(3))
    return param_enviado*param_opcional

# La función func tiene un argumento opcional, en este caso b con valor 2, así
# que es posible realizar un llamado sin necesidad de pasar un valor para esta
# variable.


# F U N C I O N E S  R E T O R N O   V A R I A B L E S  A  L A  V E Z


def retorno_variable_a_la_vez():
#Funciones Retorno de varias variables a la vez MUY POTENTE, 
#no es común en otros lenguajes de programación	

# funcionesCurso.retorno_variable_a_la_vez()

# cadena, numero, lista = funcionesCurso.retorno_variable_a_la_vez()
# print (cadena) # out: Una cadena
# print (numero) # out: 20 
# print (lista) # out: [1,2,3]


# lista.append(12)

# print(lista) # out: [1,2,3,12]


    return "Una cadena", 20, [1,2,3]




# F U N C I O N E S   A R G U M E N T O S   I N D E T E R M I N A D O S

# P O R   P O S I C I O N - T U P L A S


def indeterminados_posicion(*args):
# Funciones: ARGUMENTOS INDETERMINADOS  (envío de parámetros sin determinar)	
# POR POSICION
# "Cuando en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. En estos casos podemos utilizar los parametros indeterminados por posición y por nombre
# Para recibir un número indeterminado de parámetros por posición, debemos crear una lista dinámica de argumentos (una tupla en realidad) definiendo el parámetro con un asterisco. 
    
# *args: no se especifican los argumentos ni se les ordena"
# ***** Sintaxis de lo recibido en función: *args
# ***** lo que se le envía: 5, ""Hola"", [1,2,3,4,5]


#funcionesCurso.indeterminados_posicion(5, "Hola", [1,2,3,4,5])
    
     for arg in args:
      print (arg)


# P O R   N U M E R O S

def calcula_media(*args):
#Funciones: ARGUMENTOS INDETERMINADOS  EJEMPLO 1	"
#---------- proceso principal  
# a,b,c = 3,5,7

# media = funcionesCurso.calcula_media (a,b,c)
# print ("media:", media)

# media = funcionesCurso.calcula_media(6,7,8,9,12,33,44)
# print ("media:", media)

    
    total = 0
    for i in args:
        total +=i
    resultado = total / len(args)
    return resultado


# P O R   O R D E N

def junta_items(nombre_archivo, separador, *args) :
    #------------------------- proceso principal
    #
    #funcionesCurso.guardar_en_archivo_junta_items("pepe.txt", ";", "a", "b", "c", "d")
    
    #Funciones: ARGUMENTOS INDETERMINADOS  EJEMPLO 2: Guardar en archivo, juntar, escribir en archivo	"Escribir en un archivo, juntar cosas
    
    archivo = open(nombre_archivo, "a")
    archivo.write(separador.join(args)+ "\n")


# F U N C I O N E S   R E C U R S I V I D A D 

def funciones_recursividad_fibbonaci(n):
#"Funciones recursividad múltiple, el retorno te hace una ejecución doble
# Fibonacci version recursiva

#print("El fibonacci es ", funcionesCurso.funciones_recursividad_fibbonaci(10))

     if n <=1:
      return n
     else: 
      return funciones_recursividad_fibbonaci(n-1)+funciones_recursividad_fibbonaci(n-2)
    















    
    










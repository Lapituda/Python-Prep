# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

a = 12
print(a)

# 2) Imprimir el tipo de dato de la constante 8.5
let = 8.5
print(type(let))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(a))

# 4) Crear una variable que contenga tu nombre
b = "Angel"
#
# 5) Crear una variable que contenga un número complejo
c = 2 + 3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(c)

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
bool = "True"
bol = True
# No es lo mismo ya que una contiene una string y otra contiene un booleano que verdadero.

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(bool), type(bol))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

d = 12 + 12.5

# 11) Realizar una operación de suma de números complejos
print(c + d)

# 12) Realizar una operación de suma de un número real y otro complejo

e = 12 + 2j

# 13) Realizar una operación de multiplicación
print(e * d)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
resulado = 2**8
print(resulado)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

f = 27 // 4
print(f)

# 16) De la divisió#n anterior solamente mostrar la parte entera

g = 27 % 4
print(g)

# 17) De la división de 27 entre 4 mostrar solamente el resto

h = 27 % 4
print(h)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

i = 4 * 6 + 3

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

j = "Hola" + "Mundo"

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)
# No son iguales ya que uno es un string y el otro es un entero.

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == int(2))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# por que el float va con . y no con ,

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

k = 3
k -= 1
print(k)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print(1 << 2)
# El sistema binario es un sistema de numeración en el que los números se representan utilizando solamente las cifras cero y uno, es decir, utilizando únicamente dos estados.


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# por que no puede sumar un string con un entero

# 26) Realizar una operación válida entre valores de tipo entero y string

print(2 + int("2"))

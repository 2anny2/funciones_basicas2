#1 Cuenta regresiva crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def countdown (num):
    list = []
    for resta in range(num,-1,-1):
        list.append(resta)
    return list

NewList = countdown(5)
print(NewList)

#2 Imprimir y devolver:crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
def imprimir_ydevolver(list):
    print(list[0])
    return list[1]

devolver = imprimir_ydevolver([5,15,45])
print(devolver)

#3 Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
def longitud(list1):
    sum = list1[0] + len(list1)
    return sum
print(longitud([1,2,3,4,5]))

#4 Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def lenght_and_value(num1, num2):
    list = []
    for x in range(0, num1):
        list.append(num2)
    return list

List2 = lenght_and_value(8,7)
print(List2)


#5 Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def mayores(num):
    lista = []
    contador = 0
    if len(num) > 1:
        for x in num:
            if x > num[1]:
                lista.append(x)
                contador = contador + 1
    else:
        return False
    
    print(contador)
    return lista

result = mayores([5,2,3,2,1,4])
print(result)
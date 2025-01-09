"""numero =[1,2,3,4,5,6,7,8,9]
numero1=[10,11,12,13,14]
numero1.append(15)
print (numero1)"""

## ejemplo de funcion encontrar los pares
"""def pares(nuemros):
    numeros_pares = []
    for n in numero:
        if n % 2 == 0:
            numeros_pares.append(n)
    return numeros_pares
                             
resultado = pares(numero)
#print (resultado)"""



## tabla de multiplicar        
def tabla_Multiplicar (numero):
    resultado = []
    multiplicar = [1,2,3,4,5,6,7,8,9,10]
    for n in multiplicar:
        var = numero * n
        #resultado.append(str(numero)+'x'+str(n)+'='+str(var))
        resultado.append(f"{numero} x {n} = {var}")   
               
    return (resultado)

resultados1 = tabla_Multiplicar(3) 
print (resultados1)


##Importar Fecha
"""import datetime
fecha = datetime.datetime.now()
print (type(fecha))
print (fecha.strftime('%d/%m/%Y'))"""


### invertir cadena
##1era forma
texto = 'Python'
"""for i in range(len(texto)-1,-1,-1):
    print(texto[i])"""
##2da forma
"""print(texto[: :-1])"""
   

### obterner el primer y ultimo elemento de una lista
"""lenguajes = ['Python','Cr','Php','Jave','JavaScripts']
primer_elem = lenguajes[0]
print(primer_elem )
ultimo_elem = lenguajes[len(lenguajes)-1]
print(ultimo_elem)
ultimo1_elem = lenguajes[-1]
print(ultimo1_elem)"""

### tupla
"""fecha_event = (2024,12,10)
print(type(fecha_event))
print('El evento esta programado para la fecha:', fecha_event)
print('El evento esta programado para la fecha:%i/%i/%i', fecha_event)
ano , mes , dia = fecha_event
print('El evento esta programado para la fecha: {}/{}/{}'.format(ano,mes,dia))"""

#valor absoluto y valo entero la documentaciom
"""print(abs.__doc__)
print(int.__doc__)"""

#imprimir un cadena de multiples lineas
#forma 1
#cadena = "Es un lenguaje de programación increíblemente versátil y fácil de aprender,"
#cadena +="ideal tanto para principiantes como para expertos."
#cadena +="Puedes usar Python para una variedad de tareas"
#print(cadena)
#forma 2
#cadena = """Es un lenguaje de programación increíblemente versátil y fácil de aprender, 
#ideal tanto para principiantes como para expertos.
#Puedes usar Python para una variedad de tareas"""
#print(cadena)"""

# diferencia entre fecha
"""from datetime import date
hoy = date(2024, 12, 10)
otra_fecha = date(2024, 11, 20)

delta = hoy - otra_fecha  
print(delta.days)"""

# ejemplo de suma, se hacen if no hay necesidad de colocar la algo despues de la condicion por defecto si es verdad lo coloca 
#en true de lo contrario lo coloca en False
"""def numero_operacion(a, b, c):
    suma = a + b + c
    if a==b and a==c:
        suma *= 3
    return suma
     
print(numero_operacion(2,2,7))
print(numero_operacion(2,2,2))"""


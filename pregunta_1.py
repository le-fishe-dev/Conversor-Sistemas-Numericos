"""
Conversor Binario a Decimal
"""
# funcion que lee cada 1 en un numero binario y lo asocia a un valor, que luego va sumando.
def binario_a_decimal(numero_binario:str) -> int:
    # declarar variable entero, numero decimal
    numero_decimal = 0
    # leer cada 1, de derecha a izquierda.
    for i in range(len(numero_binario)):
        #print(numero_binario[-(i+1)])
        if numero_binario[-(i+1)] == "1":
            numero_decimal += 2**i
    return numero_decimal

"""
Conversor Decimal a Binario
"""

# funcion que devuelve el maximo divisor de 2**x, para cualquier entero.
def max_divisor2(decimal:int) -> int:
    divisor = 1
    while decimal >= divisor:
        divisor *= 2
    return divisor//2

# funcion que devuelve el exponente de una potencia de base 2.
def exp2(potencia:int) -> int:   # la potencia debe ser de base 2, entera y positiva.
    exp = 0
    while potencia > 2**exp:
        exp += 1
    return exp

# funcion que recibe exponente de una potencia de base 2, y devuelve un string con (exponente + 1) ceros.
def longitudBin(exponente:int) -> str:
    binario = ""
    for i in range(exponente + 1):
        binario += "0"
    return binario

# funcion que reemplaza el valor de un digito especifico, en una cadena binaria, de un cero a un uno.
def reemplazaBin(exponente:int,cadena_binaria:str) -> str:
    # Caso 1: Reemplazar el primer cero por un uno. Ej: "0000" --> "1000"
    if exponente == len(cadena_binaria) - 1:
        return "1" + cadena_binaria[1:]
    # Caso 2: Reemplazar el último cero por un uno. Ej: "0000" --> "0001"
    elif exponente == 0:
        return cadena_binaria[:len(cadena_binaria) - 1] + "1"
    # Caso 3: Reemplazar un cero intermedio por un uno. Ej: "0000" --> "0010"
    else:
        return cadena_binaria[:-exponente-1] + "1" + cadena_binaria[-exponente:]

def decimal_a_binario(numero_decimal:int) -> str:
    # obtener la longitud maxima del numero entero del sistema binario
    numero_binario = longitudBin((exp2(max_divisor2(numero_decimal))))

    # bucle, repetir hasta que numero decimal sea menor que 0
    while numero_decimal > 0:
        # obtener potencia de 2, menor o igual al numero decimal, más cercano.
        potencia_2 = max_divisor2(numero_decimal)
        # obtener exponente de la potencia de 2
        exp_2 = exp2(potencia_2)
        # agregar un '1' a la posicion correcta
        numero_binario = reemplazaBin(exp_2,numero_binario)
        # restar el numero por la potencia de 2 menor o igual mas cercana
        numero_decimal = numero_decimal - potencia_2

    return numero_binario

def suma_binario(numero_binario:str,sumando:int):
    # convertir binario a decimal
    numero_decimal = binario_a_decimal(numero_binario)
    # sumarle el sumando al numero decimal
    numero_decimal += sumando
    # devolver decimal a binario
    return decimal_a_binario(numero_decimal)

def complemento_a_uno(numero_binario: str) -> str:
    contador = 0
    # lee cada digito
    for d in numero_binario:
        #print(f"d vale {d}")
        # Caso 1: si el digito es 1, cambiarlo a 0
        if d == "1":
            # si es el primer caracter, entonces cambiarlo asi
            if contador == 0:
                numero_binario = "0" + numero_binario[1:]
            # si es el ultimo caracter, entonces cambiarlo asi
            elif contador == len(numero_binario):
                numero_binario = numero_binario[:contador - 1] + "0"
            # si es un caracter intermedio, entonces cambiarlo asi
            else:
                numero_binario = numero_binario[:contador] + "0" + numero_binario[contador+1:]
        
        # Caso 2: si el digito es 0, cambiarlo a 1
        if d == "0":
            # si es el primer caracter, entonces cambiarlo asi
            if contador == 0:
                numero_binario = "1" + numero_binario[1:]
            # si es el ultimo caracter, entonces cambiarlo asi
            elif contador == len(numero_binario):
                numero_binario = numero_binario[:contador - 1] + "1"
            # si es un caracter intermedio, entonces cambiarlo asi
            else:
                numero_binario = numero_binario[:contador] + "1" + numero_binario[contador+1:]
        #print(f"numero binario vale ahora {numero_binario}")

        # aumentar contador en 1
        contador += 1
    return numero_binario

def complemento_a_dos(numero_binario: str) -> str:
    # invertir todos los digitos
    numero_binario = complemento_a_uno(numero_binario)
    # sumarle 1 al numero binario
    numero_binario = suma_binario(numero_binario,1)
    # devolver resultado
    return numero_binario

"""
Seccion de Llamada
"""

print(decimal_a_binario(10))

print(binario_a_decimal("00010"))

print(complemento_a_dos("0010"))
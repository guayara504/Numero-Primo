def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("El número {} Es primo".format(numero),"!"*10)
    return True
 
numero = int(input("Ingrese un numero: "))
es_primo(numero)

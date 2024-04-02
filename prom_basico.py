# def es_primo(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def imprimir_primos(numero):
#     primos = [num for num in range(2, 101*numero) if es_primo(num)]
#     print(f"Los números primos entre 0 y {100*numero} son:")
#     print(primos)

# def imprimir_impares(inicio, fin):
#     impares = [num for num in range(inicio, fin + 1) if num % 2 != 0]
#     print(f"Los números impares entre {inicio} y {fin} son:")
#     print(impares)

# def main():
#     num = int(input("Ingrese un número: "))
    
#     if num < 0:
#         print("Por favor ingrese un número positivo.")
#         return
    
#     imprimir_primos(num)
#     imprimir_impares(num, 2*num)

# if __name__ == "__main__":
#     main()

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_primos(numero):
    primos = [num for num in range(2, 100*numero) if es_primo(num)]
    print("Los números primos son:", primos)

def imprimir_impares(inicio, fin):
    impares = [num for num in range(inicio, fin + 1) if num % 2 != 0]
    print("Los números impares son:", impares)

def main():
    num = int(input("Ingrese un número: "))
    imprimir_primos(num)
    imprimir_impares(num, 2*num)

if __name__ == "__main__":
    main()

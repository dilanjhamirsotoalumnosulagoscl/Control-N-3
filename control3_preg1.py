def digitos(num):
    return len(str(num))

num = int(input("Ingrese un número: "))

print("El número tiene", digitos(num), "dígitos.")
def es_binario(var):
    for caracter in var:
        if caracter!= "0" and caracter!= "1":
            return False
    return True

print(es_binario("101010"))
print(es_binario("10102"))
print(es_binario("11001100"))
print(es_binario("abcdefg"))
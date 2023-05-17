numero = int(input('Digite um numero natural: '))
i = 1

while numero > 0:
    i *= numero
    numero = numero - 1
print(i)
    
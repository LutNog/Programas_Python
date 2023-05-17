numero = int(input('Digite um numero: '))
soma = numero * 4
i = 0

while soma > i:
    if not soma % 2 == 0:
        print(i)
    soma = soma - 1
    i = i + 1 
    

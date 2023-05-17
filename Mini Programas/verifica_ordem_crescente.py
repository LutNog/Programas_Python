numero1 = int(input("Digite o numero: "))
numero2 = int(input("Digite o numero: "))
numero3 = int(input("Digite o numero: "))

if (numero1 < numero2) and (numero2 < numero3) and (numero1 < numero3) :
    print("crescente")
else:
    print("não está em ordem crescente")
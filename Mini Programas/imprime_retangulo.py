largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))


while largura > 0:
    while altura > 0:
        altura = altura - 1
        print("#" * (largura))
    largura = largura - 1
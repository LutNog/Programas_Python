def remove_repetidos(lista):
    lista.sort()
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
    return lista1
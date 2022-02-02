lista = [8, 5, 10, 5, 2, 4, 4, 3]

def manipulandoLista(lista):

    listaCurta = []

    for x in lista:
        if x not in listaCurta:
            listaCurta.append(x)

    i = 0
    while i < len(listaCurta):
        j = 0
        while j < len(listaCurta):
            if (listaCurta[i] < listaCurta[j]):
                temp = listaCurta[i]
                listaCurta[i] = listaCurta[j]
                listaCurta[j] = temp
            j += 1
        i += 1

    return listaCurta
if __name__ == '__main__':
    print(f'Comprimento total da lista: {len(lista)}, elementos')
    print(manipulandoLista(lista))


def tira_tipo(path):
    m = list()
    o = 0

    for c in path[::-1]:
        if c == '.':
            break
        o -= 1
        m.append(c)
    return ''.join(m[::-1])


def tirando_iguais(lista):
    lista_A = lista
    lista_B = [lista_A[0]]

    n = 0
    for i in lista_A:
        o = 0
        for j in lista_B:
            if i == j:
                o += 1
        if o == 0:
            lista_B.append(i)
    return lista_B

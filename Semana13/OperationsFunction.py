def soma(lista):
    resultado = 0

    for i in range(len(lista)):
        resultado += lista[i]
    
    return resultado

def media(lista):
    media = 0

    for i in range(len(lista)):
        media += lista[i]

    return media/len(lista)

def distintos(lista):
    condicao = 0

    for i in range(len(lista)):
        valor = lista[i]
        for j in range(len(lista)):
            if(valor == lista[j] and i != j ):
                condicao += 1
    
    if(condicao > 0):
        return False
    else:
        return True
    
def maior(lista):
    maior = lista[0]

    for i in range(len(lista)):
        if(lista[i] > maior):
            maior = lista[i]
    
    return maior

def menor(lista):
    menor = lista[0]

    for i in range(len(lista)):
        if(lista[i] < menor):
            menor = lista[i]
    
    return menor
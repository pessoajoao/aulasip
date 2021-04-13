N = int(input())

numeros = input().split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

menorValor = numeros[0]
posicao = 0

for i in range(len(numeros)):
    if(numeros[i] < menorValor):
        menorValor = numeros[i]
        posicao = i

print("Menor valor: %d"%(menorValor))
print("Posicao: %d"%(posicao))
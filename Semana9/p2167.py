N = int(input())

rpm = input().split()

for i in range(len(rpm)):
    rpm[i] = int(rpm[i])

velocidade = 0
queda = 0

for i in range(len(rpm)):
    if(rpm[i] >= velocidade):
        velocidade = rpm[i]
    else:
        queda = i+1
        break
   
print(queda)
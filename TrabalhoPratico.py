num = [0, 0, 0, 0]
i = 1
qtd = int(input("Digite a quantidade de mouses: "))
while(i != 0):
    i = int(input("Digite a situação: "))
    if(i == 1):
        num[0] = num[0]+int(input("Digite a quantidade: "))
    elif (i == 2):
        num[1] = num[1]+int(input("Digite a quantidade: "))
    elif (i == 3):
        num[2] = num[2]+int(input("Digite a quantidade: "))
    elif (i == 4):
        num[3] = num[3]+int(input("Digite a quantidade: "))
    elif (i != 0):
        print("Digite um número entre 1 e 4\n")

print("Quantidade de mouses: ", qtd, '\n')
print("Situação                               Quantidade           Porcentagem")
print("Necessita de esfera:                      ",num[0],"                ",(num[0]*100)/qtd, '%')
print("Necessita de limpeza:                     ",num[1],"                ",(num[1]*100)/qtd, '%')
print("Necessita de troca do cabo conector:      ",num[2],"                ",(num[2]*100)/qtd, '%')
print("Quebrado ou inutilizado:                  ",num[3],"                ",(num[3]*100)/qtd, '%')
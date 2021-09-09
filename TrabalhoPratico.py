num = [0, 0, 0, 0]
i = 1
busca = 1
while(i != 0):
    i = int(input("Digite a situação: (digite o número zero para sair do fluxo) "))
    if(i == 1):
        num[0] = num[0]+int(input("Digite a quantidade de mouses: "))
    elif (i == 2):
        num[1] = num[1]+int(input("Digite a quantidade de mouses: "))
    elif (i == 3):
        num[2] = num[2]+int(input("Digite a quantidade de mouses: "))
    elif (i == 4):
        num[3] = num[3]+int(input("Digite a quantidade de mouses: "))
    elif (i != 0):
        print("Digite um número entre 1 e 4\n")

while (busca != 0):
    busca = int(input("Qual situação você deseja buscar? (digite o número zero para sair do programa e mostrar o relatório) \n"))
    if (busca == 1):
        print(num[busca-1], 'mouses com defeito na esfera.\n')
    elif (busca == 2):
        print(num[busca - 1], 'mouses com necessita de limpeza.\n')
    elif (busca == 3):
        print(num[busca - 1], 'mouses com necessita de troca do cabo conector.\n')
    elif (busca == 4):
        print(num[busca - 1], 'mouses quebrados ou inutilizados.\n')
    else:
        print("Digite um valor válido para a pesquisa.\n")

qtd = sum(num)
print("Quantidade de mouses: ", qtd)
print("Situação                               Quantidade           Porcentagem")
print("1-Necessita de esfera:                    ",num[0],"                ",(num[0]*100)/qtd, '%')
print("2-Necessita de limpeza:                   ",num[1],"                ",(num[1]*100)/qtd, '%')
print("3-Necessita de troca do cabo conector:    ",num[2],"                ",(num[2]*100)/qtd, '%')
print("4-Quebrado ou inutilizado:                ",num[3],"                ",(num[3]*100)/qtd, '%')
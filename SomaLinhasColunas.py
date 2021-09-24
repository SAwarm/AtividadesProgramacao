def adicionarValoresMatriz(lis):
    linhas = int(input("Linhas: "))
    colunas = int(input("Colunas: "))

    for i in range(linhas):
        linha = []
        lis.append(linha)
        for x in range(colunas):
            lis[i].append(int(input("Digite um número: ")))

def lerValoresMatriz(lis):
    for i in range(len(lis)):
        print(lis[i])

def somarValores(lis):
    for i in range(len(lis)):
        for x in range(len(lis[i])):
            if x == len(lis[i])-1:
                lis[i].append(sum(lis[i]))

def novaLinha(lis):
    soma = 0;
    for i in range(len(lis)+1):
        if i == len(lis):
            linha = []
            lis.append(linha)
    for x in range(len(lis)):
        if x == len(lis)-1:
            for y in range(len(lis)-1):
                for z in range(len(lis)-1):
                    soma += lis[z][y]
                lis[x].append(soma)
                soma = 0

lis = []
adicionarValoresMatriz(lis)
lerValoresMatriz(lis)
somarValores(lis)
lerValoresMatriz(lis)
novaLinha(lis)
lerValoresMatriz(lis)
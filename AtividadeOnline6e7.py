def leituraLista(lis):
    indice = 0
    lis.append(int(input("Digite um número: ")))
    while int(lis[indice]) > -1 :
        lis.append(int(input("Digite um número: ")))
        indice += 1
    lis.pop()
    for i in range(len(lis)):
        print(i,':', lis[i])

def moverIndiceLista(lis):
    origemIndex = int(input("Digite a origem: "))
    destinoIndex = int(input("Digite o destino: "))
    origem = lis[origemIndex]
    lis.remove(lis[origemIndex])
    lis.insert(destinoIndex, origem)
    for i in range(len(lis)):
        print(i,':',  lis[i])
lis = []
leituraLista(lis)
moverIndiceLista(lis)

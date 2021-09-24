salario = []
numeroFilhos = []

def lerColetaDados(salario, numeroFilhos):
    salario.append(int(input("Qual o seu salário? ")))
    numeroFilhos.append(int(input("Quantos filhos você tem? ")))
    indice = 0
    while salario[indice] != -1 and numeroFilhos[indice] != -1:
        salario.append(int(input("Qual o seu salário? ")))
        numeroFilhos.append(int(input("Quantos filhos você tem? ")))
        indice += 1
    if salario[indice] == -1:
        salario.pop()
    if numeroFilhos[indice] == -1:
        numeroFilhos.pop()
    return True

def calcularMedia(lista):
    media = sum(lista)/len(lista)
    print("Média: ", media)

def maiorValor(lista):
    print("Maior valor", max(lista))

def percentualPessoasSalarioEspecifico(lista, n):
    contadorPessoas = 0
    for i in range(len(lista)):
        if(lista[i] <= n):
            contadorPessoas += 1
    percentual = (contadorPessoas*100)/len(lista)
    print("Percentual de pessoas com o salario menor que", n,':', percentual,"%")

def relatorio(lista, nome):
    for i in range(len(lista)):
        print(nome,":",lista[i])

lerColetaDados(salario, numeroFilhos)
calcularMedia(salario)
calcularMedia(numeroFilhos)
maiorValor(salario)
percentualPessoasSalarioEspecifico(salario, 350)
relatorio(salario, "Salário")
relatorio(numeroFilhos, "Número de filhos")





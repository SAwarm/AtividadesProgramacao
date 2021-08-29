print("Para sair do programa, digite uma nota fora do intervalo de 0.0 à 10.0")
notas = []
nota = 0
x = 0
while(x == 0):
    nota = float(input("Digite a nota do aluno: "))
    if(nota <= 10 and nota >= 0):
        notas.append(nota)
    else:
        x = 1
print(min(notas))
print(max(notas))
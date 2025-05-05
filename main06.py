notas = [""] *5
soma=0
qntnotas = 0

for i in range (len(notas)):
    notas[i] = float(input(f"Digite a nota do aluno {i+1}: "))

for x in range (len(notas)):
    soma += notas [x]

media = soma / (len(notas))

for j in range (len(notas)):
    if notas [j] > media:
        qntnotas +=1


print(f"A média da turma é {media} e{qntnotas} aluno(s) estão com a nota acima da média")
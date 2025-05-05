nomes=["joão","Carlos", "Maria", "luiza", "isabel"]
NomeCerto = input("Digite o nome de um aluno")

for i in range(len(NomeCerto)):
    if nomes[i] == NomeCerto:
        print(f"o nome é{NomeCerto}, e está na lista de posição {i}")
    else:
        print("nome não encontrado")
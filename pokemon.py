#adding a new pokemon to the list
def adicionar_pokemon():
    nome = input("Nome do Pokémon: ")
    tipo = input("Tipo: ")

    ataque1 = input("Nome da Ataque normal: ")
    dano1 = int(input("Dano normal: "))

    ataque2 = input("Nome da Ataque especial: ")
    dano2 = int(input("Dano especial: "))
    precisao = int(input("Precisão especial (0-100): "))

    hp = int(input("HP: "))

    with open("pokemons.txt", "a") as ficheiro:
        ficheiro.write(f"{nome};{tipo};{ataque1};{dano1};{ataque2};{dano2};{precisao};{hp}\n")

    print("Pokémon adicionado com sucesso!")
#listing all pokemons in the list
def listar_pokemons():
    pokemons = []

    with open("pokemons.txt", "r") as ficheiro:
        for linha in ficheiro:
            dados = linha.strip().split(";")
            pokemons.append(dados)

    return pokemons

def escolher_pokemon(pokemons, jogador):
    print("\nJogador", jogador)

    for i in range(len(pokemons)):
        print(i + 1, "-", pokemons[i][0])

    escolha = int(input("Escolhe um Pokémon: "))

    return pokemons[escolha - 1]


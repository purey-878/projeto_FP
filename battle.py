import random

def atacar(pokemon, escolha):
    if escolha == 1:
        return int(pokemon[3])

    elif escolha == 2:
        numero = random.randint(1, 100)

        if numero <= int(pokemon[6]):
            return int(pokemon[5])
        else:
            return 0

def iniciar_batalha(jogador1, jogador2):
    hp1 = int(jogador1[7])
    hp2 = int(jogador2[7])
    
    turno = 1

    while hp1 > 0 and hp2 > 0:
        print(jogador1[0], "HP:", hp1)
        print(jogador2[0], "HP:", hp2)

        if turno == 1:
            print(" \n Turno do jogador 1 \n")
            print("1 -", jogador1[2])
            print("2 -", jogador1[4])

            escolha = int(input("Ataque: "))
            hp2 -= atacar(jogador1, escolha)
            turno = 2

        else:
            print("\n Turno do jogador 2 \n")
            print("1 -", jogador2[2])
            print("2 -", jogador2[4])

            escolha = int(input("Ataque: "))
            hp1 -= atacar(jogador2, escolha)
            turno = 1

    if hp1 > 0:
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")
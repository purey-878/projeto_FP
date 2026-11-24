from pokemon import listar_pokemons, escolher_pokemon, adicionar_pokemon
from battle import atacar, iniciar_batalha

#lists the pokemons from the pokemon.txt file
pokemons = listar_pokemons()


#fase where each player chooses a pokemon to battle with 
jogador1 = escolher_pokemon(pokemons, 1)
jogador2 = escolher_pokemon(pokemons, 2)

#display the chosen pokemons and their attacks, then starts the battle
print(jogador1[0], "VS", jogador2[0])

print("1 -", jogador1[2])
print("2 -", jogador1[4])

#starting the battle between the two chosen pokemons haha.
iniciar_batalha(jogador1, jogador2)
from pokemon import listar_pokemons, escolher_pokemon, adicionar_pokemon

print(adicionar_pokemon())
pokemons = listar_pokemons()

jogador1 = escolher_pokemon(pokemons, 1)
jogador2 = escolher_pokemon(pokemons, 2)

print(jogador1[0], "VS", jogador2[0])
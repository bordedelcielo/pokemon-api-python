import requests

# def get_poke(pokemon):
#     r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
#     print(r['types'])

#     for i in r['types']:
#         print(i['type']['name'])

#     for i in r['abilities']:
#         print(i['ability']['name'])

#     print(r['weight'])


# get_poke('pichu')

def add_poke(pokemon='pichu', pokedex=[{},{}]):
    if pokemon.title() not in pokedex[0]:
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        if r.status_code == 200:
            data = r.json()

            pokedex[0][pokemon.title()] = 0
            
            abilities = [i['ability']['name'] for i in data['abilities']]
            weight = data['weight']

            for i in data['types']:
                type_a = i['type']['name']
                if type_a not in pokedex[1]:
                    pokedex[1][type_a] = {pokemon: {'abilities': abilities, 'weight': weight}}
                else:
                    pokedex[1][type_a][pokemon] = {'abilities': abilities, 'weight': weight}
        else:
            print(pokemon, 'is not on the poke api.')

    return pokedex[1]

my_pokedex = ['pichu', 'pikachu', 'raichu', 'mewtwo', 'jigglypuff', 'goldeen', 'lucario', 'charmander', 'charizard', 'ivysaur', 'bulbasaur', 'entei', 'squirtle', 'spearow', 'fearow', 'ekans', 'arbok', 'sandslash', 'meowth', 'gloom']

def create_dex(poke_list, pokedex=[{},{}]):
    for i in poke_list:
        add_poke(i, pokedex)

    return pokedex[1]

print(create_dex(my_pokedex))
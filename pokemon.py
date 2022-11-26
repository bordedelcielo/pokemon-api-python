import requests, json

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

def make_json(py_dict):
    print(f'Creating json for Python Dictionary: {py_dict}')

    with open('pokedex.json', 'w') as fp:
        json.dump(py_dict, fp, indent=4)

make_json(create_dex(my_pokedex))
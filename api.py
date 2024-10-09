#!/usr/bin/env python3

import requests

def pokeapi(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Converte a resposta JSON para um dicionário
        data = response.json()
        
        # Extrai o nome e as habilidades do Pokémon
        pokemon_info = {
            'name': data['name'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']]
        }
        return pokemon_info

    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro na requisição: {req_err}')
    except ValueError as json_err:
        print(f'Erro ao decodificar JSON: {json_err}')
    
    return None

# Nome do Pokémon que você quer buscar
pokemon_name = 'pikachu'  # Você pode trocar 'pikachu' pelo nome de outro Pokémon
dados = pokeapi(pokemon_name)

if dados:
    print(f"Nome: {dados['name']}")
    print("Habilidades:")
    for ability in dados['abilities']:
        print(f"- {ability}")

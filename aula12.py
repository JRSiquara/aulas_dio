import requests

def retorna_dados_cep(cep):

    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    print(dados_cep['bairro'])

    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.globo.com/')
    print(response)
    # retorna_dados_cep('01001000')
    # retorna_dados_cep('04094000')
    # retorna_dados_cep('22041001')
    # retorna_dados_cep('28973053') # CEP de Praia Seca
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny']) # Retorna link e ao acessar leva p/ pag. c/ imagem pokemon.

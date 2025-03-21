#Primeiro instale a biblioteca googlesearch com o comando pip install google-search-results 
from serpapi import GoogleSearch

# parametros de busca
# q: o que você deseja pesquisar!
# location: localização
# api_key: chave da API 
# Você pode obter uma chave de API gratuita em https://serpapi.com/
# Você também pode usar a chave de teste: d1a511741963e07de51616a5d463f5d529ef68cf47a285b030e6648b26aa9fe6

params = {
    "q": "Python bibliotecas",
    'location': 'Brazil',
    'api_key': 'Sua chave de API'
}

# Cria uma instância do GoogleSearch com os parâmetros.
# O método get_dict() retorna um dicionário com os resultados da pesquisa.  
search = GoogleSearch(params)
results = search.get_dict()

# Verifica se a chave 'organic_results' existe no dicionário de resultados.
# Se existir, imprime o título e o link de cada resultado.
# Se não existir, imprime uma mensagem de erro e o dicionário completo de resultados.

if 'organic_results' in results:
  for result in results['organic_results']:
    print(f"Title: {result['title']}\nLink: {result['link']}\n")
else:
  print('Nem um resultado encontrado')
  print(f'Reposta completa: {results}')
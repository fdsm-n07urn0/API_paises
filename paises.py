import json
import sys
import requests

# HTTP requests methods -> Connect, delete, get, head, options, patch, post e trace
URL_ALL = 'https://restcountries.com/v3.1/all'
URL_NAME = 'https://restcountries.com/v3.1/name'

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisição em:', url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('Erro ao fazer parsing')

#paises = json.loads(resposta.text)   # Parsing de Json para python (Tranforma json em objetos do python)

def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}: {} habitantes'.format(pais['name'], pais['population']))
    else:
        print('Pais não encontrado')

def mostrar_moedas(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('Moedas do', pais['name'])
                moedas = pais[currencies]
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
    else:
        print('Pais não encontrado')

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print('É preciso passar o nome do pais')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('## Bem vindo ao sistema de paises ##')
        print('Uso: python paises.py <ação> <nome do país>')
        print('Ações disponiveis: contagem, moeda, populacao')
    else:
        argumento1 = sys.argv[1]
        if argumento1 == 'contagem':
            numero_de_paises = contagem_de_paises()
            print('Existem {} paises no mundo todo'.format(numero_de_paises))
        elif argumento1 == 'moeda':
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == 'populacao':
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print('Argumento inválido')

# sys.argv - É usado para acessar argumentos
# argv - É uma lista de argumentos passada pelo terminal

    #print(sys.argv)

    #mostrar_moedas('brasil')
    #mostrar_populacao('brasil')
    #texto_da_resposta = requisicao(URL_ALL)
    #if texto_da_resposta:
        #lista_de_paises = parsing(texto_da_resposta)
        #if lista_de_paises:
            #listar_paises(lista_de_paises)
            #print(contagem_de_paises(texto_depois_do_parsing))
            #print(texto_depois_do_parsing)


#print(len(paises))
#for pais in paises:
    #print(pais['name'], pais['idd'])
    #print(pais['idd'])
    #print(pais['translations'])
    #print(pais['name'])
    #print(pais)

#print(paises)
#print(type(paises[0]))
#print(paises[0])
#print(paises[0]['name'])
#print(paises[-1]['name'])
#print(type(paises))
#print(resposta.text)
#print(resposta)
#print(resposta.status_code)
#print(type(resposta))
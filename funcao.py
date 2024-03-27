import requests
import json

def pegarValor(nomeTemp):  
    request = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL") #API
    moeda =  json.loads(request.content)
    nome = moeda[f'{nomeTemp}']['name']
    valor = moeda[f'{nomeTemp}']['bid']
    #nome = moeda['USDBRL']['name']
    #valor = moeda['USDBRL']['bid']
    return nome,valor 
    
def converter(x,y): 
    nome,valor = pegarValor(y)[0],float(pegarValor(y)[1]) # Atribui as variaveis os valores da chave (y)
    temp ='' 
    #Fatiar a string até a barra
    for i in nome:
        if i == '/':
            break
        elif i != '/':
            temp = temp +i
    nome = temp
    c = x*valor
    return c




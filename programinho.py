import requests #livraria de requisição de informações de sites
import json # JavaScript object notation

# input da data desejada
data=input('Insira a data(Ano-Mês-Dia) em que desejar verificar a cotação:')

def d_esp(data):    
# busca do cotação referente a data pedida
    req=requests.get('https://ratesapi.io/api/'+data) 
# output
    cot = json.loads(req.text)
    s=print(cot)
    return(s)

d_esp(data)

import requests #livraria de requisição de informações de sites
import json # JavaScript object notation

# input da data desejada,base de câmbio e cotação
data=input('Insira a data(Ano-Mês-Dia) em que desejar verificar a cotação:')
base=input('Digite qual a moeda base de câmbio(Ex:USD): ')
city=input('Digite qual moeda deseja verificar a cotação: ')
       
def d_esp(data):    
# busca do cotação referente a data pedida
    req=requests.get('https://ratesapi.io/api/'+data+'?base='+base+'&symbols='+city) 
# output
    cot = json.loads(req.text)
    s=cot['rates'] #taxa retirada do dicionário
    d=cot['date'] # data presente no dicionário
    r=print("A cotação desejada na data mais próxima de",data,"é :",s,"em",d )
    return r

d_esp(data)

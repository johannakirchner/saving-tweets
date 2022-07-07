import tweepy as tw
import pandas as pd
import sqlite3

# variaveis com as credencias para o acesso da API v2 do twitter
consumer_key = ''
consumer_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''

# criar o client 
client = tw.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# conectando com o SQLite
con = sqlite3.connect('BD_itaipava.db')
# cursor que acessa
cur = con.cursor()

start = '2022-06-28T08:00:00Z'
end = '2022-06-29T16:00:00Z'

# procurando sobre a marca itaipava
resposta = client.search_recent_tweets(query='itaipava', max_results=100, start_time=start, end_time=end)
# armazena apenas os tweets
dados = resposta.data

# texto, rt 
cur.execute('CREATE TABLE registros (texto TEXT, RT TEXT)')

for i in dados:
    texto = i.text
    if(texto[:2] == 'RT'):
        RT = 'S'
    else:
        RT = 'N'
    cur.execute('INSERT INTO registros (texto, RT) VALUES (?,?)', (texto, RT))

# salva as alteracoes
con.commit()
con.close()


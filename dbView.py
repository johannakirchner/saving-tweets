import sqlite3
import pandas as pd
from IPython.display import display

con = sqlite3.connect('BD_itaipava.db')
# cursor que acessa
cur = con.cursor()
# query para ver os tweets 
cur.execute('SELECT * FROM registros')

resultados = cur.fetchall()

# colocando em um data frame do pandas para facilitar vizulizacao
resultados = pd.DataFrame(resultados)

display(resultados)

resultados.to_csv("output.csv")
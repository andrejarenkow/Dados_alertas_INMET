# Importação da biblioteca
import sqlitecloud
import streamlit as st

st.write('Hello')

# Conexão com o banco
conn = sqlitecloud.connect('sqlitecloud://cajzrljjsz.sqlite.cloud:8860?apikey=JVcs3H4XeiK8G81N0hT1xjtpwRWBb2DFu8yvNXHmjXM')

# Nome da database
db_name = 'bd_alertas.sqlite'
conn.execute(f'USE DATABASE {db_name}')

dados = pd.read_sql('SELECT * FROM alertas LIMIT 20', conn)

dados

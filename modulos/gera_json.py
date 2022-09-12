import datetime
import os
import pandas as pd
import PyPDF2 

#variaveis
datainicio = datetime.date.today()

arquivo = 'IMA_B_5_Lamina.pdf'
procurar_texto = 'IMA-B 5'

caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_atual, arquivo)
arquivo_pdf = open(caminho_arquivo,'rb')

def gera_json():

    objeto_pdf = PyPDF2.PdfFileReader(arquivo_pdf) 

    objeto_pagina = objeto_pdf.getPage(0) 

    texto = objeto_pagina.extractText()

    caracter_inicial = texto.find(procurar_texto) + 8

    texto_inicial = texto[caracter_inicial:150]

    caracter_final = texto_inicial.find(' ')

    valor = texto_inicial[0:caracter_final]

    dados = {'quote': [valor], 'date': [str(datainicio)]}

    df = pd.DataFrame(data=dados)

    df['quote'] = df['quote'].apply(lambda x: str(x.replace('.','')))
    df['quote'] = df['quote'].apply(lambda x: str(x.replace(',','.')))
    df['quote'] = df['quote'].astype(float, errors = 'raise')

    df.to_json('cotacao.json', orient="records")

    arquivo_pdf.close()  

    print('Arquivo Json gerado!')

if __name__ == "__main__":
    gera_json()
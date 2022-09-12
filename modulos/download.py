import requests
import os

#variaveis
arquivo = 'IMA_B_5_Lamina.pdf'
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_atual, arquivo)

def download_file():

    URL = "https://www.anbima.com.br/data/files/9B/92/8B/AE/755FE610DC784BE6192BA2A8/" + arquivo

    try:   
        response = requests.get(URL)
        
        if response.status_code == 200:
            open(caminho_arquivo, "wb").write(response.content)   
            print('Download Conlcuido!')      

        else:
            print('Erro: ', response.status_code, '-', response.reason)

    except:
        response = requests.get(URL)
        print('Erro no Request!' , response.raise_for_status(),'FIM') #incluir como tratamento de erro

if __name__ == "__main__":
    download_file()
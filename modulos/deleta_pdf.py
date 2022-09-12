import os

#variaveis
arquivo = 'IMA_B_5_Lamina.pdf'
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_atual, arquivo)

def deleta_pdf():
    
    os.remove(caminho_arquivo)
    print('Pdf apagado!')

if __name__ == "__main__":
    deleta_pdf()    
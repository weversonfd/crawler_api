# Crawler Api

### Um teste para colocar a cotação do índice IMA-B 5 publicado pela Anbima em uma API usando Python.

### Orientações:

- Na pasta "Modulos", estão as funções utilizadas
- O script "executa_processo.py", executa todos os processos na sequência correta criando o arquivo Json para ser consumido pelo webservice.
- O script "app.py" sobe um serviço em Flask para entregar a cotação via API no endpoint /api/v1/cota recebendo requisições "GET"

### download.py

Este scrpit é responsável por fazer o download do arquivo em PDF disponibilizado no link baixo:

 https://www.anbima.com.br/pt_br/informar/precos-e-indices/indices/ima.htm#Laminas

### gera_json.py

Este script é responsável por tratar o PDF e transformar em um arquivo Json para ser consumido pelo webservice.

### deleta_pdf.py

Este scrpit é responsável por apagar o arquivo pdf baixado.

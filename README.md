# Trabalho 1 = Introdução a banco de dados 

Exporta as tabelas de bancos de dados MySQL e PostgresSQL para o formatato .csv

## Rodando a aplicação
Essa aplicação foi desenolvida no sistema operacional Ubuntu 20.04, porem pode ser utilizada no sistema Windows, sem 
a necessidade de alteração de codigo

### Commandos para rodar em linux a aplicação
- Instale as dependencias utilizando o comando `pip install -r requirements.txt`
- Rode `python3 run.py {tipoDatabase(postgres ou MySQL)} -host {HOST} -u {USERNAME} -p {PASSWORD} -d {DATABASE}`

### Commandos para rodar em windows a aplicação
- Instale as dependencias utilizando o comando `pip install -r requirements.txt`
- Rode `python run.py {tipoDatabase(postgres ou MySQL)} -host {HOST} -u {USERNAME} -p {PASSWORD} -d {DATABASE}`
'''
Link - IMDb Non-Commercial Datasets
https://developer.imdb.com/non-commercial-datasets/
'''

## Importando bibliotecas

import pandas as pd
import os

## Reparticionando as bases em pedaços menores

'''
Nesta parte, é feita a leitura dos arquivos TSV, e em seguida, a divisão desses arquivos em chunks de 10M, 
para no fim, criar um novo dataset a partir desses pedaços. 
'''


def split_file(input_file, output_folder, chunk_size=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    total_lines = 0  # Inicializar contador de linhas

    with open(input_file, 'r', encoding='utf-8') as f:
        header = f.readline()  # Assuming the first line contains headers
        chunk_number = 1
        while True:
            lines = f.readlines(chunk_size * 1024 * 1024)  # Read 10MB at a time
            if not lines:
                break
            total_lines += len(lines)  # Contar o número de linhas no chunk
            with open(os.path.join(output_folder, f'chunk_{chunk_number}.tsv'), 'w', encoding='utf-8') as chunk_file:
                chunk_file.write(header)
                chunk_file.writelines(lines)
            chunk_number += 1

    return total_lines  # Retornar o número total de linhas do arquivo

# Lista de arquivos TSV
files = ['name.basics.tsv', 'title.principals.tsv', 'title.ratings.tsv', 'title.basics.tsv', 'title.akas.tsv', 'title.crew.tsv', 'title.episode.tsv']

# Leitura dos arquivos, dividindo em chunks de 10MB
total_lines_per_file = {}  # Dicionário para armazenar o número total de linhas por arquivo
for file in files:
    input_file = f'{file}'  # Substitua 'path/to/' pelo caminho para os seus arquivos
    output_folder = f'TESTE/{file[:-4]}'  # Substitua 'path/to/output/' pelo caminho para a pasta de saída
    total_lines = split_file(input_file, output_folder)
    total_lines_per_file[file] = total_lines

# Imprimir o número total de linhas por arquivo
for file, total_lines in total_lines_per_file.items():
    print(f"Arquivo: {file}, Quantidade total de linhas: {total_lines}")

'''
Agora, cada dataset pode ser acessado pelos índices da lista, por exemplo:
datasets[0] para o dataset do primeiro arquivo
datasets[1] para o dataset do segundo arquivo
e assim por diante

NOME DO ARQUIVO         ÍNDICE
'name.basics.tsv'       = 0
'title.principals.tsv'  = 1
'title.ratings.tsv'     = 2
'title.basics.tsv'      = 3
'title.akas.tsv'        = 4
'title.crew.tsv'        = 5
'title.episode.tsv'     = 6

# OBSERVAÇÃO: O 'chunk_1' de um arquivo corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', 
   e assim successivamente.

'''
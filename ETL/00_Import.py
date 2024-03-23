'''
Link - IMDb Non-Commercial Datasets
https://developer.imdb.com/non-commercial-datasets/
'''

## Importando bibliotecas

import pandas as pd
import os

## Reparticionando as bases em pedaços menores

def split_file(input_file, output_folder, chunk_size=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, 'r', encoding='utf-8') as f:
        header = f.readline()  # Assuming the first line contains headers
        chunk_number = 1
        while True:
            lines = f.readlines(chunk_size * 1024 * 1024)  # Read 10MB at a time
            if not lines:
                break
            with open(os.path.join(output_folder, f'chunk_{chunk_number}.tsv'), 'w', encoding='utf-8') as chunk_file:
                chunk_file.write(header)
                chunk_file.writelines(lines)
            chunk_number += 1

# Lista de arquivos TSV
files = ['name.basics.tsv', 'title.principals.tsv', 'title.ratings.tsv', 'title.basics.tsv', 'title.akas.tsv', 'title.crew.tsv', 'title.episode.tsv']

# Leitura dos arquivos, dividindo em chunks de 10MB
for file in files:
    input_file = f'{file}'  # Substitua 'path/to/' pelo caminho para os seus arquivos
    output_folder = f'TESTE/{file[:-4]}'  # Substitua 'path/to/output/' pelo caminho para a pasta de saída
    split_file(input_file, output_folder)

# Criar um dataset combinando os chunks de cada arquivo
datasets = []
for file in files:
    output_folder = f'TESTE/{file[:-4]}'  # Substitua 'path/to/output/' pelo caminho para a pasta de saída
    chunks = [pd.read_csv(os.path.join(output_folder, chunk), sep='\t') for chunk in os.listdir(output_folder)]
    dataset = pd.concat(chunks)
    datasets.append(dataset)
'''
Agora você tem uma lista de datasets, um para cada arquivo
Você pode acessar cada dataset pelos índices da lista, por exemplo:
datasets[0] para o dataset do primeiro arquivo
datasets[1] para o dataset do segundo arquivo
e assim por diante
'''


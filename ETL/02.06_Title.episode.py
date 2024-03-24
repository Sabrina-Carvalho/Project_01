### ANALISANDO OS DATASETS
### 0 - Analisando title.basics, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- title.episode --
tconst (string) - alphanumeric identifier of episode
parentTconst (string) - alphanumeric identifier of the parent TV Series
seasonNumber (integer) – season number the episode belongs to
episodeNumber (integer) – episode number of the tconst in the TV series
'''

# Lista o cabeçalho
print(datasets[6].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[6].head())

#Informações gerais da base
print(datasets[6].info())

# Verificando quantos valores nulos há na base
print('tconst', datasets[6]['tconst'].isnull().sum())
print('parentTconst', datasets[6]['parentTconst'].isnull().sum())
print('seasonNumber', datasets[6]['seasonNumber'].isnull().sum())
print('episodeNumber', datasets[6]['episodeNumber'].isnull().sum())

### Transformando o tipo da coluna

# Como observado acima, a base possui valores '\N'.
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
# datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[6]['seasonNumber'] = datasets[6]['seasonNumber'].replace(r'\\N', '', regex=True).astype(str)
datasets[6]['episodeNumber'] = datasets[6]['episodeNumber'].replace(r'\\N', '', regex=True).astype(str)

# Verifica os valores únicos da base
print(datasets[5]['tconst'].unique())
print(datasets[5]['parentTconst'].unique())
print(datasets[5]['seasonNumber'].unique())
print(datasets[5]['episodeNumber'].unique())
### ANALISANDO OS DATASETS
### 0 - Analisando title.basics, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- title.crew --
tconst (string) - alphanumeric unique identifier of the title
directors (array of nconsts) - director(s) of the given title
writers (array of nconsts) – writer(s) of the given title
'''

# Lista o cabeçalho
print(datasets[5].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[5].head())

#Informações gerais da base
print(datasets[5].info())

# Verificando quantos valores nulos há na base
print('tconst', datasets[5]['tconst'].isnull().sum())
print('directors', datasets[5]['directors'].isnull().sum())
print('writers', datasets[5]['writers'].isnull().sum())

### Transformando o tipo da coluna

# Como observado acima, a base possui valores '\N'.
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
# datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[5]['writers'] = datasets[5]['writers'].replace(r'\\N', '', regex=True).astype(str)
datasets[5]['directors'] = datasets[5]['directors'].replace(r'\\N', '', regex=True).astype(str)

# Verifica os valores únicos da base
print(datasets[5]['tconst'].unique())
print(datasets[5]['directors'].unique())
print(datasets[5]['writers'].unique())
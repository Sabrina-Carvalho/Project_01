### ANALISANDO OS DATASETS
### 0 - Analisando title.principal, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- title.principals --
tconst (string) - alphanumeric unique identifier of the title
ordering (integer) – a number to uniquely identify rows for a given titleId
nconst (string) - alphanumeric unique identifier of the name/person
category (string) - the category of job that person was in
job (string) - the specific job title if applicable, else '\N'
characters (string) - the name of the character played if applicable, else '\N'
'''

# Lista o cabeçalho
print(datasets[1].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[1].head())

#Informações gerais da base
print(datasets[1].info())

    # Verificando quantos valores nulos há na base
print(datasets[1]['tconst'].isnull().sum())
print(datasets[1]['ordering'].isnull().sum())
print(datasets[1]['nconst'].isnull().sum())
print(datasets[1]['category'].isnull().sum())
print(datasets[1]['job'].isnull().sum())
print(datasets[1]['characters'].isnull().sum())

#Mostrar o tipo do campo
print(datasets[1].dtypes)

print(datasets[1]['tconst'].unique())
print(datasets[1]['ordering'].unique())
print(datasets[1]['nconst'].unique())
print(datasets[1]['category'].unique())
print(datasets[1]['job'].unique())
print(datasets[1]['characters'].unique())

# Como observado acima, a base não possui valores nulos, no lugar, há a expressão '\N'. 
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
# datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[1]['job'] = datasets[1]['job'].replace(r'\\N', '', regex=True).astype(str)
datasets[1]['characters'] = datasets[1]['characters'].replace(r'\\N', '', regex=True).astype(str)
datasets[1]['characters'] = datasets[1]['characters'].str.replace(r'\[|\]', '', regex=True)
datasets[1]['characters'] = datasets[1]['characters'].str.replace('"', '')
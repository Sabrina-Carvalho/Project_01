### ANALISANDO O DATASET
### 0 - Analisando name.basics, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- name.basics --
nconst (string) - alphanumeric unique identifier of the name/person
primaryName (string)– name by which the person is most often credited
birthYear – in YYYY format
deathYear – in YYYY format if applicable, else '\N'
primaryProfession (array of strings)– the top-3 professions of the person
knownForTitles (array of tconsts) – titles the person is known for
'''

# Lista o cabeçalho
print(datasets[0].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[0].head())

#Informações gerais da base
print(datasets[0].info())

# Verificando quantos valores nulos há na base
print('nconst', datasets[0]['nconst'].isnull().sum())
print('primaryName', datasets[0]['primaryName'].isnull().sum())
print('birthYear', datasets[0]['birthYear'].isnull().sum())
print('deathYear', datasets[0]['deathYear'].isnull().sum())
print('primaryProfession', datasets[0]['primaryProfession'].isnull().sum())
print('knownForTitles', datasets[0]['knownForTitles'].isnull().sum())

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'primaryName'
mask_primary = datasets[0]['primaryName'].isnull()

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'primaryProfession'
mask_original = datasets[0]['primaryProfession'].isnull()

# Filtrar o DataFrame usando as máscaras
null_primary = datasets[0][mask_primary]
null_original = datasets[0][mask_original]

# Imprimir as linhas com valores nulos na coluna 'primaryName'
print("Linhas com valores nulos na coluna 'title':")
print(null_primary)

# Imprimir as linhas com valores nulos na coluna 'primaryProfession'
print("\nLinhas com valores nulos na coluna 'primaryProfession':")
print(null_original)

### Transformando o tipo da coluna

# Como observado acima, a base não possui valores nulos, no lugar, há a expressão '\N'. 
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
# datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[0]['birthYear'] = datasets[0]['birthYear'].replace(r'\\N', '', regex=True).astype(str)
datasets[0]['deathYear'] = datasets[0]['deathYear'].replace(r'\\N', '', regex=True).astype(str)
datasets[0]['knownForTitles'] = datasets[0]['knownForTitles'].replace(r'\\N', '', regex=True).astype(str)

# Substituir todos os valores NaN por uma string vazia ("") nas colunas 'primaryProfession' e 'primaryName'
datasets[0]['primaryProfession'] = datasets[0]['primaryProfession'].fillna("")
datasets[0]['primaryName'] = datasets[0]['primaryName'].fillna("")

# Verificar se a substituição foi feita corretamente
print(datasets[0].head())

# Verifica os valores únicos da base
print(datasets[0]['nconst'].unique())
print(datasets[0]['primaryName'].unique())
print(datasets[0]['birthYear'].unique())
print(datasets[0]['deathYear'].unique())
print(datasets[0]['primaryProfession'].unique())
print(datasets[0]['knownForTitles'].unique())
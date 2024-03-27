### ANALISANDO OS DATASETS
### 0 - Analisando title.basics, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- title.basics --
tconst (string) - alphanumeric unique identifier of the title
titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
originalTitle (string) - original title, in the original language
isAdult (boolean) - 0: non-adult title; 1: adult title
startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
endYear (YYYY) – TV Series end year. ‘\N’ for all other title types
runtimeMinutes – primary runtime of the title, in minutes
genres (string array) – includes up to three genres associated with the title
'''

# Lista o cabeçalho
print(datasets[3].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[3].head())

#Informações gerais da base
print(datasets[3].info())

# Verificando quantos valores nulos há na base
print(datasets[3]['tconst'].isnull().sum())
print(datasets[3]['titleType'].isnull().sum())
print(datasets[3]['primaryTitle'].isnull().sum())
print(datasets[3]['originalTitle'].isnull().sum())
print(datasets[3]['isAdult'].isnull().sum())
print(datasets[3]['startYear'].isnull().sum())
print(datasets[3]['endYear'].isnull().sum())
print(datasets[3]['runtimeMinutes'].isnull().sum())
print(datasets[3]['genres'].isnull().sum())

'''
No código acima, foi retornado 12 linhas nulas para as colunas primaryTitle e originalTitle cada, e 18 linhas para a coluna genres.
Como no processo final essas colunas não agregaram à análise, foi decidido a exclusão das mesmas à posteriori.
'''

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'primaryTitle'
mask_primary = datasets[3]['primaryTitle'].isnull()

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'originalTitle'
mask_original = datasets[3]['originalTitle'].isnull()

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'genres'
mask_secundary = datasets[3]['genres'].isnull()


# Filtrar o DataFrame usando as máscaras
null_primary = datasets[3][mask_primary]
null_original = datasets[3][mask_original]
null_secundary = datasets[3][mask_secundary]

# Imprimir as linhas com valores nulos na coluna 'primaryTitle'
print("Linhas com valores nulos na coluna 'primaryTitle':")
print(null_primary)


# Imprimir as linhas com valores nulos na coluna 'originalTitle'
print("\nLinhas com valores nulos na coluna 'originalTitle':")
print(null_original)


# Imprimir as linhas com valores nulos na coluna 'genres'
print("\nLinhas com valores nulos na coluna 'genres':")
print(null_secundary)

### Transformando o tipo da coluna

# Como observado acima, a base possui valores '\N'.
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[3]['endYear'] = datasets[3]['endYear'].replace(r'\\N', '', regex=True).astype(str)
datasets[3]['startYear'] = datasets[3]['startYear'].replace(r'\\N', '', regex=True).astype(str)
datasets[3]['runtimeMinutes'] = datasets[3]['runtimeMinutes'].replace(r'\\N', '', regex=True).astype(str)
datasets[3]['genres'] = datasets[3]['genres'].replace(r'\\N', '', regex=True).astype(str)
datasets[3]['isAdult'] = datasets[3]['isAdult'].replace(r'\\N', '', regex=True).astype(str)

# Substituir todos os valores NaN por uma string vazia ("") nas colunas 'primaryProfession' e 'primaryName'
datasets[3]['originalTitle'] = datasets[3]['originalTitle'].fillna("")
datasets[3]['primaryTitle'] = datasets[3]['primaryTitle'].fillna("")

# Verificar se a substituição foi feita corretamente
print(datasets[3].head())

# Verifica os valores únicos da base
print(datasets[3]['tconst'].unique())
print(datasets[3]['titleType'].unique())
print(datasets[3]['primaryTitle'].unique())
print(datasets[3]['originalTitle'].unique())
print(datasets[3]['isAdult'].unique())
print(datasets[3]['startYear'].unique())
print(datasets[3]['endYear'].unique())
print(datasets[3]['runtimeMinutes'].unique())
print(datasets[3]['genres'].unique())
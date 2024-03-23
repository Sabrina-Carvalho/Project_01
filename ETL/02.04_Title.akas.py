### ANALISANDO OS DATASETS
### 0 - Analisando title.akas, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- title.akas --
titleId (string) - a tconst, an alphanumeric unique identifier of the title
ordering (integer) – a number to uniquely identify rows for a given titleId
title (string) – the localized title
region (string) - the region for this version of the title
language (string) - the language of the title
types (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". New values may be added in the future without warning
attributes (array) - Additional terms to describe this alternative title, not enumerated
isOriginalTitle (boolean) – 0: not original title; 1: original title
'''

# Lista o cabeçalho
print(datasets[4].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[4].head())

#Informações gerais da base
print(datasets[4].info())

# Verificando quantos valores nulos há na base
print('titleId', datasets[4]['titleId'].isnull().sum())
print('ordering', datasets[4]['ordering'].isnull().sum())
print('title', datasets[4]['title'].isnull().sum())
print('region', datasets[4]['region'].isnull().sum())
print('language', datasets[4]['language'].isnull().sum())
print('types', datasets[4]['types'].isnull().sum())
print('attributes', datasets[4]['attributes'].isnull().sum())
print('isOriginalTitle', datasets[4]['isOriginalTitle'].isnull().sum())

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'title'
mask_primary = datasets[4]['title'].isnull()

# Criar uma máscara booleana para identificar linhas com valores nulos na coluna 'region'
mask_original = datasets[4]['region'].isnull()

# Filtrar o DataFrame usando as máscaras
null_primary = datasets[4][mask_primary]
null_original = datasets[4][mask_original]

# Imprimir as linhas com valores nulos na coluna 'title'
print("Linhas com valores nulos na coluna 'title':")
print(null_primary)

# Imprimir as linhas com valores nulos na coluna 'region'
print("\nLinhas com valores nulos na coluna 'region':")
print(null_original)

### Transformando o tipo da coluna

# Como observado acima, a base possui valores '\N'.
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
# datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[4]['attributes'] = datasets[4]['attributes'].replace(r'\\N', '', regex=True).astype(str)
datasets[4]['types'] = datasets[4]['types'].replace(r'\\N', '', regex=True).astype(str)
datasets[4]['language'] = datasets[4]['language'].replace(r'\\N', '', regex=True).astype(str)

# Substituir todos os valores NaN por uma string vazia ("") nas colunas 'title' e 'region'
datasets[4]['region'] = datasets[4]['region'].fillna("")
datasets[4]['title'] = datasets[4]['title'].fillna("")

# Verificar se a substituição foi feita corretamente
print(datasets[3].head())  # ou qualquer outra forma de visualização que você esteja utilizando
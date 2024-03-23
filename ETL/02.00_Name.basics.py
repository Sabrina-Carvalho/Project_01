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
print(datasets[0]['nconst'].isnull().sum())
print(datasets[0]['primaryName'].isnull().sum())
print(datasets[0]['birthYear'].isnull().sum())
print(datasets[0]['deathYear'].isnull().sum())
print(datasets[0]['primaryProfession'].isnull().sum())
print(datasets[0]['knownForTitles'].isnull().sum())

#Mostrar o tipo do campo
print(datasets[0].dtypes)

print(datasets[0]['nconst'].unique())
print(datasets[0]['primaryName'].unique())
print(datasets[0]['birthYear'].unique())
print(datasets[0]['deathYear'].unique())
print(datasets[0]['primaryProfession'].unique())
print(datasets[0]['knownForTitles'].unique())

### Transformando o tipo da coluna

# Como observado acima, a base não possui valores nulos, no lugar, há a expressão '\N'. 
# Sendo assim, para a conversão dos campos para string, será necessário substituir tal expressão por ''
# datasets[0] = datasets[0].replace(r'\\N', '', regex=True)
datasets[0]['nconst'] = datasets[0]['nconst'].astype(str)
datasets[0]['primaryName'] = datasets[0]['primaryName'].astype(str)
datasets[0]['birthYear'] = datasets[0]['birthYear'].replace(r'\\N', '', regex=True).astype(str)
datasets[0]['deathYear'] = datasets[0]['deathYear'].replace(r'\\N', '', regex=True).astype(str)
datasets[0]['primaryProfession'] = datasets[0]['primaryProfession'].astype(str)
datasets[0]['knownForTitles'] = datasets[0]['knownForTitles'].astype(str)
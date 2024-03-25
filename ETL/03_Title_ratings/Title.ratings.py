### ANALISANDO OS DATASETS
### 0 - Analisando title.ratings, 'chunk_1'
# OBSERVAÇÃO: O 'chunk_1' corresponde ao índice '0', e o 'chunk_2' corresponde ao índice '1', e assim successivamente.

'''
-- title.ratings --
tconst (string) - alphanumeric unique identifier of the title
averageRating – weighted average of all the individual user ratings
numVotes - number of votes the title has received
'''

# Lista o cabeçalho
print(datasets[2].keys())

# Mostra o cabeçalho e dá exemplos dos dados da base
print(datasets[2].head())

#Informações gerais da base
print(datasets[2].info())

# Verificando quantos valores nulos há na base
print('tconst', datasets[2]['tconst'].isnull().sum())
print('averageRating', datasets[2]['averageRating'].isnull().sum())
print('numVotes', datasets[2]['numVotes'].isnull().sum())

# Verifica os valores únicos da base
print(datasets[2]['tconst'].unique())
print(datasets[2]['averageRating'].unique())
print(datasets[2]['numVotes'].unique())
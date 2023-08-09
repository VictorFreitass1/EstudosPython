import json
import glob

dicionario = {
    'nome': 'Victor Freitas',
    'idade' : 19,
    'altura' : 1.80,
    'status' : True,
    'linguagens' : [
        {'linguagem': 'python', 'proficiencia': 6},
        {'linguagem': 'java', 'proficiencia': 6},
        {'linguagem': 'c/c++', 'proficiencia': 0},
        {'linguagem': 'javascript', 'proficiencia': 3},
        {'linguagem': 'rust', 'proficiencia': 0},
        {'linguagem': 'c#', 'proficiencia': 5}, 
        {'linguagem': 'sql', 'proficiencia': 4},
    ]
} 

for i in dicionario['linguagens']:
    if i['proficiencia'] > 5:
        print('Linguagem: ', i ['linguagem'], ' Proeficiência: ', i['proficiencia'])

dicionario['nome'] [0:6]
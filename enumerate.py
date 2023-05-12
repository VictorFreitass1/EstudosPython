import json
import glob

dicionario = {
    'nome': 'Victor Freitas',
    'idade' : 19,
    'altura' : 1.80,
    'status' : True,
    'treinamentos' : {
        'python' : [9, 7 ,6 ,8],
        'java' : [2],
        'c/c++' : [3],
        'javascript' : [3],
        'rust' : [2, 8],
        'c#' : [6],
        'sql' : [9, 7, 7]
}
} 

for i, j in dicionario['treinamentos'].items():
    print('Linguagem: ',i)

    for i, nota in enumerate(j):
        print(f'Curso{i +1} - nota: {nota}')
    print()
dicionario['nome'] [0:6]
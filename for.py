criancas = "Enzo", "Paola", "Valentina", "Laura"

for index in range(len(criancas)):
    print(criancas[index], index)

print('outro exemplo')


for index in range(5):
    if index == 3:
        print('primeira linha')
    else:
        print(f'outras linhas{index}')



print('outro exemplo')
print('--------------------')


matrix_numeros = [
    ['1,2,3'],
    ['4,5,6'],
    ['7,8,9'],
    ['0']
]

for linha in matrix_numeros:
    print("========")
    for coluna in linha:
        print(coluna)
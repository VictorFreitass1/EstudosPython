numero = int(input('Digite um número: '))


if numero % 2 != 0:
    numero = numero - 1

for num in range(numero, -1, -2):
    print(num)
    

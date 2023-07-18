'''
SEQUENCIA DE FIBONACCI
'''
print('-' * 30)
print('    SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
while True:    
    try:
        posicao = int(input('Informe a quantidade de termos: '))
    except ValueError:
            print('Insira apenas números inteiros.')
            continue
    if posicao == 1:
        print(f'Sequência de {posicao} termo:')
        print(0)
        break
    elif posicao == 2:
        print(f'Sequência de {posicao} termos:')
        print(0, end=' ')
        print(1)
        break
    elif posicao > 2:
        a = 0
        b = 1
        print(f'Sequência de {posicao} termos:')
        print(0, end=' ')
        print(1, end=' ')
        for x in range(posicao - 2): 
            c = a + b
            print (c, end=' ')
            a = b
            b = c
        break
# SEQUENCIA DE FIBONACCI

sequencia = []

def fibonacci(posicao):   
    if posicao == 1:
        return f"{posicao}º termo na sequência: {0}"
        
    elif posicao == 2:
        return f"Sequência para {posicao} termos: {0, 1}"
    
    else:
        a = 0
        b = 1
        sequencia = [0, 1]
        for _ in range(posicao - 2): 
            c = a + b
            sequencia.append(c)
            a = b
            b = c
        return f"Sequência para {posicao} termos: {tuple(sequencia)}"

print('-' * 30)
print('    SEQUÊNCIA DE FIBONACCI')
print('-' * 30)

while True:    
    try:
        termo = int(input('Informe a quantidade de termos para gerar a sequência: '))
        if termo <= 0:
             print("Insira um valor maior que zero.")
             continue
        break
    except ValueError:
            print('Valor inválido! Insira apenas números inteiros.')
            continue

print(fibonacci(termo))
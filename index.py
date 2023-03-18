from random import randint

vitorias = 0; derrotas = 0

while True:
    try:
        numJogador = int(input('Digite qualquer número entre 1 e 10: '))
        if numJogador < 0 or numJogador > 10:
            print('Digite um número válido.')
    except:
        print('Digite um número válido.')
    else:
        parImp = str(input('Par ou Ímpar? [P/I] ').lower())

        numMaquina = randint(0, 10)

        resultado = numJogador + numMaquina

        print(f'Você escolheu {numJogador} e o computador escolheu {numMaquina}. Total = {resultado}')

        if resultado % 2 == 0:
            print('Deu PAR!')
            if parImp == 'p':
                print('Jogador 1 venceu!')
                vitorias += 1
            else:
                print('Jogador 2 venceu!')
                derrotas += 1
        else:
            print('Deu ÍMPAR!')
            if parImp == 'i':
                print('Jogador 1 venceu!')
                vitorias += 1
            else:
                print('Jogador 2 venceu!')
                derrotas += 1

    res = str(input('Jogar novamente? [S/N] ').lower())

    if res == 'n':
        break

print('Fim de jogo.')
print(f'Vitórias: {vitorias}')
print(f'Derrotas: {derrotas}')
from random import randint
from time import sleep
print('-=-'*30)
print('JoKenPo')
print('-=-'*30)
computador = randint(1,3)
jogadas = ['Pedra', 'Papel', 'Tesoura']
print('Escolha Pedra, papel ou tesoura:\n'
           '(1)Pedra\n'
           '(2)Papel\n'
           '(3)Tesoura')
jogador = int(input('Qual sua jogada? '))
print('Jo..')
sleep(1)
print('Ken..')
sleep(1)
print('Pô!!!')
sleep(1)
if computador == 1 and jogador == 1:
    print('Jogador {} vs Computador {}\n'
          'Deu \033[033mEMPATE\033[m'.format(jogadas[0], jogadas[0]))
elif computador == 2 and jogador == 2:
    print('Jogador {} vs Computador {}\n'
          'Deu \033[033mEMPATE\033[m'.format(jogadas[1], jogadas[1]))
elif computador == 3 and jogador == 3:
    print('Jogador {} vs Computador {}\n'
          'Deu \033[033mEMPATE\033[m!'.format(jogadas[2], jogadas[2]))
elif computador == 1 and jogador == 2:
    print('Jogador {} vs Computador {}\n'
          'Você \033[032mVENCEU\033[m!'.format(jogadas[1], jogadas[0]))
elif computador == 2 and jogador == 3:
    print('Jogador {} vs Computador {}\n'
          'Você \033[032mVENCEU\033[m!'.format(jogadas[2], jogadas[1]))
elif computador == 3 and jogador == 1:
    print('Jogador {} vs Computador {}\n'
          'Você \033[032mVENCEU\033[m!'.format(jogadas[0], jogadas[2]))
elif computador == 1 and jogador == 3:
    print('Jogador {} vs Computador {}\n'
          'Você \033[031mPERDEU\033[m!'.format(jogadas[2], jogadas[0]))
elif computador == 2 and jogador == 1:
    print('Jogador {} vs Computador {}\n'
          'Você \033[031mPERDEU\033[m!'.format(jogadas[0], jogadas[1]))
elif computador == 3 and jogador == 2:
    print('Jogador {} vs Computador {}\n'
          'Você \033[031mPERDEU\033[m!'.format(jogadas[1], jogadas[2]))
elif jogador != 1 != 2 !=3 != 1:
    print('Jogada Inválida!')
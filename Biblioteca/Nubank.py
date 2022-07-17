from .pessoa import Cliente
import time


class Nubank:
    print('\033[1;44m\033[1;34m████████████████\033[0;0m NUBANK - CONTA E CARTÃO ----------')
    print('\033[1;44m\033[1;34m██\033[0;0m\033[1;44m▒▒\033[1;34m█\033[0;0m\033[1;44m▒▒\033[1;34m██\033[0;0m\033[1;44m'
          '▒\033[1;34m████\033[0;0m\033[1;44m▒\033[1;34m█\033[0;0m')
    print('\033[1;44m\033[1;34m██\033[0;0m\033[1;44m▒\033[1;34m█\033[0;0m\033[1;44m▒\033[1;34m██\033[0;0m\033[1;44m'
          '▒\033[1;34m█\033[0;0m\033[1;44m▒\033[1;34m████\033[0;0m\033[1;44m▒\033[1;34m█\033[0;0m')
    print('\033[1;44m\033[1;34m██\033[0;0m\033[1;44m▒\033[1;34m████\033[0;0m\033[1;44m▒\033[1;34m█\033[0;0m'
          '\033[1;44m▒\033[1;34m██\033[0;0m\033[1;44m▒\033[1;34m█\033[0;0m\033[1;44m▒\033[1;34m█\033[0;0m')
    print('\033[1;44m\033[1;34m██\033[0;0m\033[1;44m▒\033[1;34m████\033[0;0m\033[1;44m▒\033[1;34m██\033[0;0m'
          '\033[1;44m▒▒\033[1;34m█\033[0;0m\033[1;44m▒\033[1;34m██\033[0;0m')
    print('----------credito,debito,pix e mais ----------')
    print('Banco top 1 do brasil')
    print('---Classificações e Avaliações---')
    print('   ▒')
    print('  ▒▒▒     ▒▒▒▒▒▒▒▒    ***** \033[1;43m                 \033[0;0m')
    print(' ▒  ▒     ▒      ▒     **** \033[1;43m    \033[0;0m')
    print('▒▒▒▒▒      ▒▒▒▒▒▒       *** \033[1;43m  \033[0;0m')
    print('    ▒     ▒      ▒       ** \033[1;43m \033[0;0m')
    print('    ▒  ▒  ▒▒▒▒▒▒▒▒        * \033[1;43m  \033[0;0m')
    print('                        595.424 Classificações')
    enter = input('Abrir?[s/n]: ')
    if enter == 's':
        print('Abrindo')
        print(f'CA')
        time.sleep(0.3)
        print(f'   RE')
        time.sleep(0.3)
        print(f'      GAN')
        time.sleep(0.3)
        print(f'          DO')

        def openbank(self):
            nome = input('Digite seu nome ')
            idade = input('Digite sua idade ')

            pessoa = Cliente(nome, idade)
            pessoa.logar()
    else:
        print('Ate mais')

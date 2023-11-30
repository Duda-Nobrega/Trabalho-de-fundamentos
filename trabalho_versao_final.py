import random


print ('Olá Aventureiro, espero que esteja animado para a sua aventura!\n Primeiro escolha uma opção:')
opcao = int(input(' 1.Embarcar em uma Nova missão\n 2.Explorar o último desafio\n 3.Abandonar a Convanção(Sair)\n'))
tentativas = 0
while opcao != 3:
    if opcao == 1:
        print('Então vamos começar a nossa aventura!')
        nome = input('Mas primeito, entre seu nome: ')
        numero = random.randint(1,100)
        escolha = int(input('Transmita um número às estrelas '))
        while escolha != numero:
            if escolha > numero:
                print('O número transmitido está em uma órbita mais elevada! Tente novamente ')
                tentativas +=1
            elif escolha < numero:
                print('O número transmitido está em uma órbita inferior! Tente novamente  ')
                tentativas +=1
            escolha = int(input('Transmita um número às estrelas '))
            print('Parabéns!! O número transmitido está em sintonia com o código')
    elif opcao == 2:
        print(f'O nome do último aventureiro foi', nome, 'e chegou em sintonia com o código em', tentativas, 'tentativas')       
    else:
        print('Opção não reconhecida')
    opcao = int(input(' 1.Embarcar em uma Nova missão\n 2.Explorar o último desafio\n 3.Abandonar a Convanção(Sair)\n'))
if opcao == 3:
    print('Que os astros sempre te levem seguro em direção a sua jornada.\n Até a proxima missão, meu companheiro')
    
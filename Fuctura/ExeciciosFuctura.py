def exercio1e2():
    usuario = (int(input('Digite um numero: ').strip()))
    for c in range(1, usuario + 1):
        print(c)


# exercio1e2()

def exercio3():
    soma = 0
    for c in range(1, 4):
        usuario = int(input('Digite {} numero: '.format(c)).strip())
        soma = soma + usuario
    print('a soma de todos  os {}'.format(soma))


# exercio3()


def exercio4():
    usuario = int(input('Digite um numero par: ').strip())
    if usuario % 2 == 0:
        print('O numero escolhido é Par !')
    else:
        print(f'o numero {usuario} Nao é par')


# exercio4()

def exercio5():
    pass

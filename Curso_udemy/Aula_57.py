"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


def exercio():
    usuario = input('Digite um numero: ').strip()
    if usuario.isdigit():
        usuario_int = int(usuario)
        if usuario_int % 2 == 0:
            print('O numero escolhido é Par !')
        else:
            print(f'o numero {usuario} é impar')
    else:
        print('nao é numero inteiro')


# exercio()
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


def exercio2():
    usuario = int(input('Me diga as horas: ').strip())
    if usuario <= 11:
        print('Bom dia !')
    elif usuario <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')


exercio2()
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


def exercio3():
    usuario = str(input('digite seu nome').strip())
    if len(usuario) <= 4:
        print('Nome curto')
    elif len(usuario) >= 6:
        print('nome normal')
    else:
        print('nome grande')


exercio3()

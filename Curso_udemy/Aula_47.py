nome = str(input('Digite seu nome: ').strip())
idade = str(input('Digite sua idade: ').strip())
nome2 = nome.split()
if nome and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome [::-1]}')
    print(f'Seu nome contem {nome.count(" ")} espacos')
    print(f'seu nome tem {len ("".join(nome2))} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Descupe, vc deixou o campos vazios')

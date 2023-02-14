'''Calculadora com While'''

while True:
    print('**** Calculadora ****')
    numero = print(float(input('Digite um numero: ').strip()))
    numero2 = print(float(input('Digite outro numero: ').strip()))
    mat = str(print(input(
        'Quer \n somar [+] \n subtrair [-] \n Mutiplicar [x] \n Dividir [/] : ').strip()))
    if mat == "+":
        print(f'A soma é {numero+numero2}')
    elif mat == '-':
        print(f'A subtracão é {numero-numero2}')
    elif mat == 'x':
        print(f'Mutiplicacão é {numero*numero2}')
    elif mat == '/':
        print(f'Divisão é {numero/numero2}')
    else:
        print('Não selecionou corretamente')

    print("1 para SAIR")
    if int(input()) == 1:
        break

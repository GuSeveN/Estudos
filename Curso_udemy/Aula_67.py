'''Calculadora com While'''

while True:
    print('**** Calculadora ****')
    numero = float (input ('Digite um numero: ').strip())
    numero2 = float (input ('Digite outro numero: ').strip())
    mat = str (input ('Digite um operador \n + = Soma \n - = Subtracao \n x = Mutiplicacao \n / = Divicao \n').strip())
    if mat =='+':
        print(f'A soma é {numero+numero2}')
    elif mat =='-':
        print(f'A subtracão é {numero-numero2}')
    elif mat =='x':
        print(f'Mutiplicacão é {numero*numero2}')
    elif mat =='/':
        print(f'Divisão é {numero/numero2}')
    else:
        print('Não selecionou corretamente')
        continue

    print("1 para SAIR")
    if int(input()) == 1:
        break

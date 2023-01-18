# projeto 4
print('='*9, 'Analise de emprestimo', '='*9)  # entrada
while True:  # usando para criar um loop no programa
    # recebendo o valor para salvar no sistema
    salario = float(input('Digite aqui o seu salário:').strip())
    # recebendo o valor para salvar no sistema
    emprestimo = float(input('Digite o valor do seu emprestimo:').strip())
    # recebendo o valor para salvar no sistema
    parcela = float(input('Quantas parcelas que gostaria de pagar ?').strip())
    # calculando juros do emprestimo
    juros = ((emprestimo*0.07)*parcela+emprestimo)/parcela
    juros2 = juros*parcela
    if (juros2 <= salario * 0.3):  # se 30% do salario for maior ou igual ao emprestimo
        print('O emprestimo está aprovado!')
        print('Valor da parcela ficou R$: {:.2f}, no total de R$: {:.2f}'.format(
            juros, juros2))
        break
    elif (juros2 <= salario * 0.5):  # se 50% do salario for maior ou igual ao emprestimo
        print('O emprestimo está em analise!')
        print('Valor da parcela ficou R$: {:.2f}, no total de R$: {:.2f}'.format(
            juros, juros2))
        break
    else:  # se 51% ou + do salario for maior ou igual ao emprestimo
        print('O emprestimo não está aprovado.')
        # sugerindo um novo analise se for SIM vai voltar ao comeco se nao encerra o programa
        t = input(str('Quer fazer outra analise ?').strip())
        if t.upper() == 'NAO':
            print('Encerrando...')
            break

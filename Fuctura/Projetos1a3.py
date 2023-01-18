# Projeto 1 á 3 comentando linha a linha
# ENTRADA
print('='*9, 'Cupom de Desconto', '='*8)
print('Valor do curso é R$: 1500,00')
while True:  # USANDO O WHILE PARA TER UM LOOP SE DIGITAR CUPOM INVALIDO
    cupom = str(input('Digite o cupom: ').strip())  # RECEBENDO A INFORMACAO
    if (cupom == 'FUCTURA1'):  # SE INFORMACAO RECEBIDA FOR IGUAL FUCTURA1
        # INFORMANDO VALOR X DE DESCONTO
        print('Vc acabou de ganhar 15% de desconto')
        print('Seu curso saiu á R$:{:.2f} um deconto total de R$:{:.2f}'.format(
            1500 - (1500*0.15), 1500*0.15))  # INFORMANDO QUANTO GANHOU DE DESCONTO E QUAL FOI O VALOR DO DESCONTO
        break
    elif (cupom == 'FUCTURA2'):  # SE INFORMACAO RECEBIDA FOR IGUAL FUCTURA1
        # INFORMANDO VALOR X DE DESCONTO
        print('vc acabou de ganhar 10% de desconto')
        print('Seu curso saiu á R$:{:.2f} um deconto total de R$:{:.2f}'.format(
            1500 - (1500*0.10), 1500*0.10))  # INFORMANDO QUANTO GANHOU DE DESCONTO E QUAL FOI O VALOR DO DESCONTO
        break
    else:  # se nao ter nenhuma das informacoes anteriores
        print('CUPOM INVALIDO, TENTE NOVAMENTE !!!!!')
        tentativa = str(
            input(('Quer tentar novamente ? digite sim ou nao '))).strip()  # dei uma alternativa se quiser tentar de novo
        if tentativa.upper() == 'NAO':  # se ele receber o nao tanto maiusculo ou minusculo vai parar
            print('Encerrando !!')
            break
        elif tentativa.upper() == 'SIM':  # o programa se dizer sim ele volta para inicio
            print('digite novamente')

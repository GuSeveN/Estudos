import os
carros = [("Chevrolet Tracker", 120),  # listas que vai ser usada em uma funcao
          ("Chevrolet Onix", 90),
          ("Chevrolet Spin", 150),
          ("Hyundai HB20", 85),
          ("Hyundai Tucson", 120),
          ("Fiat Uno", 60),
          ("Fiat Mobi", 70),
          ("Fiat Pulse", 130)]
alugados = []


# funcao q vai ser  impressa com as   listas
def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} / dia.".format(i, car[0], car[1]))


while True:  # repeticao
    os.system('cls')
    print('='*8)
    print("Bem vindo a locadora Fuctura !")
    print("="*8)
    print("O que você deseja fazer ?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int((input()))

    os.system('cls')

    if op == 0:  # se usuario escolher opcao 0
        mostrar_lista_de_carros(carros)  # uso da funcao impressa para usuario
    elif op == 1:  # se nao se usuario escolher opcao 1
        mostrar_lista_de_carros(carros)
        print("="*20)
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quanto dias você deseja alugar ?")
        dias = int(input())
        os.system("cls")
        # vai impremir a chave solicitada na posicao 0 e o dias escolhido
        print("você escolheu {} por {} dias".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(
            dias * carros[cod_car][1]))
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:  # se usuario escolher opcao 0
            print("Parabéns você alugou o {} por {} dias.".format(
                carros[cod_car][0], dias))
            # adicionando a escolha do usuario na lista alugados
            alugados.append(carros.pop(cod_car))
    elif op == 2:  # se nao se usuario escolher opcao 2
        if len(alugados) == 0:  # contando quantas chaves tem na lista citadda
            print("Não há carros para devolver!")
        else:  # se nao
            print("Segue lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver: ")
            cod = int(input())
            if conf == 0:  # se usuario escolher opcao 0
                print("Obrigado por devolver o carro {}.".format(
                    alugados[cod][0]))
                # adicionando novamente na lista carro e apangado na lista alugados !! essa é brabaaaa
                carros.append(alugados.pop(cod))
    print("")
    print("Digite 0 - CONTINUAR | 1 - SAIR")
    if int(input()) == 1:  # encerrar a repeitcao
        break

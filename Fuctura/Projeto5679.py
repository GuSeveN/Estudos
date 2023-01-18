cod_alunoD = {}  # na linha 1 a 4 é a base do lista ou biblioteca que vai receber a informacao
banco_notas = {}
lista_notas = []
banco_medias = {}
while True:  # para ter loop do programa nao fechar sozinho
    print("0 - CADASTRAR ALUNO \n1 - MOSTRAR CADASTROS \n2 - MOSTRAR NOTA \n3 - MOSTRAR SE ALUNO FOI APROVADO")
    # digitar o menu que está na linha 6
    conf = int(input("Digite sua opção: ").strip())
    if (conf == 0):  # Cadastrar aluno
        # receber a informacao cod do aluno
        cod_aluno = input("Digite um código numérico para o aluno: ").strip()
        # receber a informacao do aluno
        nome_aluno = input("Digite o nome do aluno:").strip()
        # receber a informacao da nota da linha 12 á 14
        nota1 = float(input("Digite a primeira nota do aluno:").strip())
        nota2 = float(input("Digite a segunda nota do aluno:").strip())
        nota3 = float(input("Digite a terceira nota do aluno:").strip())
        media = (nota1 + nota2 + nota3) / 3  # media das 3 notas
        # linha 16 a 18 está adicionando as 3 notas em uma lista, só pode adiacionar a lista uma variavel por linha.
        lista_notas.append(nota1)
        lista_notas.append(nota2)
        lista_notas.append(nota3)
        # Dic, adicionando a chave e o valor
        cod_alunoD[cod_aluno] = nome_aluno
        banco_medias[cod_aluno] = media  # Dic, adicionando a chave e o valor
        lista_notas = []  # ZERANDO A LISTA
        print(
            f'O aluno cadastrado foi {nome_aluno} e a suas notas estão no sistema.')  # CONFIRMANDO TODO RECEBIMENTO DA INFORMACAO

    elif (conf == 1):  # Mostrar cadastros
        print("Lista de alunos cadastrados:")
        print("-----------------------------")
        print(cod_alunoD)
    elif (conf == 2):  # Mostrar notas de um aluno
        Cod_Aluno = input("Digite o cod de cadastro do aluno: ").strip()
        # nome do aluno recebendo a dicionario cod_alunoD e vinculando ao nova variavel CoD_aluno
        nome_aluno = cod_alunoD.get(Cod_Aluno)
        # notas recebendo a dicionario notas e vinculando ao nova variavel CoD_aluno
        notas = banco_notas.get(Cod_Aluno)
        # notas recebendo a dicionario media e vinculando ao nova variavel CoD_aluno
        media = banco_medias.get(Cod_Aluno)
        print("As notas do aluno {} são: {}".format(nome_aluno, notas))
        print("E sua média é: {}".format(media))
    elif (conf == 3):  # mostrar a nota final do aluno
        cOd_aluno = input('Digite o cod de cadastro: ').strip()
        # nome do aluno recebendo a dicionario cod_alunoD e vinculando ao nova variavel CoD_aluno
        nome_aluno = cod_alunoD.get(cOd_aluno)
        # notas recebendo a dicionario notas e vinculando ao nova variavel CoD_aluno
        nOtas_aluno = banco_notas.get(cOd_aluno)
        # notas recebendo a dicionario media e vinculando ao nova variavel CoD_aluno
        mEdia = banco_medias.get(cOd_aluno)
        if mEdia >= 7:
            print('Aluno, {} ,APROVADO,sua media foi {}'.format(nome_aluno, mEdia))
        elif mEdia >= 5:
            print(
                'Aluno, {} ,está de RECUPERACAO, sua media foi {}'.format(nome_aluno, mEdia))
        else:
            print('Aluno, {} ,está REPROVADO, sua media foi {}'.format(
                nome_aluno, mEdia))

    print("")
    print("===========")
    print("0 para CONTINUAR | 1 para SAIR")
    if int(input()) == 1:
        break

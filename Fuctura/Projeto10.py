cod_alunoD = {}
banco_notas = {}
lista_notas = []
banco_medias = {}

while True:  # repeticao
    print('='*45)
    print("0 - CADASTRAR ALUNO \n1 - MOSTRAR CADASTROS \n2 - MOSTRAR NOTA \n3 - MOSTRAR SE ALUNO FOI APROVADO")
    print('='*45)
    conf = int(input("Digite sua opção: ").strip())
    if (conf == 0):
        print('='*45)
        cod_aluno = input("Digite um código numérico para o aluno: ").strip()
        print('='*45)
        nome_aluno = input("Digite o nome do aluno:").strip()
        print('='*45)
        for notas in range(1, 4):
            print('='*45)
            notas = float(input(f"Digite a {notas} nota do aluno:").strip())
            print('='*45)
            lista_notas.append(notas)
            media = sum(lista_notas)/3
            cod_alunoD[cod_aluno] = nome_aluno
            banco_medias[cod_aluno] = media
            lista_notas = []
        print(
            f'O aluno cadastrado foi {nome_aluno} e a suas notas estão no sistema.')

    elif (conf == 1):  # Mostrar cadastros
        print('='*45)
        print("Lista de alunos cadastrados:")
        print('='*45)
        print(cod_alunoD)
        print('='*45)
    elif (conf == 2):  # Mostrar notas de um aluno
        cod_aluno = input(
            "Digite um código numérico para o aluno: ").strip()
        notas = banco_notas.get(cod_aluno)
        print('='*45)
        print("As notas do aluno {} são: {}".format(nome_aluno, notas))
        print('='*45)
        print("E sua média é: {:.2f}".format(media))
        print('='*45)
    elif (conf == 3):  # mostrar a nota final do aluno
        cod_aluno = input(
            "Digite um código numérico para o aluno: ").strip()
        media = banco_medias.get(cod_aluno)
        if media >= 7:
            print('='*45)
            print('Aluno, {} ,APROVADO,sua media foi {:.2f}'.format(
                nome_aluno, media))
            print('='*45)
        elif media >= 5:
            print('='*45)
            print('Aluno, {} ,está de RECUPERACAO, sua media foi {:.2f}'.format(
                nome_aluno, media))
            print('='*45)
        else:
            print('='*45)
            print('Aluno, {} ,está REPROVADO, sua media foi {:.2f}'.format(
                nome_aluno, media))
            print('='*45)

    print("")
    print('='*45)
    print("0 para CONTINUAR | 1 para SAIR")
    if int(input()) == 1:
        break

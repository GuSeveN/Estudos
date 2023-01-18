class PessoaFisica():  # Classe pessoa fisica (biblioteca pode ser usada !!!! TOP!!!!)
    def __init__(self, nome, salario):  # Construtor da classe informando atributos
        self.nome = nome  # atributos
        self.salario = salario  # atributos

    def impostoderendaPF(self):  # funcao
        irrf = self.salario * 0.03
        print(f"{self.nome} seu salário é R$ {self.salario} e seu IRRF é R$ {irrf}")


class PessoaJuridica():  # Classe pessoa juridica (biblioteca pode ser usada !!!! TOP!!!!)
    def __init__(self, razaoSocial, faturamento):  # Construtor da classe informando atributos
        self.razaoSocial = razaoSocial  # atributos
        self.faturamento = faturamento  # atributos

    def impostoderendaPJ(self):  # funcao
        irrf = self.faturamento * 0.1
        print(
            f"{self.razaoSocial} seu salário é R$ {self.faturamento} e seu IRRF é R$ {irrf}")


while True:  # repeticao
    print("Escolha a opção 0 - Pessoa Fisica | 1 - Pessoa Juridica:")
    conf = int(input())
    if conf == 0:  # se usuario escolher o 0
        nome = input("Digite seu nome: ")
        salario = float(input("Digite seu salário: "))
        # variavel recebendo funcao com os atributos
        in1 = PessoaFisica(nome, salario)
        in1.impostoderendaPF()
    elif conf == 1:  # se usuario escolher o 1
        razao = input("Digite o razão social da empresa: ")
        faturamento = float(input("Digite o faturamento da empresa: "))
        # variavel recebendo funcao com os atributos
        in2 = PessoaJuridica(razao, faturamento)
        in2.impostoderendaPJ()
    print("")
    print("0 - CONTINUAR | 1 - SAIR")
    if (int(input())) == 1:
        break

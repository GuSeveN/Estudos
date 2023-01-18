

class cadastro ():

    def __int__(self, codproduto, descricao, preco, estoque):
        self.codproduto = codproduto
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    menu_list = ['Cadastro de produto.', 'Preço.',
                 'Estoque.', 'Produtos Cadastrado', 'Pre-Venda.']
    while True:
        print('='*30)
        print('      VENDAS - GuS ELETRO')
        print('='*30)
        for i, menu in enumerate(menu_list):
            print('({}) {}'.format(i, menu))
        print('='*30)
        op = (input('Digite: ').strip())
        if op == '0':
            print('='*6, 'Tela De Cadastro', '='*6)
        print("")
        print("0 para CONTINUAR | 1 para SAIR")
        if op == '0':
            print('='*6, 'Tela De Cadastro', '='*6)
            Cod_cadastro = int((input('Digite para cadastro: ').strip()))
            Descricao = (input('Digite descrição do produto: ').strip())
            Preco = float((input('Digite o preço: ').strip()))
            Estoque = int((input('Digite o estoque: ').strip()))
            codproduto = Cod_cadastro
            descricao = Descricao
            preco = Preco
            estoque = Estoque
            print('Produto cadastrado,cod {}, {},preço: R$ {}, estoque: {} unid'.format(
                Cod_cadastro, Descricao, Preco, Estoque))
        if int(input()) == 1:
            break

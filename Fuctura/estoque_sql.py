import mysql.connector
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='estoque_cliente'
)

cursor = banco.cursor()

menu_list = ['Cadastro de produto.', 'Consulta de Preço.',
             'Consulta de estoque.', 'Produtos Cadastrado', 'Pre-Venda.']
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
        Cod_cadastro = int((input('Digite para cadastro: ').strip()))
        Descricao = (input('Digite descrição do produto: ').strip())
        Preco = float((input('Digite o preço: ').strip()))
        Estoque = int((input('Digite o estoque: ').strip()))
        comando = f'INSERT INTO estoque (cod,descricao,preco,quantidade) VALUES ("{Cod_cadastro}","{Descricao}","{Preco}","{Estoque}")'
        cursor.execute(comando)
        banco.commit()
        print('Cadastro com $UCE$$O !')
    elif op == '1':
        pesquisa = int(input('Digite o codigo do produto: ').strip())
        comando = f'select cod,descricao,preco from estoque WHERE cod = "{pesquisa}"'
        cursor.execute(comando)
        consulta = cursor.fetchall()
        print(consulta)
    elif op == '2':
        pesquisa = int(input('Digite o codigo do produto: ').strip())
        comando = f'select cod,descricao,estoque from estoque where cod ="{pesquisa}"'
        cursor.execute(comando)
        consulta = cursor.fetchall()
        print(consulta)
    elif op == '3':
        comando = 'select * from estoque'
        cursor.execute(comando)
        consulta = cursor.fetchall()
        print(consulta)
    print('1 - sair')
    if input() == '1':
        break

# cursor.close()
# cnx.close()

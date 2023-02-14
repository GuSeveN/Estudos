"""
Iterando strings com while
"""
# nome = str (input ("Digite seu primeiro nome: ").strip ())
# total = nome.join ()
'''nome = 'Gustavo Alvetti'
nome2 = '*'.join(nome)

print(nome2)
'''

nome = 'Gustavo Alvetti'
nome2 = len(nome)
cont = 0
novo_nome = ''

while cont < nome2:
    letra = nome[cont]
    novo_nome += letra+'*'
    cont += 1
print(novo_nome)

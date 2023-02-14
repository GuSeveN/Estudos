"""Qual a letra aparece mais vezes em uma frase """

frase = '''O python é um liguagem de programacão 
multiparadigma
Python foi criado por Guido Van Rossum'''.upper()

cont = 0
frase = frase.split()
frase = ''.join(frase)
cont_frase = ''
cont_atual = 0
while cont < len(frase):
    letra = frase[cont]
    cont_frase = frase.count(letra)
    cont += 1
    if cont_atual < cont_frase:
      cont_atual = cont_frase
      print (f'a letra que mais apareceu foi {letra} a quantidade foi {cont_frase}x')
    #print (letra,cont_frase)
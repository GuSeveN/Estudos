"""Qual a letra aparece mais vezes em uma frase """

texto = '''O python é um liguagem de programacão 
multiparadigma
Python foi criado por Guido Van Rossum'''.upper()

contagem_letras = {}
texto = texto.split()
texto = ''.join(texto)
letra_mais_frequente = ''
quantidade = 0

for letra in texto:
    if letra in contagem_letras:
        contagem_letras[letra] += 1
    else:
        contagem_letras[letra] = 1


for letra, ocorrencias in contagem_letras.items():
    if ocorrencias > quantidade:
        letra_mais_frequente = letra
        quantidade = ocorrencias

print("A letra mais frequente é", letra_mais_frequente,
      "e ela apareceu", quantidade, "vezes.")

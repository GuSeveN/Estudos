d = {'tv': 3500, 'notebook': 3000, 'iphone': 4500}

print(d)

# Obtendo os valores minimos
# usando a funcao zip para inverter o par chave/valor do dicionario
# zip trabalha com par chave/valor (tupla)

min_preco = min(zip(d.values(), d.keys()))

print(min_preco)

#x = np.linspace(0, 2 * np.pi, 100)
#
#plt.plot(x, np.sin(x))
# plt.show()

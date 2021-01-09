from janela_correr_2f_vidro import calcular

largura = int(input('Digite a largura (mm): '))
altura = int(input('Digite a altura (mm): '))
escolha = None

while True:
	print('\nEscolhas uma das opções abaixo:')
	print('1 - Porta de correr 2 folhas')
	print('2 - Janela de correr 2 folhas')
	print('0 - Sair')

	escolha = int(input())
	print()

	if escolha == 0:
		break

	if escolha == 1:
		print(f'Largura da porta {largura}\nAltura da porta {altura}\nMetros quadrados {(largura / 1000) * (altura / 1000)}')
	elif escolha == 2:
		resultado = calcular(largura, altura)
		for chave, valor in resultado.items():
			print(f'- {chave}: {valor}')
		largura = int(input('\nDigite a largura (mm): '))
		altura = int(input('Digite a altura (mm): '))
	else:
		break
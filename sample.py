class Calculo():

	def __init__(self, larg, alt, quant):
		self.largura = larg
		self.altura = alt
		self.quant = quant
		self.su_001 = None
		self.su_002 = None
		self.su_003 = None
		self.material = dict()
		self.arquivo = None
		self.subtotal = None

	def janela_correr_2f(self):
		self.su_001 = self.largura
		self.su_002 = self.largura
		self.su_003 = 2 * self.altura
		self.material = {"Su-001": self.su_001,
								"Su-002": self.su_002,
								"Su-003": self.su_003,}
		return self.material

	def criar_lista(self):
		self.subtotal = self.janela_correr_2f()
						# "a" escrever sem sobreescrever
						# "w" sobreescreve o conteudo
						# "r" somente leitura do arquivo
		try:
			self.arquivo = open("arquivo.txt", "r")
		except FileNotFoundError:
			self.arquivo = open("arquivo.txt", "w")
			for chave, valor in self.subtotal.items():
				self.arquivo.write(f"{str(chave)}: {str(valor)}" + "\n")
		finally:
			self.arquivo.close()

teste = Calculo(1500, 1000, 1)
teste.criar_lista()
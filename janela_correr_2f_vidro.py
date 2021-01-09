

def calcular(largura, altura):
	"""
		Calcula o material necessário para produzir janelas de correr 2 folhas
		retorna uma lista com os materiais necessarios

		LISTA DE PERFIS
		SU-001, SU-002, SU-003, SU-053, SU-039, SU-291, SU-040, SU-041, SU-102
		RM-005, CM-063
	"""

	su_001 = largura
	su_002 = largura
	su_003 = 2 * altura
	su_053 = (largura / 2) * 4
	su_039 = 2 * altura
	su_040 = altura
	su_041 = altura
	su_291 = 2 * altura
	su_102 = ((largura / 2) * 4) + (4 * altura)
	rm_005 = ((largura + 20) + (altura + 20)) * 2
	cm_063 = (largura + altura) * 2

	materiais = dict()
	materiais = {"su_001": su_001,
				"su_002": su_002,
				"su_003": su_003,
				"su_053": su_053,
				"su_039": su_039,
				"su_040": su_040,
				"su_041": su_041,
				"su_291": su_291,
				"su_102": su_102,
				"rm_005": rm_005,
				"cm_063": cm_063}
	return materiais



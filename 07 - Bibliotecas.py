#Exemplo de manipulação de datas
from datetime import date
from datetime import time
from datetime import datetime

def ManipulaDataHora():
	hoje = date.today()
	print("Hoje é: ", hoje) #data completa
	print("(ordenadamente) Hoje é: ", hoje.day, hoje.month, hoje.year ) #data completa
	print("Dia da semana: ", hoje.weekday())
	dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"] #índice
	print("Nome abreviado: ", dias[hoje.weekday()])

	data = datetime.now()
	print("data e hora: ", data)

	tempo = datetime.time(data)
	print("hora atual: ", tempo)
ManipulaDataHora()
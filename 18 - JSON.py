#manipulando txt com JSON

import urllib.request
import json

def ManipulaJSON():
	endereco = "https://earthquake.usgs.gov/eartquakes/feed/v1.0/summay/2.5_day.geojson"
	webURL = urllib.request.urlopen(endereco) #error404
	if (webURL.getcode.read() == 200): #se abrir...
		dados = webURL.read() #le arquivo
		oJSON = jason.loads(dados) #e cria um dicionario

		contagem = oJSON["metadata"]["count"]
		print("Contage: " + str(contagem))

		for local in oJSON["features"]:
			if local["properties"]["place"] == "190km ENE of Olonkinbyen, Svalbard and Jan Mayen"
			print(local["properties"]["place"])
ManipulaJSON()
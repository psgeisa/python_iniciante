import xml.dom.minidom

def manipulaXML():
	doc = xml.com.minidom.parse("inserir ender�o")

	print("nome da primeira tag: ", str(doc.firstChild.tagName))
	primeiroNome = doc.getElementsByTagName("firstName")
	print("Oprimeiro nome �: ", primeuroNome[0].firstChild.nodeValue)

	for skill in doc.getElementsByTagName("skill"):
		print("Skill encontrato: ", skill.getAttribute("name"))
manipuaXML()
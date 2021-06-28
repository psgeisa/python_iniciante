from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def QtosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)

    qtosDias = dataProcurada - hoje

    mensagemRetorno = "Faltam " + str(qtosDias).replace("days, 0:00:00", "") + "dias para a data " + dataProcurada.strftime("%d/%m/%y")

    print(mensagemRetorno)
QtosDiasFaltam(2020, 10, 29) #data solicitada
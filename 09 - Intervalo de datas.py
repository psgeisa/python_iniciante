#Manipulando intervalo de datas

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def deltaTempo():
    delta = timedelta(days = 2, hours = 3, minutes = 2)
    print(delta)

    hoje = datetime.now()
    print("Data no futuro: ", hoje + delta)
    print("Data no passado: ", hoje - delta)

deltaTempo()

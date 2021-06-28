#Formatando data e hora
from datetime import datetime

#usando um conjunto de str
def FormataDataHora():
    hoje = datetime.now()
    print(hoje.strftime("O ano eh: %y")) #ultima década
    print(hoje.strftime("Data e hora local: %c")) #linguagem de máquina completa
    print(hoje.strftime("A hora atual é:  %I:%M:%S %p")) #hora formatada
FormataDataHora()

"""
outros formatos: 

Datas
%y/Y - Ano; %a/%A - Dia da semana; %b/%B - Mês; %d - Dia

Datas locais
%c - Data e hora da localidade; %x - Data da localidade; %X - Hora da localidade

Formatação
%I/%H - 12/24 horas; %M - Minutos; $S - Segundos/ %p - AM or PM

"""


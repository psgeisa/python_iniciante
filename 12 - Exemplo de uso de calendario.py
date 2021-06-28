import calendar

def ImprimeMes():
    #imprime os meses do ano
    for mes in calendar.month_name:
        print(mes)
    #imprime os dias da semana
    for dia in calendar.day_name:
        print(dia)
ImprimeMes()
#Trabalhando com calendarios

import calendar

#calendarios em formato txt
def Calendariotexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2020, 4)
    print(txtCalendario)
Calendariotexto()

#calendarios em formato HTML
def CalendarioHTML():
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHTML.formatmonth(2020, 4)
    print(htmlCalendario)
CalendarioHTML()

"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""

import datetime

dataAtual = datetime.datetime.now()
print(dataAtual)
print(dataAtual.strftime("%Y-%m-%d %H:%M:%S"))
print(dataAtual.strftime("%d/%m/%Y"))
print(dataAtual.strftime("%A, %d de %B de %Y"))
dataEspecifica = datetime.datetime(2020, 5, 17, 15, 30, 45)
print(dataEspecifica)
print(dataEspecifica.strftime("%Y-%m-%d %H:%M:%S"))
print(dataEspecifica.strftime("%d/%m/%Y"))
print(dataEspecifica.strftime("%A, %d de %B de %Y"))
dataString = "2023-08-15 14:45:30"
dataConvertida = datetime.datetime.strptime(dataString, "%Y-%m-%d %H:%M:%S") # Converting string to datetime object
print(dataConvertida)
print(dataConvertida.strftime("%A, %d de %B de %Y"))
print(type(dataConvertida))
print(dataConvertida.year)
print(dataConvertida.month)
print(dataConvertida.day)
print(dataConvertida.hour)
print(dataConvertida.minute)
print(dataConvertida.second)
dataConvertida2 = datetime.datetime.strptime("25/12/2022", "%d/%m/%Y")
print(dataConvertida2)
print(dataConvertida2.strftime("%A, %d de %B de %Y"))
print(type(dataConvertida2))
print(dataConvertida2.year)
print(dataConvertida2.month)
print(dataConvertida2.day)
print(dataConvertida2.hour)
print(dataConvertida2.minute)
print(dataConvertida2.second)
dataHoje = datetime.datetime.now()
dataFutura = datetime.datetime(2027, 1, 1)
diferenca = dataFutura - dataHoje
print(f"Dias até 2027-01-01: {diferenca.days}")
print(f"Segundos até 2027-01-01: {diferenca.total_seconds()}")
print(f"Dias até 2027-01-01 (usando .days): {diferenca.days}")
      
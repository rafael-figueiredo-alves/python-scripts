txt = f"Este é um texto formatado com f-strings em Python. "
print(txt)
name = "Rafael"
age = 41
txt2 = f"Meu nome é {name} e eu tenho {age} anos."
print(txt2)

txt2 = f"Meu nome é {name.upper()} e eu tenho {age + 1} anos no próximo aniversário."
print(txt2)

pi = 3.14159
txt3 = f"O valor de pi com duas casas decimais é {pi:.2f}."
print(txt3)

width = 10
height = 5
area = width * height
txt4 = f"A área de um retângulo com largura {width} e altura {height} é {area}."
print(txt4)

number = 255
txt5 = f"O número {number} em hexadecimal é {number:#04x}."
print(txt5)

value = 0.756
txt6 = f"O valor {value:.2%} como porcentagem."
print(txt6)

from datetime import datetime
now = datetime.now()
txt7 = f"A data e hora atuais são: {now:%d/%m/%Y %H:%M:%S}."
print(txt7)

media = 6.74
txt8 = f"A média do aluno é {media:.1f}."
print(txt8)
txt8 = f"O aluno foi {'aprovado' if media >= 7 else 'reprovado'}." 
print(txt8)

"""
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
"""

texto = "Formatando string com format() para versão anterior a 3.6"
print("{}".format(texto))
name = "Rafael"
age = 41
print("Meu nome é {} e eu tenho {} anos.".format(name, age))
print("Meu nome é {0} e eu tenho {1} anos. {0} é um bom nome.".format(name, age))
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome=name, idade=age))
print("O valor de pi com três casas decimais é {:.3f}.".format(3.14159))

texto2 = "Meu nome é {} e eu tenho {} anos."
print(texto2.format(name, age))
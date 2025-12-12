sample_text = "Python é divertido"
print("Texto original:", sample_text)

print("Funções com strings em Python:")
print("Comprimento da string:", len(sample_text))
print("Contar ocorrências de 'a':", sample_text.count('a'))
print("Encontrar índice da primeira ocorrência de 'é':", sample_text.find('é'))
print("Verificar se a string começa com 'Python':", sample_text.startswith('Python'))
print("Verificar se a string termina com 'divertido':", sample_text.endswith('divertido'))
print("Converter para maiúsculas:", sample_text.upper())
print("Converter para minúsculas:", sample_text.lower())
print("Dividir a string em palavras:", sample_text.split())
print("Juntar palavras com '-':", '-'.join(sample_text.split()))
print("Substituir 'divertido' por 'incrível':", sample_text.replace('divertido', 'incrível'))
print("String invertida usando slicing:", sample_text[::-1])
print("Verificar se todos os caracteres são alfabéticos:", sample_text.isalpha())
print("Verificar se todos os caracteres são dígitos:", sample_text.isdigit())
print("Remover espaços em branco no início e fim: '   Olá, Mundo!   ' -> '", '   Olá, Mundo!   '.strip(), "'")
print("Verificar se a string é um título:", "Python É Divertido".istitle())
print("Converter para título:", sample_text.title())
print("Encontrar índice da última ocorrência de 'i':", sample_text.rfind('i'))
print("Converts string into lower case", sample_text.casefold())
print("Verificar se a string é numérica:", "12345".isnumeric())
print("Verificar se a string é alfanumérica:", "Python3".isalnum())
print("Verificar se a string é decimal:", "10.5".isdecimal())
print("Verificar se a string é um espaço em branco:", "   ".isspace())
print("Encodar string para bytes:", sample_text.encode('utf-8'))
print("Decodar bytes para string:", sample_text.encode('utf-8').decode('utf-8'))
print("Formatar string com f-string:", f"O texto é: {sample_text}")
print("Sets the tab size of the string:", sample_text.expandtabs(4))
print("Verificar se a string é imprimível:", sample_text.isprintable())
print("Verificar se a string é um identificador válido:", "Python_Var1".isidentifier())
print("Contar ocorrências de 'i' entre os índices 0 e 10:", sample_text.count('i', 0, 10))
print("Encontrar índice de 'é' entre os índices 0 e 10:", sample_text.find('é', 0, 10))
print("Verificar se a string começa com 'Py' entre os índices 0 e 6:", sample_text.startswith('Py', 0, 6))
print("Formats specified values in a string:", "O texto é: {}".format(sample_text))
print("Formats specified values from a dictionary in a string:", "O texto é: {text}".format(text=sample_text))
print("Fills the string with a specified number of 0 values at the beginning:", sample_text.zfill(30))
print("Formata NDOC", f"{"NF"}{"1385".zfill(7)}")
print("Adiciona prefixo '>>>' na string:", sample_text.rjust(len(sample_text) + 3, '>'))
print("Adiciona sufixo '<<<' na string:", sample_text.ljust(len(sample_text) + 3, '<'))
print("Verificar se a string é capitalizada:", "Python é Divertido".isupper())
print("Verificar se a string é minúscula:", "python é divertido".islower())
print("Returns a translated string", sample_text.translate(str.maketrans('one', 'uma')))
print("Returns a translation table to be used in translations", str.maketrans('once', 'upon'))
print("Returns a left justified version of the string", sample_text.ljust(255, '*'))
print("Returns a right justified version of the string", sample_text.rjust(255, '*'))
print("Returns a centered version of the string", sample_text.center(150, '*'))
print("Remover caracteres específicos do início e fim: '---Olá, Mundo!---' -> '", '---Olá, Mundo!---'.strip('-'), "'")
print("Remover caracteres específicos do início: '---Olá, Mundo!---' -> '", '---Olá, Mundo!---'.lstrip('-'), "'")
print("Remover caracteres específicos do fim: '---Olá, Mundo!---' -> '", '---Olá, Mundo!---'.rstrip('-'), "'")
print("Returns a tuple where the string is parted into three parts", sample_text.partition('é'))
print("Returns a tuple where the string is parted into three parts from the right", sample_text.rpartition('é'))
print("Formatar valor numérico em string:", "O valor é: {:.2f}".format(123.4567))
print("Verificar se a string é um número de ponto flutuante:", "123.45".replace('.', '', 1).isdigit())
print("Verificar se a string é um número complexo:", "1+2j".replace('j', '').replace('+', '').replace('-', '').isdigit())
print("Convertendo a string para bytes e de volta para string:", sample_text.encode().decode())
print("Verificar se a string é um número hexadecimal:", "1A3F".isxdigit() if hasattr(str, 'isxdigit') else "isxdigit não disponível")
print("Verificar se a string é um número octal:", "123".isodigit() if hasattr(str, 'isodigit') else "isodigit não disponível")
print("Verificar se a string é um número binário:", "1010".isbdigit() if hasattr(str, 'isbdigit') else "isbdigit não disponível")
print("Funções concluídas.")

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""

"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

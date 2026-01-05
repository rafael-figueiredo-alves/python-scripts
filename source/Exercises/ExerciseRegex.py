# Usando módulo nativo re para trabalhar com expressões regulares em Python

import re

def encontrar_palavras_com_prefixo(texto, prefixo):
    """
    Encontra todas as palavras em um texto que começam com um determinado prefixo.

    :param texto: O texto onde procurar as palavras.
    :param prefixo: O prefixo que as palavras devem começar.
    :return: Uma lista de palavras que começam com o prefixo.
    """
    padrao = r'\b' + re.escape(prefixo) + r'\w*' # Padrão regex para palavras com o prefixo
    return re.findall(padrao, texto) # Retorna todas as correspondências encontradas

def substituir_palavras(texto, palavra_antiga, palavra_nova):
    """
    Substitui todas as ocorrências de uma palavra por outra em um texto.

    :param texto: O texto onde substituir as palavras.
    :param palavra_antiga: A palavra a ser substituída.
    :param palavra_nova: A palavra que substituirá a antiga.
    :return: O texto com as palavras substituídas.
    """
    padrao = re.escape(palavra_antiga) # Padrão regex para a palavra antiga
    return re.sub(padrao, palavra_nova, texto) # Substitui todas as ocorrências

def validar_email(email):
    """
    Valida se um endereço de email está no formato correto.

    :param email: O endereço de email a ser validado.
    :return: True se o email for válido, False caso contrário.
    """
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None # Retorna True se o email corresponder ao padrão

# Exemplo de uso das funções
if __name__ == "__main__":
    texto_exemplo = "O rato roeu a roupa do rei de Roma."
    prefixo = "ro"
    print("Palavras com prefixo '{}': {}".format(prefixo, encontrar_palavras_com_prefixo(texto_exemplo, prefixo)))

    texto_substituir = "O gato está no telhado. O gato é preto."
    palavra_antiga = "gato"
    palavra_nova = "cachorro"
    print("Texto após substituição: {}".format(substituir_palavras(texto_substituir, palavra_antiga, palavra_nova)))

    email_teste = "rafael.alve@gmail.com"
    print("Email '{}' é válido? {}".format(email_teste, validar_email(email_teste)))

"""
Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""

"""
Metacharacters
Metacharacters are characters with a special meaning:

Character	Description	Example
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
"""

"""
Flags
You can add flags to the pattern when using regular expressions.

Flag	Shorthand	Description	Try it
re.ASCII	re.A	Returns only ASCII matches	
re.DEBUG		Returns debug information	
re.DOTALL	re.S	Makes the . character match all characters (including newline character)	
re.IGNORECASE	re.I	Case-insensitive matching	
re.MULTILINE	re.M	Returns only matches at the beginning of each line	
re.NOFLAG		Specifies that no flag is set for this pattern	
re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable	
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	Example	Try it
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	Description	Try it
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

teste = "Teste de metacaracteres: gato, gato123, gato_preto, gato-preto."
print(encontrar_palavras_com_prefixo(teste, "gato"))  # ['gato', 'gato123', 'gato_preto', 'gato']

print(re.split(r'\s', 'Palavras separadas por espaços'))  # ['Palavras', 'separadas', 'por', 'espaços']

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())  # (12, 17)
print(x.string)  # The rain in Spain
print(x.group())  # Spain
print(x.start())  # 12
print(x.end())    # 17
print(x.re)      # re.compile('\\bS\\w+')


numero1 = 10
numero2 = 20

if numero1 > numero2:
    print("Número 1 é maior que Número 2")

if numero1 < numero2:
    print("Número 1 é menor que Número 2")

if 10 > 4:
    print("10 é maior que 4")
    print("Isso é verdade")
    print("Fim do bloco if")

is_logged_in = True
if is_logged_in:
    print("Usuário está logado")

if numero1 != numero2:
    print("Número 1 é diferente de Número 2")
elif numero1 == numero2:
    print("Número 1 é igual a Número 2")

if numero1 > numero2:
    print("Número 1 é maior que Número 2")
else:
    print("Número 1 não é maior que Número 2")

print("Teste de shorhand if") if numero1 < numero2 else print("Número 1 é menor que Número 2")

print("Numero 1 é maior que Número 2") if numero1 > numero2 else print("Número 1 é igual a Número 2") if numero1 == numero2 else print("Número 1 é menor que Número 2")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

"""
Why Use pass?
The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
"""

temperature = 35

if temperature > 30:
    pass  # Placeholder for future code when temperature exceeds 30

def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet
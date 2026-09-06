import re

print("===== MANIPULAÇÃO DE STRINGS =====")

# Variável
nome = "JUVENALDO FLORENTINO"

# lower
print("\nLower:")
print(nome.lower())

# upper
print("\nUpper:")
print(nome.upper())

# capitalize
print("\nCapitalize:")
print(nome.capitalize())

# title
print("\nTitle:")
print(nome.title())

# swapcase
print("\nSwapcase:")
print(nome.swapcase())


# len
print("\nTamanho da string:")
print(len(nome))


# Indexação
alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("\nPrimeira letra:")
print(alfabeto[0])


# Concatenação
letras = "ABDE"

print("\nConcatenação:")
print(letras + "FGH")


# Repetição
print("\nRepetição:")
print(letras + "F" * 5)


# Linha
print("\nLinha:")
print("X" + "-" * 10 + "X")


# Fatiamento
cidade = "Fortaleza"

fateada = cidade[0:3]

print("\nFatiamento:")
print(fateada)


# Strip
texto = "    Python    "

print("\nStrip:")
print(texto.strip())


# Replace
frase = "Eu gosto de Java"

print("\nReplace:")
print(frase.replace("Java", "Python"))


# Split e Join
nome_com_espacos = "Ju ve n a l d o Flo ren tin o"

nome_sem_espacos = "".join(nome_com_espacos.split())

print("\nNome sem espaços:")
print(nome_sem_espacos)


# Regex
nome_regex = "JuvenaldoFlorentino"

partes = re.findall('[A-Z][a-z]*', nome_regex)

nome_corrigido = " ".join(partes)

print("\nNome corrigido com Regex:")
print(nome_corrigido)
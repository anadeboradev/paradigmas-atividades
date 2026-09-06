print("===== CADASTRO DE PERFIL =====")

nome = input("Digite seu nome completo: ")

# Validar idade
while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade >= 0:
            break
        else:
            print("Erro! A idade não pode ser negativa.")

    except ValueError:
        print("Erro! Digite um número inteiro válido.")

# Validar altura
while True:
    try:
        altura = float(
            input("Digite sua altura em metros: ").replace(",", ".")
        )

        if altura > 0:
            break
        else:
            print("Erro! A altura deve ser maior que zero.")

    except ValueError:
        print("Erro! Digite uma altura válida.")

cidade = input("Digite a cidade onde você mora: ")

# Exibição
print("\n==============================")
print("   CARTÃO DE IDENTIFICAÇÃO")
print("==============================")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
print(f"Cidade: {cidade}")
print("==============================")
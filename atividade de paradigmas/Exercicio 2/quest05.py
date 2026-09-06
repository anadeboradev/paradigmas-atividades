print("===== CLASSIFICAÇÃO ETÁRIA =====")

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade >= 0:
            break
        else:
            print("Erro! A idade não pode ser negativa.")

    except ValueError:
        print("Erro! Digite uma idade válida.")

if idade <= 12:
    classificacao = "Criança"

elif idade <= 17:
    classificacao = "Adolescente"

elif idade <= 59:
    classificacao = "Adulto"

else:
    classificacao = "Idoso"

print(f"\nA pessoa é classificada como: {classificacao}")
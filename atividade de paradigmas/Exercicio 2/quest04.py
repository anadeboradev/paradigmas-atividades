print("===== MÉDIA ESCOLAR =====")

notas = []

for i in range(1, 4):

    while True:
        try:
            nota = float(
                input(f"Digite a nota {i}: ").replace(",", ".")
            )

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Erro! A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Erro! Digite uma nota válida.")

media = sum(notas) / len(notas)

if media >= 7:
    situacao = "APROVADO"
elif media >= 5:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "REPROVADO"

print("\n===== RESULTADO =====")

print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
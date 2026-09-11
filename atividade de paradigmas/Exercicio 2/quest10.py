print("===== Temperaturas da semana =====")

temperaturas = []

for dia in range(1, 8):
    temperatura = float(
        input(f"Digite a temperatura do dia {dia}: ").replace(",", ".")
    )

    temperaturas.append(temperatura)

maior = max(temperatura)
menor = min(temperatura)
media = sum(temperatura) / len(temperatura)

acima_media = 0

for temperatura in temperaturas: 
    if temperatura > media:
        acima_media += 1

print("\n ===== Relatório =====")
print(f"Temperatuas: {temperaturas}")
print(f"Maior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
print(f"Média: {media:.2f}")
print(f"Dias acima da média: {acima_media}")
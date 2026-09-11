print("===== Análise de lista =====")

numeros = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}° número: "))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print("\n ===== Relatório =====")
print(f"Números informados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")
print("===== Ordenação de 3 números =====")

while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        n3 = int(input("Digite o terceiro número: "))

        if n1 != n2 and n1 != n3 and n2 != n3:
            break
        else:
            print("Erro! Os númeors devem ser diferentes.")
    
    except ValueError:
        print("Erro! Digite apenas números inteiros.")

if n1 > n2:
    if n1 > n3:
        maior = n1

        if n2 > n3:
            meio = n2
            menor = n3
        else:
            meio = n3
            menor = n2
    else:
        maior = n3
        meio = n1
        menor = n2

else:
    if n2 > n3:
        maior = n2

        if n1 > n3:
            meio = n1
            menor = n3
        else:
            meio = n3
            menor = n1
    else:
        maior = n3
        meio = n2
        menor = n1

print("\n ===== Resultado =====")
print(f"Maior número: {maior}")
print(f"Número intermediário: {meio}")
print(f"Menor número: {menor}")
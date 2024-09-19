def converter():
    print("Escolha a conversão desejada:")
    print("1. Centímetros para Polegadas")
    print("2. Polegadas para Centímetros")
    print("3. Quilômetros para Milhas")
    print("4. Milhas para Quilômetros")

    escolha = int(input("Digite o número da conversão desejada (1/2/3/4): "))

    if escolha == 1:
        cm = float(input("Digite o valor em centímetros: "))
        polegadas = cm * 0.3937
        print(f"{cm} centímetros é igual a {polegadas} polegadas.")
    elif escolha == 2:
        polegadas = float(input("Digite o valor em polegadas: "))
        cm = polegadas * 2.54
        print(f"{polegadas} polegadas é igual a {cm} centímetros.")
    elif escolha == 3:
        km = float(input("Digite o valor em quilômetros: "))
        milhas = km * 0.6214
        print(f"{km} quilômetros é igual a {milhas} milhas.")
    elif escolha == 4:
        milhas = float(input("Digite o valor em milhas: "))
        km = milhas * 1.6093
        print(f"{milhas} milhas é igual a {km} quilômetros.")
    else:
        print("Escolha inválida. Por favor, selecione uma opção válida.")


# Chamar a função de conversão
converter()

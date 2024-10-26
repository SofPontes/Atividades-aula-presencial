def maior_de_tres():
    # Solicita tres números ao usuário
    num1 = int(input("Digite o primeiro numero"))
    num2 = int(input("Digite o segundo numero"))
    num3 = int(input("Digite o terceiro numero"))

    # Usa a funçaõ max() para encontrar o maior numero 
    maior = max (num1, num2, num3)

    print(f"O maior numero é: {maior} ")
    
maior_de_tres()

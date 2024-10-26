def calculo_media():
    nota1 = float(input("Insira a primeira nota"))
    nota2 = float(input("Insira a segunda nota"))
    nota3 = float(input("Insira a terceira nota"))

    media = (nota1+ nota2+ nota3) / 3
    print(f"A média é: {media: .2f}")
    if media >=7:
        print("Aprovado")
    else:
        print("Reprovado")

 #chamar função
calculo_media() 
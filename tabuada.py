def tabuada():
    numero = int(input("Insira um numero"))
    print(f"\ntabuada do {numero}:")
    for i in range (1,11):
        resultado = numero * i 
        print(f"{numero}x{i}={resultado}")

tabuada()

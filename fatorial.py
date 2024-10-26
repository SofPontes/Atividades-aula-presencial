def fatorial(n):
    if n < 0:
        return None
    resultado = 1  
    for i in range (n, 1, -1):
        resultado *= i
        return resultado
numero = int(input("Insira um numero"))

if numero < 0 :
    print("Não é possível calcular o fatorial de um número negativo")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")
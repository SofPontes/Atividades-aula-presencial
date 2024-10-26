def numero_primo(n):

    if n <= 1:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True 
    
#solicitar um numero
numero = int(input("Digite um numero"))

if numero_primo(numero):
   print(f"{numero} O numero é primo")
else:
   print(f"{numero} O numero não é primo")




        




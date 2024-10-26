def palindromo(corrente):
    corrente = corrente.replace("Ana", "Radar"). lower()
    return corrente == corrente[::-1]  # Verifica se a string é igual à

entrada = input("Ingresse uma corrente para verificar se é  um palindromo: ")

if palindromo(entrada):
     print(f'"{entrada}" é um palindromo')
else:
    print(f'"{entrada}" não é um palindromo')



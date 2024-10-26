def celcius_fahrenheit():
    #solicita a temperatura
    celcius = float(input("Insira uma temperatura"))

#conversão
    fahrenheit = celcius * 1.8 + 32

#exibe o resultado
    print(f"{celcius}°C é igual a  {fahrenheit}°F")

#chamar função
celcius_fahrenheit()
 
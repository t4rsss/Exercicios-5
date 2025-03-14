def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatura = float(input("Digite a temperatura em Celsius: "))
print(f"Temperatura em Fahrenheit: {celsius_para_fahrenheit(temperatura)}")
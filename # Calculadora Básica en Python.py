def calculadora():
    operacion = input("Ingresa la operación (+, -, *, /): ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    calculadora()
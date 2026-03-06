def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro: não é possível dividir por zero.")
        return None
    return a / b


while True:
    print("\n--- Calculadora ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Até mais!")
        break

    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(a, b))
    elif opcao == "2":
        print("Resultado:", subtrair(a, b))
    elif opcao == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcao == "4":
        resultado = dividir(a, b)
        if resultado is not None:
            print("Resultado:", resultado)
    else:
        print("Opção inválida.")

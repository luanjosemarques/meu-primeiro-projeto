def calcular():
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando...")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = num1 + num2
            elif opcao == "2":
                resultado = num1 - num2
            elif opcao == "3":
                resultado = num1 * num2
            elif opcao == "4":
                if num2 == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado = num1 / num2
            else:
                print("Opção inválida!")
                continue

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Erro: digite apenas números válidos!")

if __name__ == "__main__":
    calcular()
    git add Main.py
    git commit -m "Implementação da calculadora"    
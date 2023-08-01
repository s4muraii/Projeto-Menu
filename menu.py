import os

x = 1
z = 1
while x == 1:
    print("Bem vindo ao software de operações!") # Introdução ao software
    a = input("Escolha a opção desejada: \n 1 - Número primo \n 2 - Número decrescente \n 3 - Mediana de 3 números \n 4 - Sair \n ") # Seleção de operação
    z = 1
    b = "inalterado"
    while z == 1:
        if a == "1":

            os.system ("cls")

            print("Número primo selecionado \n") # Operação de adição
            lógica = input("[1] Prosseguir para a lógica \n[2] Refazer \n[3] Voltar \n[4] Sair \n") # Seleção de menu dentro da sessão de operação
            if lógica == "1":
                b = int(input("Digite o valor desejado \n")) # Valor a ser inserido ao cliente
                if (b % 3 > 0 and b % 5 > 0 and b % 7 > 0 and b % 2 > 0 and b > 2): # Operação que será realizada pelo software
                    print ("O número é primo.")
                else:
                    print("O número não é primo.")
                c =input("Deseja retornar ao menu da operação? Se desejar retornar ao início, digite n \n s - Sim \n n - Não \n")
                if c == "s":

                    os.system ("cls")

                    lógica = "1"

                else:

                    os.system ("cls")
                    b = "inalterado"
                    z = "1"
            elif lógica == "2":
                if b == "inalterado":
                    print("Não é possível refazer")

                    os.system ("pause")

                elif b != "inalterado":

                    os.system ("cls")

                    lógica = "1"

            elif lógica == "3":

                os.system("cls")

                z = 2
            elif lógica == "4":

                os.system ("cls")

                print("Finalizando sistema")
                z = 2
                x = 2

        if a == "2":

            os.system ("cls")

            print("Número decrescente selecionado")
            lógica = input("[1] Prosseguir para a lógica \n[2] Refazer \n[3] Voltar \n[4] Sair \n")
            if lógica == "1":
                d = int(input("insira o valor desejado: "))
                while d >= 0:
                    print (d)
                    d -= 1
                if d == 0:
                    print ("Contagem finalizada")
                c =input("Deseja retornar ao menu da operação? Se desejar retornar ao início, digite n \n s - Sim \n n - Não \n")
                if c == "s":

                    os.system ("cls")

                    a = "2"
                    lógica = "1"
                else:

                    os.system ("cls")

                    z = 2
            elif lógica == "2":
                if b == "inalterado":
                    print("Não é possível refazer")

                    os.system ("pause")

                elif b != "inalterado":

                    os.system ("cls")

                    lógica = "2"

            elif lógica == "3":

                os.system("cls")

                b = "inalterado"
                z = 2
            if lógica == "4":

                os.system ("cls")

                print("Finalizando sistema")
                z = 2
                x = 2

        if a == "3":
            os.system ("cls")

            print("Mediana de três números selecionada")
            lógica = input("[1] Prosseguir para a lógica \n[2] Refazer \n[3] Voltar \n[4] Sair \n")
            if lógica == "1":
                b = int(input("Digite o primeiro valor: "))
                c = int(input("Digite o segundo valor: "))
                d = int(input("Digite o terceiro valor: "))
                números = [b,c,d]
                números.sort()
                print(números[1])
                c =input("Deseja retornar ao menu da operação? Se desejar retornar ao início, digite n \n s - Sim \n n - Não \n")
                if c == "s":

                    os.system ("cls")

                    a = "3"
                    lógica = "1"
                else:

                    os.system ("cls")

                    z = 2
            elif lógica == "2":
                if b == "inalterado":
                    print("Não é possível refazer")

                    os.system ("pause")

                elif b != "inalterado":

                    os.system ("cls")

                    lógica = "3"

            elif lógica == "3":
                os.system("cls")

                b = "inalterado"
                z = 2
            if lógica == "4":

                os.system ("cls")

                print("Finalizando sistema...")

                z = 2
                x = 2

        if a == "4":

            os.system("cls")

            print("Finalizando sistema")
            z = 2
            x = 2

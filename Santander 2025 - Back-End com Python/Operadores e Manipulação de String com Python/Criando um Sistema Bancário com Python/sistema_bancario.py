menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção que deseja => """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("$--$--Depositar--$--$")
        while True:
            deposito = int(input("Digite o valor a ser depositado: R$"))
            if(deposito <= 0):
                print("!Digite um valor maior ou igual a 1!")
                continue
            elif(deposito > 0):
                saldo += deposito
                print(f"O valor: R${deposito:.2f} foi depositado na conta com sucesso")
                break
            else:
                print("Erro no sistema, tente novamente!")
                continue


    elif opcao == "s":
        print("$--$--Sacar--$--$")
        while True:
            saque = int(input("Digite o valor a ser sacado: R$"))

            if(saque > limite or saque > saldo):
                if(saque > limite):
                    print(f"Saque maior que o limite de R${limite:.2f}, tente realizar um valor menor.")
                else:
                    print(f"Saque maior que o saldo atual de R${saldo:.2f}, Tente novamente, ou digite '0' para sair!")
                continue
                
            elif (saque >= 0 and LIMITE_SAQUES > 0): 
                saldo -= saque
                LIMITE_SAQUES -= 1
                print(f"Saque realizado com sucesso no valor de R${saque:.2f}")
                break

            else:
                print("Valor invalido ou limite diario de saques atingido.")
                break
                
        
    elif opcao == "e":
        print(f"Seu saldo é de: R${saldo}")
        print(f"Restão {LIMITE_SAQUES} saques restantes hoje.")

    elif opcao == "q":
        print("Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    

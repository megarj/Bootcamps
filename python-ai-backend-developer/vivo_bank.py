menu = """
                                           ##     
                                          ####   
            ##                            ####    
                                           ##     
 ##     ##  ##   ##    ##    ####      ########### 
  ##   ##   ##   ##    ##  ##    ##        ###    
   ## ##    ##    ##  ##   ##    ##        ###    
    ###     ##     ####    ##    ##       ## ##   
     #      ##      ##       ####        ##   ##  
                                                  
  ###                        
   ##                         
   ##       ####    #####     ##  ## 
   #####       ##   ##  ##    ## ## 
   ##  ##   #####   ##  ##    #### 
   ##  ##  ##  ##   ##  ##    ## ## 
  ######    #####   ##  ##    ##  ## 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

layout_extrato = """
================ EXTRATO ================
{movimentos}
Saldo: R$ {saldo:.2f}
Número de saques realizados hoje: {num_saques}
==========================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("Não foram realizadas movimentações." if not extrato else layout_extrato.format(movimentos=extrato, saldo=saldo, num_saques=numero_saques))

    elif opcao == "q":
        print("Obrigado por usar nosso sistema! Tenha um ótimo dia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
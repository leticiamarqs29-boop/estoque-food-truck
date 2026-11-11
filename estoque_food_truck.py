# Estoque do Food Truck
estoque_pao = 100
estoque_salsicha = 120
estoque_batata_palha = 30

# LIMITE MÍNIMO DE SEGURANÇA
MINIMO_PAO = 20
MINIMO_SALSICHA = 30
MINIMO_BATATA_PALHA = 5

while True: 
    print("=======================================")
    print(" GESTÃO DE ESTOQUE - HOT DOG ")
    print("=======================================")
    print("1. Visualizar Estoque e Alertas")
    print("2. Atualizar Estoque (Entrada de Produtos)")
    print("3. Registrar Venda (Dar Baixa automática)")
    print("4. Sair do Programa")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    if opcao == "1":
        print("=== ESTOQUE ATUAL ===")
        if estoque_pao <= MINIMO_PAO:
            print("Pão de Hot Dog: " + str(estoque_pao) + " unidades -> BAIXO ESTOQUE.")
        else:
            print("Pão de Hot Dog: " + str(estoque_pao) + " unidades -> OK")
            
        if estoque_salsicha <= MINIMO_SALSICHA:
            print("Salsicha: " + str(estoque_salsicha) + " unidades -> BAIXO ESTOQUE.")
        else:
            print("Salsicha: " + str(estoque_salsicha) + " unidades -> OK")
            
        if estoque_batata_palha <= MINIMO_BATATA_PALHA:
            print("Batata Palha: " + str(estoque_batata) + " pacotes -> BAIXO ESTOQUE.")
        else:
            print("Batata Palha: " + str(estoque_batata_palha) + " pacotes -> OK")

    elif opcao == "2":
        print("Qual produto deseja abastecer?")
        print("1. Pão de Hot Dog")
        print("2. Salsicha")
        print("3. Batata Palha")
        item = input("Escolha o produto (1-3): ")
        
        if item == "1":
            quantidade = int(input("Quantos pães entrou no estoque? "))
            estoque_pao = estoque_pao + quantidade
            print("Estoque de pães atualizado")
        elif item == "2":
            quantidade = int(input("Quantas salsichas entrou no estoque? "))
            estoque_salsicha = estoque_salsicha + quantidade
            print("Estoque de salsichas atualizado")
        elif item == "3":
            quantidade = int(input("Quantos pacotes de batata entrou no estoque? "))
            estoque_batata_palha = estoque_batata_palha + quantidade
            print("Estoque de batatas palha atualizado")
        else:
            print("Opção de produto inválida.")

    elif opcao == "3":
        print("--- REGISTRAR VENDA ---")
        print("1. Hot Dog Simples (Consome: 1 Pão, 1 Salsicha)")
        print("2. Hot Dog Especial (Consome: 1 Pão, 1 Salsicha, 1 Batata Palha)")
        lanche = input("Escolha o lanche vendido: ")
        
        if lanche == "1":
            if estoque_pao >= 1 and estoque_salsicha >= 1:
                estoque_pao = estoque_pao - 1
                estoque_salsicha = estoque_salsicha - 1
                print("Venda realizada! 1 Pão e 1 Salsicha retirados do estoque.")
            else:
                print("Insumos insuficientes!")
        elif lanche == "2":
            if estoque_pao >= 1 and estoque_salsicha >= 1 and estoque_batata_palha >= 1:
                estoque_pao = estoque_pao - 1
                estoque_salsicha = estoque_salsicha - 1
                estoque_batata_palha = estoque_batata_palha - 1
                print("Venda realizada! Estoque atualizado.")
            else:
                print("Insumos insuficientes!")
        else:
            print("Opção de lanche inválida.")

    elif opcao == "4":
        print("Encerrando o sistema do Food Truck.")
        break
        
    else:
        print("Opção inválida! Digite um número de 1 a 4.")

estoque_produto = {
    1 : {"Nome": "Tenis Nike", "preco": 400.00,"Quantidade": 2 },
    2 : {"Nome":"Tenis Adidas", "preco": 700.00,"Quantidade": 100},
    3 : {"Nome": "Camisa CazeTV", "preco": 80.00,"Quantidade": 8 },
    4 : {"Nome": "Camisa Flamengo", "preco": 150.00,"Quantidade": 1 },
    5 : {"Nome": "Energetico", "preco": 14.00,"Quantidade": 6 },
}
carrinho = []

while True:
    print ("*" * 30)
    print ("SISTEMA VENDA-SEJA BEM VINDO")
    print ("*" * 30)
    print ("[1] Visualizar Estoque.")
    print ("[2] Adicionar item ao carrinho.")
    print ("[3] Visualizar Carrinhos.")
    print ("[4] Finalizar Compra.")
    print ("[0] Sair do sistema.")

    opcao = int(input("Escolha uma Opcao: "))
    if opcao == 1:
        print("Visualizar Estoque!")
        print("ID | Nome | VALOR | Quantidade")
        for c,v in estoque_produto.items():
            print(f"{c} | {v['Nome']} | {v['preco']} | {v['Quantidade']}")
    elif opcao == 2:
        print("Adicionar item ao carrinho!")
        id_produto = int(input("Qual id do produto deseja compra? "))
        if id_produto in estoque_produto:
            qtd_produto = int(input("Qual quantidade do produto deseja compra? "))
            if qtd_produto <= 0:
                print("Quantidade Invalida!")
            elif qtd_produto <= estoque_produto[id_produto]['Quantidade']:
                item = {
                    "Qtd" : qtd_produto,
                    "Nome" : estoque_produto[id_produto]['Nome'],
                    "preco" : estoque_produto[id_produto]['preco'],
                    "Valor_total": qtd_produto * estoque_produto[id_produto]['preco'],
                }
                carrinho.append(item)
                estoque_produto[id_produto]['Quantidade'] -= qtd_produto
            else :
                print(f"Quantidade Indisponivel, temos apenas {estoque_produto[id_produto]['Quantidade']} no estoque.")
        else :
                print("ID informado nao existe no estoque."
              )
    elif opcao == 3:
        if carrinho:
            print("Visualizar Carrinhos!")
            subtotal = 0
            for i in carrinho:
                print(f"{i["Qtd"]}x {i['Nome']} no valor de R$ {i['preco']}(cada)\nTotal R$ {i['Valor_total']}")
                subtotal += i['Valor_total']
            print (f"Total R$ {subtotal}")
        else :
            print("Carrinho vazio")
    elif opcao == 4:
        print("Finalizar Compra!")

    elif opcao == 0:
        print("Sair do sistema.")
        break
    else :
        print("Opcao invalida!")
        break





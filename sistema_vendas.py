estoque_produto = {
    1: {"Nome": "Tenis Nike", "preco": 400.00, "Quantidade": 2},
    2: {"Nome": "Tenis Adidas", "preco": 700.00, "Quantidade": 100},
    3: {"Nome": "Camisa CazeTV", "preco": 80.00, "Quantidade": 8},
    4: {"Nome": "Camisa Flamengo", "preco": 150.00, "Quantidade": 1},
    5: {"Nome": "Energetico", "preco": 14.00, "Quantidade": 6},
}
carrinho = []
subtotal = 0

while True:
    print("*" * 30)
    print("SISTEMA VENDA-SEJA BEM VINDO")
    print("*" * 30)
    print("[1] Visualizar Estoque.")
    print("[2] Adicionar item ao carrinho.")
    print("[3] Visualizar Carrinhos.")
    print("[4] Finalizar Compra.")
    print("[0] Sair do sistema.")

    opcao = int(input("Escolha uma Opcao: "))
    if opcao == 1:
        print("Visualizar Estoque!")
        print("ID | Nome | VALOR | Quantidade")
        for c, v in estoque_produto.items():
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
                    "id": id_produto,
                    "Qtd": qtd_produto,
                    "Nome": estoque_produto[id_produto]['Nome'],
                    "preco": estoque_produto[id_produto]['preco'],
                    "Valor_total": qtd_produto * estoque_produto[id_produto]['preco'],
                }
                carrinho.append(item)
                estoque_produto[id_produto]['Quantidade'] -= qtd_produto
                print(f"{qtd_produto}x {item['Nome']} adicionado ao carrinho!")
            else:
                print(f"Quantidade Indisponivel, temos apenas {estoque_produto[id_produto]['Quantidade']} no estoque.")
        else:
            print("ID informado nao existe no estoque.")

    elif opcao == 3:
        if carrinho:
            print("\n=== Visualizar Carrinho! ===")
            subtotal = 0

            for i in carrinho:
                print(
                    f"{i['Qtd']}x {i['Nome']} - Valor Unitário: R$ {i['preco']:.2f} (Total: R$ {i['Valor_total']:.2f})")
                subtotal += i['Valor_total']

            print("============================")
            print(f"Total Atual do Carrinho: R$ {subtotal:.2f}")
            print("============================\n")
        else:
            print("\n⚠ Carrinho vazio! Adicione produtos antes de visualizar.\n")

    elif opcao == 4:
        if carrinho:
            print("\n=== Finalizar Compra ===")

            total_compra = sum(item["Valor_total"] for item in carrinho)

            cupom = input("Digite um cupom (ou pressione Enter): ").upper()
            desconto = 0

            if cupom == "DEV10":
                desconto = total_compra * 0.1
                print("Cupom Valido: Voce obteve 10% de desconto.")
            elif cupom == "DEV20" and total_compra > 500:
                desconto = total_compra * 0.2
                print("Cupom valido: Voce obteve 20% de desconto.")
            elif len(cupom) == 0:
                print("Nenhum cupom adicionado.")
            else:
                print("Cupom invalido, nenhum desconto adicionado.")

            total = total_compra - desconto

            print(f"\nSubtotal: R$ {total_compra:.2f}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Total a pagar: R$ {total:.2f}")

            confirmar = input(
                "Confirmar pagamento? (S/N): ").upper()

            if confirmar == "S":
                print("Compra finalizada com sucesso!")
                carrinho.clear()
            else:
                for i in carrinho:
                    id_prod = i["id"]
                    estoque_produto[id_prod]["Quantidade"] += i["Qtd"]

                carrinho.clear()
                print("Compra cancelada. Itens devolvidos ao estoque.")
        else:
            print("\n⚠ Não há itens no carrinho para finalizar a compra.\n")

    elif opcao == 0:
        print("Sair do sistema.")
        break
    else:
        print("Opcao invalida!")

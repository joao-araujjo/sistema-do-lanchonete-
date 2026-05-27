def mostrar_cardapio():
    print("\n===== LANCHONETE DO GORDAO =====")
    print("1 - X-SIMPLES     R$ 12.00")
    print("2 - X-TUDO        R$ 15.00")
    print("3 - Batata frita  R$ 10.00")
    print("4 - Refrigerante  R$  6.00")
    print("5 - Finalizar pedido")
    print("0 - Sair")


def ler_opcao():
    while True:
        try:
            opcao = int(input("Escolha uma opcao: "))
            return opcao
        except ValueError:
            print("Opcao invalida. Digite apenas numeros.")


def ler_quantidade(nome_produto):
    while True:
        try:
            quantidade = int(input(f"Quantidade de {nome_produto}: "))
            if quantidade > 0:
                return quantidade
            else:
                print("A quantidade precisa ser maior que zero.")
        except ValueError:
            print("Quantidade invalida. Digite apenas numeros.")


def calcular_desconto(total):
    if total >= 80:
        return total * 0.15
    elif total >= 50:
        return total * 0.10
    elif total >= 30:
        return total * 0.05
    else:
        return 0


def mostrar_resumo(pedido, total):
    print("\n===== RESUMO DO PEDIDO =====")
    if len(pedido) == 0:
        print("Nenhum item foi comprado.")
    else:
        for item in pedido:
            print(f"{item['quantidade']}x {item['nome']} - R$ {item['subtotal']:.2f}")

        desconto = calcular_desconto(total)
        total_final = total - desconto
        print(f"\nTotal bruto: R$ {total:.2f}")
        print(f"Desconto:    R$ {desconto:.2f}")
        print(f"Total final: R$ {total_final:.2f}")


def adicionar_item(pedido, codigo, nome, preco):
    quantidade = ler_quantidade(nome)
    subtotal = quantidade * preco
    pedido.append({
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "subtotal": subtotal
    })
    print(f"{nome} adicionado ao pedido. Subtotal: R$ {subtotal:.2f}")
    return subtotal


def executar_sistema():
    pedido = []
    total = 0

    while True:
        mostrar_cardapio()
        opcao = ler_opcao()

        if opcao == 1:
            total += adicionar_item(pedido, 1, "X-SIMPLES", 12.00)
        elif opcao == 2:
            total += adicionar_item(pedido, 2, "X-TUDO", 15.00)
        elif opcao == 3:
            total += adicionar_item(pedido, 3, "Batata frita", 10.00)
        elif opcao == 4:
            total += adicionar_item(pedido, 4, "Refrigerante", 6.00)
        elif opcao == 5:
            mostrar_resumo(pedido, total)
        elif opcao == 0:
            mostrar_resumo(pedido, total)
            print("\nObrigado por usar o sistema da Lanchonete Do Gordao!")
            break
        else:
            print("Opcao inexistente. Escolha uma opcao do menu.")


executar_sistema()


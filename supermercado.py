# Supermercado Simples

# Dicionário com os produtos disponíveis no supermercado e seus preços
produtos = {
    "Arroz": 10.00,
    "Feijão": 8.50,
    "Macarrão": 5.00,
    "Leite": 4.30,
    "Pão": 3.50,
    "Banana": 2.00
}

# Carrinho de compras (vazio no início)
carrinho = []

def exibir_produtos():
    """Função para exibir os produtos disponíveis no supermercado."""
    print("\nProdutos disponíveis no supermercado:")
    for produto, preco in produtos.items():
        print(f"{produto}: R$ {preco:.2f}")

def adicionar_ao_carrinho(produto):
    """Função para adicionar um produto ao carrinho."""
    if produto in produtos:
        carrinho.append(produto)
        print(f"{produto} adicionado ao carrinho.")
    else:
        print("Produto não encontrado.")

def exibir_carrinho():
    """Função para exibir os produtos no carrinho e calcular o total."""
    if carrinho:
        print("\nCarrinho de compras:")
        total = 0
        for item in carrinho:
            print(f"{item}: R$ {produtos[item]:.2f}")
            total += produtos[item]
        print(f"Total: R$ {total:.2f}")
        return total
    else:
        print("O carrinho está vazio.")
        return 0

def finalizar_compra():
    """Função para finalizar a compra com pagamento."""
    total = exibir_carrinho()
    if total > 0:
        while True:
            try:
                pagamento = float(input(f"\nO total é R$ {total:.2f}. Insira o valor pago: R$ "))
                if pagamento >= total:
                    troco = pagamento - total
                    print(f"Compra finalizada. Seu troco é R$ {troco:.2f}. Obrigado por comprar conosco!")
                    carrinho.clear()  # Esvaziar o carrinho após a compra
                    break
                else:
                    print(f"Valor insuficiente. Faltam R$ {total - pagamento:.2f}.")
            except ValueError:
                print("Por favor, insira um valor válido.")
    else:
        print("O carrinho está vazio. Adicione itens antes de finalizar a compra.")

# Menu principal
while True:
    print("\n1. Exibir produtos")
    print("2. Adicionar produto ao carrinho")
    print("3. Exibir carrinho")
    print("4. Finalizar compra")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_produtos()
    elif opcao == "2":
        produto = input("Digite o nome do produto que deseja adicionar: ")
        adicionar_ao_carrinho(produto)
    elif opcao == "3":
        exibir_carrinho()
    elif opcao == "4":
        finalizar_compra()
    elif opcao == "5":
        print("Obrigado por usar o sistema do supermercado. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Função para exibir o menu
def exibir_menu():
    print("\n---- Menu do Inventário ----")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    return escolha

# Função para adicionar produto
def adicionar_produto(inventario):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    # Verifica se o produto já existe no inventário
    if nome in inventario:
        inventario[nome]['quantidade'] += quantidade
        print(f"Produto '{nome}' atualizado no inventário. Quantidade atualizada.")
    else:
        inventario[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' adicionado ao inventário.")

# Função para remover produto
def remover_produto(inventario):
    nome = input("Digite o nome do produto para remover: ")
    if nome in inventario:
        del inventario[nome]
        print(f"Produto '{nome}' removido do inventário.")
    else:
        print(f"Produto '{nome}' não encontrado no inventário.")

# Função para listar produtos
def listar_produtos(inventario):
    if inventario:
        print("\n--- Produtos no Inventário ---")
        for nome, dados in inventario.items():
            print(f"Nome: {nome}, Preço: R${dados['preco']:.2f}, Quantidade: {dados['quantidade']}")
    else:
        print("Não há produtos no inventário.")

# Função principal
def main():
    inventario = {}
    
    while True:
        escolha = exibir_menu()
        
        if escolha == '1':
            adicionar_produto(inventario)
        elif escolha == '2':
            remover_produto(inventario)
        elif escolha == '3':
            listar_produtos(inventario)
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

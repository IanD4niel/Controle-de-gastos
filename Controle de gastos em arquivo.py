#Controle de gastos em arquivo
import json
import os

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gastos.json")

def carregar_gastos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=4)

def menu():
    print("\n=== Gerenciador de Gastos ===")
    print("1. Adicionar Gasto")
    print("2. Listar Gastos")
    print("3. Total por categoria")
    print("4. Listar Categorias")
    print("5. Adicionar Categoria")
    print("0. Sair")

def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números.")

def adicionar_categoria():
    nome = input("Digite o nome da categoria: ")
    if nome in gastos:
        print("Essa categoria já existe.")
    else:
        gastos[nome] = []   #serve para criar uma nova categoria vazia
        print(f"Categoria '{nome}' adicionada com sucesso!")

def listar_categorias():
    if not gastos:
        print("Nenhuma categoria encontrada.")
    else:
        print("\n=== Lista de Categorias ===")
        for categoria in gastos:
            print(f"- {categoria}")

def adicionar_gasto():
    categoria = input("Digite a categoria do gasto: ")
    if categoria not in gastos:
        print("Categoria não encontrada. Por favor, adicione a categoria primeiro.")
        return
    data = input("Digite a data do gasto (dd/mm/aaaa): ")
    descricao = input("Digite a descrição do gasto: ")
    while True:
        try:
            valor = float(input("Digite o valor do gasto: "))
            break
        except ValueError:
            print("Por favor, digite um valor numérico válido.")
    gasto = {"data": data, "descricao": descricao, "valor": valor}
    gastos[categoria].append(gasto)   #coloca o gasto dentro da lista da categoria
    print("Gasto adicionado com sucesso!")

def listar_gastos():
    if not gastos:
        print("Nenhuma categoria encontrada.")
    for categoria, lista in gastos.items():
        print(f"\nCategoria: [{categoria}]")
        for i, g in enumerate(lista, start=1):
            print(f"{i}. Data: {g['data']}, Descrição: {g['descricao']}, Valor: R${g['valor']:.2f}")

def total_por_categoria():
    for categoria in gastos:
        total = sum(g['valor'] for g in gastos[categoria])
        print(f"Total gasto em {categoria}: R${total:.2f}")

gastos = carregar_gastos()
while True:
    menu()
    opcao = ler_numero("Escolha uma opção: ")
    if opcao == 1:
        adicionar_gasto()
    elif opcao == 2:
        listar_gastos()
    elif opcao == 3:
        total_por_categoria()
    elif opcao == 4:
        listar_categorias()
    elif opcao == 5:
        adicionar_categoria()
    elif opcao == 0:
        salvar(gastos)
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

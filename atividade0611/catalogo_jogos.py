import os

# Lista principal para armazenar os jogos
catalogo = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_jogo():
    print("\n--- CADASTRAR NOVO JOGO ---")
    nome = input("Nome do jogo: ").strip()
    if not nome:
        print("O nome não pode estar vazio!")
        return
    
    plataforma = input("Plataforma (ex: PC, PS5, Switch, Xbox): ").strip()
    genero = input("Gênero (ex: RPG, Ação, FPS): ").strip()
    
    jogo = {
        "nome": nome,
        "plataforma": plataforma,
        "genero": genero,
        "concluido": False
    }
    
    catalogo.append(jogo)
    print(f"\nSucesso! '{nome}' foi cadastrado com sucesso.")

def listar_jogos():
    print("\n--- LISTA DE JOGOS ---")
    if not catalogo:
        print("Nenhum jogo cadastrado no catálogo.")
        return

    for i, jogo in enumerate(catalogo, 1):
        status = "Concluído" if jogo["concluido"] else "Não concluído"
        print(f"{i}. {jogo['nome']} | Plataforma: {jogo['plataforma']} | Gênero: {jogo['genero']} | Status: {status}")

def marcar_concluido():
    print("\n--- MARCAR JOGO COMO CONCLUÍDO ---")
    if not catalogo:
        print("Nenhum jogo cadastrado.")
        return
    
    listar_jogos()
    try:
        escolha = int(input("\nDigite o número do jogo que deseja marcar como concluído: "))
        if 1 <= escolha <= len(catalogo):
            catalogo[escolha - 1]["concluido"] = True
            print(f"Parabéns! '{catalogo[escolha - 1]['nome']}' marcado como concluído.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def pesquisar_jogos():
    print("\n--- PESQUISAR JOGOS ---")
    if not catalogo:
        print("Nenhum jogo cadastrado.")
        return
    
    termo = input("Digite o nome (ou parte do nome) do jogo que deseja buscar: ").lower()
    encontrados = [j for j in catalogo if termo in j["nome"].lower()]
    
    if encontrados:
        print(f"\nForam encontrados {len(encontrados)} jogo(s):")
        for jogo in encontrados:
            status = "Concluído" if jogo["concluido"] else "Não concluído"
            print(f"- {jogo['nome']} ({jogo['plataforma']} | {jogo['genero']}) - [{status}]")
    else:
        print("Nenhum jogo encontrado com esse termo.")

def gerar_estatisticas():
    print("\n--- ESTATÍSTICAS DO CATÁLOGO ---")
    total = len(catalogo)
    if total == 0:
        print("Nenhum jogo cadastrado para gerar estatísticas.")
        return
    
    concluidos = sum(1 for j in catalogo if j["concluido"])
    porcentagem = (concluidos / total) * 100
    
    print(f"Total de jogos cadastrados: {total}")
    print(f"Jogos concluídos: {concluidos} ({porcentagem:.1f}%)")
    print(f"Jogos pendentes: {total - concluidos}")

    # Estatísticas por plataforma
    print("\nJogos por Plataforma:")
    plataformas = {}
    for j in catalogo:
        p = j["plataforma"] or "Desconhecida"
        plataformas[p] = plataformas.get(p, 0) + 1
    for plat, qtd in plataformas.items():
        print(f"  - {plat}: {qtd}")

def menu():
    while True:
        print("\n===============================")
        print("    CATÁLOGO DE JOGOS - CLI    ")
        print("===============================")
        print("1. Cadastrar Jogo")
        print("2. Listar Jogos")
        print("3. Marcar como Concluído")
        print("4. Pesquisar Títulos")
        print("5. Gerar Estatísticas")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
        if opcao == "1":
            cadastrar_jogo()
        elif opcao == "2":
            listar_jogos()
        elif opcao == "3":
            marcar_concluido()
        elif opcao == "4":
            pesquisar_jogos()
        elif opcao == "5":
            gerar_estatisticas()
        elif opcao == "6":
            print("\nSaindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 6.")
        
        input("\nPressione ENTER para continuar...")
        limpar_tela()

if __name__ == "__main__":
    menu()
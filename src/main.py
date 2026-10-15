
tarefas = []


def ler_titulo():
    """Solicita um título obrigatório e não vazio."""
    while True:
        titulo = input("Título: ").strip()

        if titulo:
            return titulo

        print("Erro: o título não pode ficar vazio. Tente novamente.")


def ler_prioridade():
    """Aceita somente Alta, Média ou Baixa."""
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa"
    }

    while True:
        prioridade = input(
            "Prioridade (Alta/Média/Baixa): "
        ).strip().casefold()

        if prioridade in prioridades:
            return prioridades[prioridade]

        print(
            "Erro: prioridade inválida. "
            "Digite Alta, Média ou Baixa."
        )


def cadastrar_tarefa():
    """Recebe os dados e cadastra uma nova tarefa."""
    print("\n--- CADASTRAR NOVA TAREFA ---")

    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")
    print(f"Status: {tarefa['status']}")


def visualizar_tarefas():
    """Exibe todas as tarefas cadastradas."""
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or 'Não informada'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or 'Não informada'}")
        print(f"Status: {tarefa['status']}")


def exibir_menu():
    """Mostra as opções disponíveis."""
    print("\n" + "=" * 32)
    print("          TASKTRACKER")
    print("=" * 32)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    """Controla o menu e a navegação da aplicação."""
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até mais!")
            break
        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()


import unicodedata
from datetime import datetime

tarefas = []


def limpar_entrada(valor):
    """Remove espaços e caracteres invisíveis das extremidades."""
    return "".join(
        caractere
        for caractere in valor
        if unicodedata.category(caractere) not in ("Cf", "Cc", "Cs")
    ).strip()


def ler_campo(mensagem):
    """Impede campos vazios ou compostos por caracteres invisíveis."""
    while True:
        valor = limpar_entrada(input(mensagem))

        if valor:
            return valor

        print("Erro: este campo não pode ficar vazio. Tente novamente.")


def ler_titulo():
    """Solicita um título obrigatório."""
    return ler_campo("Título: ")


def ler_descricao():
    """Solicita uma descrição obrigatória."""
    return ler_campo("Descrição: ")


def ler_prioridade():
    """Aceita somente Alta, Média/Media ou Baixa."""
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa"
    }

    while True:
        prioridade = ler_campo(
            "Prioridade (Alta/Média/Baixa): "
        ).casefold()

        if prioridade in prioridades:
            return prioridades[prioridade]

        print(
            "Erro: prioridade inválida. "
            "Digite Alta, Média ou Baixa."
        )

def ler_data_limite():
    """Solicita uma data válida no formato brasileiro DD/MM/AAAA."""
    while True:
        data = ler_campo("Data limite (DD/MM/AAAA): ")

        try:
            data_validada = datetime.strptime(data, "%d/%m/%Y")

            # Confirma que a entrada corresponde exatamente ao formato exigido.
            if data_validada.strftime("%d/%m/%Y") == data:
                return data

            print("Erro: use exatamente o formato DD/MM/AAAA.")

        except ValueError:
            print(
                "Erro: data inválida! Digite uma data válida "
                "no formato DD/MM/AAAA (ex.: 25/12/2026)."
            )



def cadastrar_tarefa():
    """Recebe, valida e cadastra uma tarefa."""
    print("\n--- CADASTRAR NOVA TAREFA ---")

    tarefa = {
        "titulo": ler_titulo(),
        "descricao": ler_descricao(),
        "prioridade": ler_prioridade(),
        "data_limite": ler_data_limite(),
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
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
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
    """Controla o menu e a navegação."""
    while True:
        exibir_menu()
        opcao = ler_campo("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()

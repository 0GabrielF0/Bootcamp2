
# TaskTracker

Aplicação CLI desenvolvida em Python para cadastro e visualização de tarefas de uma equipe.

## Funcionalidades

- Cadastro de tarefas com título, descrição, prioridade e data limite.
- Validação de título obrigatório.
- Validação de prioridades: Alta, Média e Baixa.
- Definição automática do status como Pendente.
- Listagem das tarefas cadastradas.
- Tratamento de opções inválidas no menu.

## Tecnologias

- Python 3
- Git
- GitHub
- Visual Studio Code

## Estrutura do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Requisitos

- Python 3 instalado.
- Git instalado para versionamento.

## Como executar

1. Clone o repositório ou abra a pasta do projeto.
2. Abra o terminal na raiz do projeto.
3. Execute:

```bash
python src/main.py
```

No Windows, caso necessário, utilize:

```bash
py src/main.py
```

## Armazenamento

Nesta versão, as tarefas ficam armazenadas em memória
durante a execução. Ao encerrar o programa, os registros
são perdidos.

## Objetivo acadêmico

Aplicar conceitos de programação em Python, estruturas
de dados, funções, validação de entradas e versionamento
colaborativo com Git e GitHub.

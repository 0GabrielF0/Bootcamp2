# TaskTracker

Aplicação de linha de comando (CLI) desenvolvida em Python para cadastro e visualização de tarefas de uma equipe. O projeto aplica conceitos de programação, validação de dados, versionamento colaborativo e conteinerização com Docker.

## Funcionalidades

- Cadastro de tarefas com título, descrição, prioridade e data limite.
- Validação de título e descrição obrigatórios.
- Validação de prioridades: Alta, Média e Baixa.
- Validação de data no formato `DD/MM/AAAA`.
- Definição automática do status como Pendente.
- Listagem das tarefas cadastradas.
- Tratamento de opções inválidas no menu.

## Tecnologias

- Python 3
- Git e GitHub
- Docker
- Docker Compose
- Visual Studio Code

## Estrutura do projeto

```text
ETAPA2/
├── src/
│   └── main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Requisitos

Para executar diretamente com Python:
- Python 3 instalado.

Para executar com Docker:
- Docker instalado e em execução.
- Docker Compose disponível.

## Como executar com Python

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

## Como executar com Docker

O projeto possui um `Dockerfile` para construir a imagem da aplicação e um `docker-compose.yml` para facilitar a execução.

### 1. Construir a imagem

Na raiz do projeto, execute:

```bash
docker compose build
```

Também é possível construir diretamente com:

```bash
docker build -t tasktracker .
```

### 2. Executar com Docker Compose

Para iniciar a aplicação de forma interativa:

```bash
docker compose run --rm tasktracker
```

### 3. Executar diretamente com Docker

Após construir a imagem com o nome `tasktracker`, execute:

```bash
docker run -it --rm tasktracker
```

**Observação:** como o TaskTracker é uma aplicação CLI interativa, o comando `docker compose run --rm tasktracker` é a forma recomendada para utilizar o menu e interagir com a aplicação pelo terminal.

## Armazenamento

Nesta versão, as tarefas ficam armazenadas em memória durante a execução. Ao encerrar o programa, os registros são perdidos. Não há persistência em banco de dados.

## Conteinerização

A aplicação é empacotada em uma imagem baseada em `python:3.11-slim`. O Dockerfile configura o diretório de trabalho, copia o código-fonte e define o comando de inicialização.

O Docker Compose facilita a construção e execução do serviço, reduzindo a necessidade de configurações manuais no ambiente de execução.

## Objetivo acadêmico

Aplicar conceitos de programação em Python, estruturas de dados, funções, validação de entradas, versionamento colaborativo com Git e GitHub e práticas de DevOps por meio da conteinerização com Docker.

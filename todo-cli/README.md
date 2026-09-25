# Todo CLI

Gerenciador de tarefas simples via linha de comando, feito em Python com persistência em SQLite.

## Funcionalidades

- Adicionar tarefas
- Listar tarefas (concluídas e pendentes)
- Marcar tarefas como concluídas
- Remover tarefas

## Tecnologias

- Python 3
- SQLite3 (biblioteca padrão)
- argparse (biblioteca padrão)
- pytest (testes)

## Como usar

```bash
# Adicionar uma tarefa
python todo.py add "Estudar Python"

# Listar tarefas
python todo.py list

# Marcar tarefa como concluída (pelo id mostrado na listagem)
python todo.py done 1

# Remover uma tarefa
python todo.py remove 1
```

## Rodando os testes

```bash
pip install -r requirements.txt
pytest
```

## Estrutura do projeto

```
todo-cli/
├── todo.py           # CLI principal
├── tests/
│   └── test_todo.py  # Testes automatizados
├── requirements.txt
└── README.md
```

## Possíveis melhorias futuras

- Adicionar prazos (due dates) às tarefas
- Filtrar tarefas por status (pendente/concluída)
- Interface web com FastAPI

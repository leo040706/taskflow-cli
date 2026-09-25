"""
Todo CLI — gerenciador simples de tarefas via linha de comando.

Uso:
    python todo.py add "Estudar SQL"
    python todo.py list
    python todo.py done 1
    python todo.py remove 1
"""

import argparse
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "tasks.db"


def get_connection() -> sqlite3.Connection:
    """Abre (ou cria) a conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    return conn


def add_task(description: str) -> None:
    """Adiciona uma nova tarefa."""
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    print(f"Tarefa adicionada: {description}")


def list_tasks() -> None:
    """Lista todas as tarefas cadastradas."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, description, done FROM tasks ORDER BY id"
        ).fetchall()

    if not rows:
        print("Nenhuma tarefa cadastrada.")
        return

    for task_id, description, done in rows:
        status = "[x]" if done else "[ ]"
        print(f"{task_id:>3} {status} {description}")


def complete_task(task_id: int) -> None:
    """Marca uma tarefa como concluída."""
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET done = 1 WHERE id = ?", (task_id,)
        )
    if cursor.rowcount:
        print(f"Tarefa {task_id} marcada como concluída.")
    else:
        print(f"Tarefa {task_id} não encontrada.")


def remove_task(task_id: int) -> None:
    """Remove uma tarefa pelo id."""
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount:
        print(f"Tarefa {task_id} removida.")
    else:
        print(f"Tarefa {task_id} não encontrada.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas simples.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    add_parser.add_argument("description", help="Descrição da tarefa")

    subparsers.add_parser("list", help="Lista todas as tarefas")

    done_parser = subparsers.add_parser("done", help="Marca uma tarefa como concluída")
    done_parser.add_argument("id", type=int, help="ID da tarefa")

    remove_parser = subparsers.add_parser("remove", help="Remove uma tarefa")
    remove_parser.add_argument("id", type=int, help="ID da tarefa")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.id)
    elif args.command == "remove":
        remove_task(args.id)


if __name__ == "__main__":
    main()

"""Testes básicos para o todo.py usando um banco de dados temporário."""

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import todo  # noqa: E402


@pytest.fixture(autouse=True)
def temp_db(tmp_path, monkeypatch):
    """Substitui o banco de dados real por um temporário durante os testes."""
    fake_db = tmp_path / "test_tasks.db"
    monkeypatch.setattr(todo, "DB_PATH", fake_db)
    yield fake_db


def test_add_and_list_task(capsys):
    todo.add_task("Estudar SQL")
    todo.list_tasks()
    captured = capsys.readouterr()
    assert "Estudar SQL" in captured.out
    assert "[ ]" in captured.out


def test_complete_task(capsys):
    todo.add_task("Ler um livro")
    todo.complete_task(1)
    todo.list_tasks()
    captured = capsys.readouterr()
    assert "[x]" in captured.out


def test_remove_task(capsys):
    todo.add_task("Tarefa temporária")
    todo.remove_task(1)
    todo.list_tasks()
    captured = capsys.readouterr()
    assert "Nenhuma tarefa cadastrada." in captured.out


def test_complete_nonexistent_task(capsys):
    todo.complete_task(999)
    captured = capsys.readouterr()
    assert "não encontrada" in captured.out

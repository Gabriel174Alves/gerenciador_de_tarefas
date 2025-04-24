import sqlite3
from datetime import datetime
from colorama import Fore

DB_NAME = "tarefas.db"

def conectar():
    conn   = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    """Cria a tabela de tarefas (status como TEXT)."""
    conn, cursor = conectar()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao    TEXT    NOT NULL,
            data_criacao TEXT    NOT NULL,
            status       TEXT    NOT NULL DEFAULT 'pendente'
        );
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao):
    conn, cursor = conectar()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO tarefas (descricao, data_criacao, status)
        VALUES (?, ?, 'pendente')
    ''', (descricao, data))
    conn.commit()
    conn.close()

def visualizar_tarefas():
    conn, cursor = conectar()
    cursor.execute("SELECT id, descricao, data_criacao, status FROM tarefas")
    tarefas = cursor.fetchall()
    if tarefas:
        print(Fore.CYAN + "Tarefas:")
        for id_tarefa, descricao, data, status in tarefas:
            cor = Fore.YELLOW if status == "pendente" else Fore.GREEN
            print(cor + f"[ID:{id_tarefa}] {descricao} | {status} | Criada em: {data}")
    else:
        print(Fore.RED + "Nenhuma tarefa encontrada.")
    conn.close()

def marcar_como_concluida(id_tarefa):
    conn, cursor = conectar()
    cursor.execute(
        "UPDATE tarefas SET status = ? WHERE id = ?",
        ('concluida', id_tarefa)
    )
    conn.commit()
    conn.close()

def remover_tarefa(id_tarefa):
    conn, cursor = conectar()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()

# Garante que a tabela exista sempre que o módulo for importado
criar_tabela()

from dataclasses import dataclass
from datetime import datetime

from utils import questionario_auditoria

@dataclass
class SQL:
    nome: str
    status_global_sql: str
    status_global_sql_texto: str
    agente: str
    agente_texto: str    
    simulacao_restauro_sql: str
    simulacao_restauro_sql_texto: str
    logs: str
    logs_texto: str
    data_ultimo_ponto: str
    tamanho_backup: str

PERGUNTAS_SQL = [
    (
        "status_global_sql",
        "O banco SQL consta como protegido no painel?",
        "O banco SQL consta como 'Protegido' no painel.",
        "O banco SQL NÃO consta como 'Protegido' no painel.",
    ),
    (
        "agente",
        "O banco SQL está funcionando normalmente?",
        "O SQL Server VSS Writer está funcionando corretamente.",
        "Foi identificada uma possível falha no SQL Server VSS Writer.",
    ),
    (
        "simulacao_restauro_sql",
        "A simulação ocorreu com sucesso e a estrutura foi listada?",
        "A estrutura de diretórios foi listada com sucesso.",
        "A simulação de restauro não ocorreu conforme esperado.",
    ),
    (
        "logs",
        "A atividade do banco está consistente?",
        "Não há erros ou truncamentos.",
        "Foram encontrados erros ou truncamentos.",
    ),
]

def auditar_sql():
    print(f"\n{'=' * 50}")
    print("AUDITORIA SQL SERVER")
    print(f"{'=' * 50}\n")

    respostas = {}

    nome = input("Nome do servidor (SQL): ").strip()

    respostas = questionario_auditoria(
        PERGUNTAS_SQL
        )

    while True:
        data_ultimo_ponto = input(
            "Data/Hora do Último Ponto do SQL (dd/mm/aaaa às hh:mm): "
        ).strip()

        try:
            datetime.strptime(
                data_ultimo_ponto,
                "%d/%m/%Y às %H:%M"
            )
            break

        except ValueError:
            print("Formato inválido.")

    tamanho_backup = input(
        "Tamanho do Backup Incremental em Nuvem (SQL): "
    ).strip()

    return SQL(
        nome=nome,
        status_global_sql=respostas["status_global_sql"],
        status_global_sql_texto=respostas["status_global_sql_texto"],
        agente=respostas["agente"],
        agente_texto=respostas["agente_texto"],
        simulacao_restauro_sql=respostas["simulacao_restauro_sql"],
        simulacao_restauro_sql_texto=respostas["simulacao_restauro_sql_texto"],
        logs=respostas["logs"],
        logs_texto=respostas["logs_texto"],
        data_ultimo_ponto=data_ultimo_ponto,
        tamanho_backup=tamanho_backup
    )
from dataclasses import dataclass
from utils import perguntar, pergunta_quantidade

@dataclass
class Cliente:
    identificacao: str
    quantidade_servidores: int
    possui_sql: bool
    quantidade_servidores_sql: int

def coletar_cliente():
    identificacao = input(
        "Cliente a ser auditado: "
    ).strip()

    quantidade_servidores_sql = 0

    quantidade_servidores = pergunta_quantidade(
        "Quantidade de servidores: "
    )

    possui_sql, _, _ = perguntar(
        "O cliente possui SQL?",
        "Cliente possui ambiente SQL Server.",
        "Cliente não possui ambiente SQL Server."
    )

    if possui_sql:
        quantidade_servidores_sql = pergunta_quantidade(
            "Quantidade de servidores (SQL): "    
    )

    return Cliente(
        identificacao=identificacao,
        possui_sql=possui_sql,
        quantidade_servidores=quantidade_servidores,
        quantidade_servidores_sql=quantidade_servidores_sql,
    )
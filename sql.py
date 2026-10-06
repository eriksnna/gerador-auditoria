from dataclasses import dataclass
from datetime import datetime

from utils import perguntar


@dataclass
class SQL:
    nome: str
    agente: str
    agente_texto: str    
    simulacao: str
    simulacao_texto: str
    logs: str
    logs_texto: str
    data_ultimo_ponto: str
    tamanho_backup: str

PERGUNTAS_SQL = [
    (
        "agente",
        "Os bancos SQL estão funcionando normalmente?",
        "O SQL Server VSS Writer está funcionando corretamente.",
        "Foi identificada uma possível falha no SQL Server VSS Writer.",
    ),
    (
        "simulacao",
        "A simulação de restauro SQL está OK?",
        "Todos os bancos aparecem disponíveis.",
        "Nem todos os bancos apareceram disponíveis.",
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

    for chave, pergunta_txt, texto_sim, texto_nao in PERGUNTAS_SQL:
        emoji, texto = perguntar(
            pergunta_txt,
            texto_sim,
            texto_nao
        )

        respostas[chave] = emoji
        respostas[f"{chave}_texto"] = texto

    while True:
        data_ultimo_ponto = input(
            "Data/Hora do Último Ponto do SQL: "
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
        "Tamanho do Backup em Nuvem (SQL): "
    ).strip()

    return SQL(
        nome=nome,
        agente=respostas["agente"],
        agente_texto=respostas["agente_texto"],
        simulacao=respostas["simulacao"],
        simulacao_texto=respostas["simulacao_texto"],
        logs=respostas["logs"],
        logs_texto=respostas["logs_texto"],
        data_ultimo_ponto=data_ultimo_ponto,
        tamanho_backup=tamanho_backup
    )
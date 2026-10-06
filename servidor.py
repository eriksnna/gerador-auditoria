from dataclasses import dataclass
from datetime import datetime

from utils import perguntar


@dataclass
class Servidor:
    nome: str
    status_global: str
    status_global_texto: str
    simulacao_restauro: str
    simulacao_restauro_texto: str
    consistencia: str
    consistencia_texto: str
    data_ultimo_ponto: str
    tamanho_backup: str

PERGUNTAS_SERVIDOR = [
    (
        "status_global",
        "O servidor consta como protegido no painel?",
        "O servidor consta como 'Protegido' no painel.",
        "O servidor NÃO consta como 'Protegido' no painel.",
    ),
    (
        "simulacao_restauro",
        "A simulação ocorreu com sucesso e a estrutura foi listada?",
        "A estrutura de diretórios foi listada com sucesso.",
        "A simulação de restauro não ocorreu conforme esperado.",
    ),
    (
        "consistencia",
        "O tamanho do backup é consistente com o tamanho real do servidor?",
        "O tamanho do backup parece consistente.",
        "O tamanho do backup não parece consistente.",
    ),
]


def auditar_servidor():
    print(f"\n{'=' * 50}")
    print("AUDITORIA DO SERVIDOR")
    print(f"{'=' * 50}\n")

    while True:
        nome = input(
            "Nome do servidor: "
            ).strip()
        if nome:
            break

        print("Informe um nome válido.")

    respostas = {}

    for chave, pergunta_txt, texto_sim, texto_nao in PERGUNTAS_SERVIDOR:
        emoji, texto = perguntar(
            pergunta_txt,
            texto_sim,
            texto_nao
        )

        respostas[chave] = emoji
        respostas[f"{chave}_texto"] = texto

    while True:
        data_ultimo_ponto = input(
            "Data/Hora do Último Ponto Gerado (dd/mm/aaaa às hh:mm): "
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
        "Tamanho do Backup em Nuvem: "
    ).strip().upper()

    return Servidor(
        nome=nome,
        status_global=respostas["status_global"],
        status_global_texto=respostas["status_global_texto"],
        simulacao_restauro=respostas["simulacao_restauro"],
        simulacao_restauro_texto=respostas["simulacao_restauro_texto"],
        consistencia=respostas["consistencia"],
        consistencia_texto=respostas["consistencia_texto"],
        data_ultimo_ponto=data_ultimo_ponto,
        tamanho_backup=tamanho_backup
    )
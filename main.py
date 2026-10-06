from datetime import datetime

from cliente import coletar_cliente
from servidor import auditar_servidor
from sql import auditar_sql

def pergunta_status_final():

    opcoes = {
        "1": "SUCESSO TOTAL",
        "2": "FALHA SILENCIOSA DETECTADA",
        "3": "ERRO IDENTIFICADO"
    }

    print("\n=== STATUS FINAL DA AUDITORIA ===\n")

    for codigo, descricao in opcoes.items():
        print(f"{codigo} - {descricao}")

    while True:

        escolha = input(
            "\nEscolha o status final (1/2/3): "
        ).strip()

        if escolha in opcoes:
            return escolha, opcoes[escolha]

        print("Escolha apenas 1, 2 ou 3.")

def coletar_observacoes():

    print("\n=== OBSERVAÇÕES ===")
    print(
        "Digite as observações ou ações corretivas."
    )
    print(
        "Pressione ENTER em uma linha vazia para finalizar.\n"
    )

    linhas = []

    while True:

        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    return "\n".join(linhas)

def gerar_bloco_servidor(servidor):

    return f"""
### {servidor.nome}

- {servidor.status_global} **STATUS GLOBAL:** {servidor.status_global_texto}
- **DATA/HORA DO ÚLTIMO PONTO:** {servidor.data_ultimo_ponto}
- {servidor.simulacao_restauro} **SIMULAÇÃO DE RESTAURO:** {servidor.simulacao_restauro_texto}
- {servidor.consistencia} **CONSISTÊNCIA DE TAMANHO:** {servidor.consistencia_texto}
- **TAMANHO DO BACKUP INCREMENTAL EM NUVEM:** {servidor.tamanho_backup}

---
"""

def gerar_bloco_sql(sql):

    return f"""
### {sql.nome}

- {sql.status_global_sql} **STATUS GLOBAL:** {sql.status_global_sql_texto}
- {sql.agente} **AGENTE SQL:** {sql.agente_texto}
- **DATA/HORA DO ÚLTIMO PONTO:** {sql.data_ultimo_ponto}
- {sql.simulacao_restauro_sql} **SIMULAÇÃO DE RESTAURO SQL:** {sql.simulacao_restauro_sql_texto}
- {sql.logs} **VERIFICAÇÃO DE LOGS:** {sql.logs_texto}
- **TAMANHO DO BACKUP INCREMENTAL EM NUVEM:** {sql.tamanho_backup}

---
"""

def gerar_bloco_status_final(status):

    codigo, _ = status

    return f"""
### STATUS FINAL DA AUDITORIA

- {"✅" if codigo == "1" else "⬜"} **SUCESSO TOTAL**
- {"❗" if codigo == "2" else "⬜"} **FALHA SILENCIOSA DETECTADA**
- {"❌" if codigo == "3" else "⬜"} **ERRO IDENTIFICADO**
"""

def gerar_relatorio(
    cliente,
    servidores,
    sqls,
    status_final,
    observacoes
):

    data_hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    relatorio = f"""# Relatório de Auditoria Semanal - {cliente.identificacao}

**Data de geração:** {data_hora}

Prezado(a),

Estamos enviando o relatório de Auditoria Semanal referente ao cliente **{cliente.identificacao}**.

## 🖥️ AUDITORIA DE SERVIDORES

"""

    for servidor in servidores:
        relatorio += gerar_bloco_servidor(
            servidor
        )

    relatorio += "\n## 🗄️ AUDITORIA SQL SERVER\n"

    if sqls:
        for sql in sqls:
            relatorio += gerar_bloco_sql(sql)
    else:
        relatorio += """
Cliente não possui ambiente SQL Server.
 
---
"""

    relatorio += f"""

## 📎 EVIDÊNCIAS E ENCERRAMENTO

{gerar_bloco_status_final(status_final)}

### OBSERVAÇÕES / AÇÕES DE CORREÇÃO APLICADAS

{observacoes if observacoes else "Nenhuma ação corretiva foi necessária."}

---

Atenciosamente,

"""
    return relatorio

def salvar_relatorio(relatorio, identificacao):

    nome_arquivo = (
        f"{identificacao}_auditoria_semanal_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    )

    with open(
        nome_arquivo,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(relatorio)

    return nome_arquivo

def main():

    print("\n=== AUDITORIA SEMANAL ===\n")

    cliente = coletar_cliente()

    if (
        cliente.quantidade_servidores == 0
        and
        cliente.quantidade_servidores_sql == 0
    ):

        print(
            "\nNenhum servidor informado. Encerrando auditoria."
        )

        return

    print("\n=== SERVIDORES ===")

    servidores = []

    for i in range(
        cliente.quantidade_servidores
    ):

        print(
            f"\nServidor {i + 1} de {cliente.quantidade_servidores}"
        )

        servidores.append(
            auditar_servidor()
        )

    sqls = []

    for i in range(
        cliente.quantidade_servidores_sql
        ):

        print(
            f"\nServidor {i + 1} de {cliente.quantidade_servidores_sql}"
        )

        sqls.append(
            auditar_sql()
        )

    status_final = pergunta_status_final()

    observacoes = coletar_observacoes()

    relatorio = gerar_relatorio(
        cliente=cliente,
        servidores=servidores,
        sqls=sqls,
        status_final=status_final,
        observacoes=observacoes
    )

    nome_arquivo = salvar_relatorio(
        relatorio,
        cliente.identificacao
    )

    print("\n========================================")
    print("Relatório gerado com sucesso!")
    print(f"Arquivo: {nome_arquivo}")
    print(f"Status final: {status_final[1]}")
    print("========================================")


if __name__ == "__main__":
    main()
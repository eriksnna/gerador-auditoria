from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class Cliente:
    identificacao: str
    servidores: list
    sqls: list

def coletar_cliente():

    arquivos = sorted(
        Path("data/clientes").glob("*.json")
    )

    if not arquivos:
        raise FileNotFoundError(
            "Nenhum cliente encontrado."
        )

    print("\n=== CLIENTES ===\n")

    for i, arquivo in enumerate(
        arquivos,
        start=1
    ):
        print(
            f"{i} - {arquivo.stem}"
        )

    while True:

        try:

            escolha = int(
                input(
                    "\nSelecione o cliente: "
                )
            )

            if not (
                1 <= escolha <= len(arquivos)
            ):
                print("Opção inválida.")
                continue

            arquivo = arquivos[
                escolha - 1
            ]

            with open(
                arquivo,
                "r",
                encoding="utf-8"
            ) as f:

                dados = json.load(f)

            return Cliente(
                identificacao=dados["nome"],
                servidores=dados.get("servidores", []),
                sqls=dados.get("sql", [])
            )

        except (
            ValueError,
            IndexError
        ):

            print("Opção inválida.")
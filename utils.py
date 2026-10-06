#funções utilitárias

def perguntar(pergunta, texto_sim, texto_nao):
    while True:
        resposta = input(f"{pergunta} (y/n): ").strip().lower()

        if resposta == "y":
            return True, "✅", texto_sim

        if resposta == "n":
            return False, "❌", texto_nao

        print("Insira apenas y ou n.")



def pergunta_quantidade(pergunta):
    while True:
        try:
            valor = int(input(pergunta).strip())

            if valor >= 0:
                return valor

            print("Digite um número igual ou maior que zero.")

        except ValueError:
            print("Digite um número inteiro válido.")
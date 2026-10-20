#funções utilitárias

def perguntar(pergunta, texto_sim, texto_nao):
    while True:
        resposta = input(f"{pergunta} (y/n): ").strip().lower()

        if resposta == "y":
            return True, "✅", texto_sim

        if resposta == "n":
            return False, "❌", texto_nao

        print("Insira apenas y ou n.")

def questionario_auditoria(perguntas):
    respostas = {}

    for chave, pergunta_txt, texto_sim, texto_nao in perguntas:
        resposta, emoji, texto = perguntar(
            pergunta_txt,
            texto_sim,
            texto_nao
        )

        respostas[chave] = emoji
        respostas[f"{chave}_texto"] = texto
        respostas[f"{chave}_bool"] = resposta

    return respostas
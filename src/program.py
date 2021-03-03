# IMPORTANTE: Indique o seu número de estudante em string, na variável de módulo
# `number`
import sudoku as sd
number = "INDICAR NÚMERO DE ESTUDANTE"


def obter_jogador(jogo, nome):
    for jogador in jogo["jogadores"]:
        if jogador["nome"] == nome:
            return jogador
    return None


def existe_jogador(jogo, nome):
    return obter_jogador(jogo, nome) is not None


def existe_jogo_em_curso(jogo):
    return jogo["em_curso"] is not None


def localizacao_valida(linha, letra_coluna):
    coluna = ord(letra_coluna.upper()) - ord("A") + 1
    return linha > 0 and linha <= 4 and coluna > 0 and coluna <= 4


def main():
    jogo = {
        "jogadores": [],
        "grelha": None,
        "em_curso": None
    }

    linha = input()
    comandos = linha.split(" ")
    if comandos[0] == "RJ":
        nome = comandos[1]
        # Não existe método existe_jogador em sudoky.py!!
        if existe_jogador(jogo, nome):
            print("Ocorreu um erro.")
        else:
            sd.registar_jogador(jogo, nome)
            print("Jogador registado.")
    elif comandos[0] == "IJ":
        nome = comandos[1]
        grelha_inicial = comandos[2]

        if not existe_jogador(jogo, nome) or existe_jogo_em_curso(jogo):
            print("Ocorreu um erro.")
        else:
            sd.iniciar_jogo(jogo, nome, grelha_inicial)
            print("Jogo iniciado.")

    elif comandos[0] == "CN":
        nome = comandos[0]
        linha = comandos[1]
        coluna = comandos[2]
        numero = comandos[3]

        if not existe_jogo_em_curso(jogo) or not localizacao_valida(linha, coluna):
            print("Ocorreu um erro.")
        else:
            sd.colocar_numero(jogo, linha, coluna, numero)
            if sd.verificar_vitoria(jogo, nome):
                print("Jogo terminado.")
            else:
                print("Número colocado com sucesso.")
    elif comandos[0] == "CJ":
        nome = comandos[0]
        jogador = obter_jogador(jogo, nome)
        print(jogador["jogos"])


if __name__ == "__main__":
    main()

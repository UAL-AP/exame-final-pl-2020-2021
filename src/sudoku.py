# Regras
# 1. O número de estudante determina que funcionalidades deve implementar.
#    Verifique no comentário de cada método.
# 2. A variável jogo é um dicionário com a seguinte estrutura mínima:
#
#    jogo = {'jogadores': lista, 'grelha': lista de listas}
#
# 3. Pode aumentar o dicionário jogo, desde que mantenha a estrutura mínima.
# 4. Não pode alterar a assinatura de qualquer método.
# 5. Não pode acrescentar métodos.
# 6. Não pode recorrer a bibliotecas externas à distribuição padrão Python 3.8.5


# IMPORTANTE: Indique o seu número de estudante em string, na variável de módulo
# `number`
number = "INDICAR NÚMERO DE ESTUDANTE"

# IMPORTANTE: A variável de módulo last_digit guarda o último dígito do número de aluno, e
# soma o valor 1. Vai ser utilizada para determinar que funcionalidades deve implementar.
last_digit = int(number[len(number)-1])+1


def registar_jogador(jogo, nome):
    # Um jogador é representado com um dicionário com a seguinte estrutura
    # mínima:
    #
    # jogador = {'nome': string, 'jogos': int}
    #
    # O nome do jogador deve ser guardado tal como estiver no parâmetro `nome`.
    pass


def obter_jogadores(jogo, nome):
    # Retorna o jogador com o nome indicado.
    #
    # Se last_digit par: retorna None se o jogador não existir..
    #
    # Se last_digit ímpar: retorna um dicionário vazio se o jogador não existir.
    pass


def obter_quadrante(grelha, num_quadrante):
    # Retorna uma coleção com todos os valores de um quadrante
    #
    # Se last_digit par: a coleção a retornar é um tuplo.
    #
    # Se last_digit ímpar: a coleção a retornar é uma lista.
    pass


def obter_linha(grelha, num_linha):
    # Retorna uma coleção com todos os valores da linha indicada.
    #
    # Se last_digit par: a coleção a retornar é um tuplo.
    #
    # Se last_digit ímpar: a coleção a retornar é uma lista.
    pass


def obter_coluna(grelha, num_coluna):
    # Retorna uma coleção com todos os valores da coluna indicada.
    #
    # Se last_digit par: a coleção a retornar é um tuplo.
    #
    # Se last_digit ímpar: a coleção a retornar é uma lista.
    pass


def verificar(colecao):
    # Retorna True se a coleção indicada tiver todos os valores de 1 a 4
    pass


def verificar_vitoria(jogo, nome):
    # Retorna True se a grelha estiver corretamente preenchida.
    pass


def iniciar_jogo(jogo, nome, grelha_inicial):
    # Deve criar a grelha inicial com os valores indicados na string `grelha_inicial.`
    #
    # Se last_digit par: guarda posições vazias como zero (0).
    #
    # Se last_digit ímpar: guarda posições vazias como None.
    pass


def colocar_numero(jogo, linha, coluna, numero):
    # Deve colocar o número indicado na localização indicada.
    #
    # `linha` é um número inteiro, entre 1 e 4.
    # `coluna` é uma letra, entre A e D.
    pass
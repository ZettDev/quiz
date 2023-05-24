score = 0

perguntas = [
    ["Qual é a capital do Brasil?", "a) São Paulo", "b) Rio de Janeiro", "c) Brasília", "d) Salvador", "3"],
    ["Qual é o maior planeta do sistema solar?", "a) Júpiter", "b) Marte", "c) Terra", "d) Saturno", "1"],
    ["Qual é o país com a maior população do mundo?", "a) Estados Unidos", "b) Rússia", "c) China", "d) Índia", "3"],
    ["Quem pintou a Mona Lisa?", "a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh", "d) Salvador Dalí", "1"],
    #...
    # Puxar essas perguntas do bd
]

def exibir_pergunta(pergunta):
    print(pergunta[0])
    for i in range(1, len(pergunta) - 1):
        print(pergunta[i])
    #número no fim da tupla = posição do botão correto que entrega bool ou resposta correta que tem que ser igual ao botão
    #resposta = botão pressionado (retorno pode ser bool ou número da resposta)
    #return resposta

# Fazer um jeito de mostrar apenas perguntas não respondidas, e gravar perguntas respondidas.
# perguntas = perguntas não respondidas (talvez guardar os indices das qual cada um ja respondeu)
for i, pergunta in enumerate(perguntas, start=1):
    print(f"Pergunta {i}:")
    resposta = exibir_pergunta(pergunta)
    print(resposta, pergunta[-1])
    
    if resposta == pergunta[-1]:
        score += 1
    else:
        pass

# pontuação final é: score/len(perguntas)

# Qual é a extensão de arquivo usada para scripts Python?
# a) .py
# b) .pt
# c) .pyt
# d) .px
# Resposta: a)

# O Python é uma linguagem de programação orientada a objetos?
# a) Verdadeiro
# b) Falso
# Resposta: a) Verdadeiro

# Qual dos seguintes métodos é usado para obter o comprimento de uma lista em Python?
# a) length()
# b) size()
# c) count()
# d) len()
# Resposta: d) len()

# O Python é uma linguagem compilada?
# a) Verdadeiro
# b) Falso
# Resposta: b) Falso

# O que é um dicionário em Python?
# a) Uma estrutura de dados que armazena pares de chave-valor.
# b) Um tipo de variável que armazena valores numéricos.
# c) Uma função embutida para ordenar listas.
# d) Um tipo de loop utilizado para repetir um bloco de código.
# Resposta: a) Uma estrutura de dados que armazena pares de chave-valor.

# Qual é o operador usado para concatenar duas strings em Python?
# a) +
# b) *
# c) /
# d) -
# Resposta: a) +

# O Python é uma linguagem interpretada?
# a) Verdadeiro
# b) Falso
# Resposta: a) Verdadeiro

# Qual é a instrução utilizada para interromper um loop em Python?
# Resposta: break

# O que é um loop "for" em Python?
# a) Um loop que repete um bloco de código enquanto uma condição é verdadeira.
# b) Um loop que executa um bloco de código um número específico de vezes.
# c) Um loop que verifica se uma condição é verdadeira antes de executar um bloco de código.
# d) Um loop que interage sobre os elementos de uma sequência (como uma lista) um por um.
# Resposta: d) Um loop que interage sobre os elementos de uma sequência (como uma lista) um por um.

# Qual caractere que, quando usando em uma string, é conhecido como "caractere de escape"?
# Resposta: \
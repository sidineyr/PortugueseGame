import random
import requests

# URL do dicionário online
url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"

# Faz o download do dicionário e o transforma em uma lista de palavras
response = requests.get(url)
palavras = response.content.decode("utf-8").split()

# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)

# Função para esconder uma letra aleatória da palavra
def esconder_letra(palavra):
    letra_escondida = random.choice(palavra)
    palavra_escondida = ""
    for letra in palavra:
        if letra == letra_escondida:
            palavra_escondida += "_"
        else:
            palavra_escondida += letra
    return (letra_escondida, palavra_escondida)

# Função principal do jogo
def jogar():
    # Escolhe uma palavra aleatória e esconde uma letra
    palavra = escolher_palavra()
    letra_escondida, palavra_escondida = esconder_letra(palavra)

    # Mostra a palavra escondida na tela
    print("Adivinhe a palavra: " + palavra_escondida)

    # Pede para o jogador digitar a letra escondida
    letra_digitada = input("Digite a letra que está faltando na palavra: ")

    # Verifica se a letra digitada está correta
    if letra_digitada == letra_escondida:
        print("Parabéns, você acertou!")
    else:
        print("Infelizmente você errou. A letra correta era " + letra_escondida)

# Executa o jogo
jogar()
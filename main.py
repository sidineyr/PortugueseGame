import random
import urllib.request
import tkinter as tk

# URL do dicionário online
url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"

# Faz o download do dicionário e o transforma em uma lista de palavras
with urllib.request.urlopen(url) as response:
    palavras_bytes = response.read()
    palavras_str = palavras_bytes.decode("utf-8")
    palavras = palavras_str.split()

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
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Jogo de Alfabetização")

    # Escolhe uma palavra aleatória e esconde uma letra
    palavra = escolher_palavra()
    letra_escondida, palavra_escondida = esconder_letra(palavra)

    # Cria os widgets na janela
    tk.Label(janela, text="Adivinhe a palavra:").pack()
    lbl_palavra = tk.Label(janela, text=palavra_escondida)
    lbl_palavra.pack()
    tk.Label(janela, text="Digite a letra que está faltando na palavra:").pack()
    entry_letra = tk.Entry(janela)
    entry_letra.pack()
    btn_verificar = tk.Button(janela, text="Verificar", command=lambda: verificar_letra(entry_letra.get(), letra_escondida, palavra, lbl_palavra))
    btn_verificar.pack()

    # Inicia a janela
    janela.mainloop()

# Função para verificar se a letra digitada está correta
def verificar_letra(letra_digitada, letra_escondida, palavra, lbl_palavra):
    if letra_digitada == letra_escondida:
        tk.messagebox.showinfo("Parabéns", "Você acertou!")
    else:
        tk.messagebox.showerror("Errou", "A letra correta era " + letra_escondida)
    letra_escondida, palavra_escondida = esconder_letra(palavra)
    lbl_palavra.config(text=palavra_escondida)

# Executa o jogo
jogar()
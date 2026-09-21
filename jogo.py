import tkinter as tk
from tkinter import messagebox
import os

# =========================
# CONFIGURAÇÕES
# =========================

pontos = 0
clique = 1

nivel = 0
pontos_por_evolucao = 1_000_000

preco_upgrade = 100

# =========================
# JANELA
# =========================

janela = tk.Tk()

janela.title("Clicker Evolution")
janela.geometry("600x700")
janela.configure(bg="#202020")
janela.resizable(False, False)

# =========================
# SPRITES
# =========================

sprites = [
    "sprite1.png",
    "sprite2.png",
    "sprite3.png",
    "sprite4.png",
    "sprite5.png"
]

imagens = []

# Pega a pasta onde o jogo.py está
pasta_jogo = os.path.dirname(os.path.abspath(__file__))

try:
    for sprite in sprites:
        caminho = os.path.join(pasta_jogo, sprite)

        if not os.path.exists(caminho):
            raise FileNotFoundError(
                f"Imagem não encontrada:\n\n{caminho}"
            )

        imagens.append(tk.PhotoImage(file=caminho))

except Exception as erro:
    messagebox.showerror(
        "Erro ao carregar sprites",
        str(erro)
    )

    janela.destroy()
    raise SystemExit


# =========================
# FUNÇÕES
# =========================

def clicar():
    global pontos, nivel

    pontos += clique

    # Calcula a evolução
    novo_nivel = pontos // pontos_por_evolucao

    # Não ultrapassa o sprite 5
    novo_nivel = min(novo_nivel, len(imagens) - 1)

    # Se mudou de sprite
    if novo_nivel != nivel:
        nivel = novo_nivel
        atualizar_sprite()

    atualizar_tela()


def atualizar_sprite():
    botao.config(
        image=imagens[nivel]
    )


def comprar_upgrade():
    global pontos, clique, preco_upgrade

    if pontos >= preco_upgrade:

        pontos -= preco_upgrade

        # Aumenta pontos por clique
        clique += 1

        # Aumenta preço do próximo upgrade
        preco_upgrade = int(preco_upgrade * 1.5)

        atualizar_tela()

    else:
        print("Pontos insuficientes!")


def atualizar_tela():

    pontos_label.config(
        text=f"Pontos: {pontos:,}"
    )

    clique_label.config(
        text=f"+{clique} ponto(s) por clique"
    )

    nivel_label.config(
        text=f"Sprite: {nivel + 1}/5"
    )

    upgrade_button.config(
        text=f"Upgrade\nPreço: {preco_upgrade:,}"
    )


# =========================
# TÍTULO
# =========================

titulo = tk.Label(
    janela,
    text="CLICKER EVOLUTION",
    font=("Arial", 30, "bold"),
    fg="white",
    bg="#202020"
)

titulo.pack(pady=20)


# =========================
# PONTOS
# =========================

pontos_label = tk.Label(
    janela,
    text="Pontos: 0",
    font=("Arial", 25, "bold"),
    fg="white",
    bg="#202020"
)

pontos_label.pack()


clique_label = tk.Label(
    janela,
    text="+1 ponto(s) por clique",
    font=("Arial", 16),
    fg="#00ff88",
    bg="#202020"
)

clique_label.pack(pady=5)


nivel_label = tk.Label(
    janela,
    text="Sprite: 1/5",
    font=("Arial", 16),
    fg="#ffd700",
    bg="#202020"
)

nivel_label.pack(pady=5)


# =========================
# SPRITE / BOTÃO
# =========================

botao = tk.Button(
    janela,
    image=imagens[0],
    command=clicar,
    borderwidth=0,
    highlightthickness=0,
    bg="#202020",
    activebackground="#202020"
)

botao.pack(pady=30)


# =========================
# LOJA
# =========================

loja = tk.Label(
    janela,
    text="🛒 LOJA",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#202020"
)

loja.pack(pady=10)


upgrade_button = tk.Button(
    janela,
    text="Upgrade\nPreço: 100",
    command=comprar_upgrade,
    font=("Arial", 15, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    width=20,
    height=3
)

upgrade_button.pack(pady=10)


# =========================
# INICIA O JOGO
# =========================

atualizar_tela()
atualizar_sprite()

janela.mainloop()

import tkinter as tk

# =========================
# CONFIGURAÇÕES
# =========================

pontos = 0
clique = 1

# Cada sprite evolui a cada 1 milhão
nivel = 0
pontos_por_evolucao = 1_000_000

# Preço do upgrade
preco_upgrade = 100

# =========================
# SPRITES
# =========================

# Coloque essas imagens na mesma pasta do jogo.py
sprites = [
    "poke.png",
    "great.png",
    "ultra.png",
    "love.png",
    "master.png"
]

imagens = []

for sprite in sprites:
    imagens.append(tk.PhotoImage(file=sprite))


# =========================
# FUNÇÕES
# =========================

def clicar():
    global pontos, nivel

    pontos += clique

    # Descobre qual deveria ser o nível
    novo_nivel = pontos // pontos_por_evolucao

    # Se o jogador evoluiu
    if novo_nivel > nivel:
        nivel = novo_nivel

        # Não passa do último sprite disponível
        if nivel >= len(imagens):
            nivel = len(imagens) - 1

        atualizar_sprite()

    atualizar_tela()


def atualizar_sprite():
    botao.config(image=imagens[nivel])


def comprar_upgrade():
    global pontos, clique, preco_upgrade

    if pontos >= preco_upgrade:
        pontos -= preco_upgrade

        # Aumenta os pontos por clique
        clique += 1

        # Aumenta o preço do próximo upgrade
        preco_upgrade = int(preco_upgrade * 1.5)

        atualizar_tela()


def atualizar_tela():
    pontos_label.config(
        text=f"Pontos: {pontos:,}"
    )

    clique_label.config(
        text=f"+{clique} ponto(s) por clique"
    )

    nivel_label.config(
        text=f"Evolução: {nivel + 1}"
    )

    upgrade_button.config(
        text=f"Upgrade\nPreço: {preco_upgrade:,}"
    )


# =========================
# JANELA
# =========================

janela = tk.Tk()

janela.title("Clicker Evolution")
janela.geometry("600x700")
janela.configure(bg="#202020")


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
    text="Evolução: 1",
    font=("Arial", 16),
    fg="#ffd700",
    bg="#202020"
)

nivel_label.pack(pady=5)


# =========================
# BOTÃO / SPRITE
# =========================

botao = tk.Button(
    janela,
    image=imagens[0],
    command=clicar,
    borderwidth=0,
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
    width=20,
    height=3
)

upgrade_button.pack(pady=10)


# =========================
# INICIA O JOGO
# =========================

atualizar_tela()

janela.mainloop()

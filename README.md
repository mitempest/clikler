# clikler
# Clicker de Pokébolas

## Integrantes da Equipe

*  Miguel Henrique de Souza Caetano
*  Maryane Cristina Bruno

## Tema Escolhido

O tema escolhido para o projeto é Pokébolas, inspirado no estilo dos jogos de captura de criaturas. O projeto consiste em um jogo do gênero Clicker, no qual o jogador deve clicar em uma Pokébola para acumular pontos e evoluir dentro do jogo.

## Objetivo do Sistema

O objetivo do sistema é desenvolver um jogo simples e interativo utilizando Python, permitindo que o jogador acumule pontos através de cliques, compre melhorias e avance por diferentes níveis de evolução.

O projeto também tem como objetivo colocar em prática conhecimentos de programação, como:

* Variáveis;
* Funções;
* Estruturas condicionais;
* Operadores matemáticos;
* Interface gráfica;
* Manipulação de imagens;
* Sistema de pontuação;
* Sistema de upgrades.

## Breve Descrição do Funcionamento

O jogo possui uma interface gráfica desenvolvida utilizando a biblioteca Tkinter.

Ao iniciar o jogo, o jogador encontra uma Pokébola na tela. Cada vez que o jogador clica nela, recebe uma determinada quantidade de pontos.

Inicialmente, cada clique fornece 1 ponto.

Os pontos acumulados são exibidos na tela e podem ser utilizados para comprar upgrades na loja.

## Sistema de Pontos

Os pontos aumentam conforme o jogador clica na Pokébola.

Exemplo:

```text
Pontos: 100
+1 ponto(s) por clique
```

## Sistema de Evolução

Conforme o jogador acumula pontos, a imagem apresentada na tela muda, representando a evolução dentro do jogo.

O projeto possui 5 sprites diferentes.

O sistema verifica automaticamente a quantidade de pontos do jogador. Quando uma determinada quantidade é alcançada, o sprite é alterado para o próximo nível.

## Sistema de Upgrade

O jogo possui uma loja onde o jogador pode comprar upgrades.

O primeiro upgrade custa 100 pontos.

Ao comprar um upgrade:

* Os pontos necessários são descontados;
* A quantidade de pontos recebidos por clique aumenta;
* O preço do próximo upgrade aumenta.

Por exemplo:

```text
Upgrade
Preço: 100
```

Depois da compra:

```text
+2 pontos por clique
Upgrade
Preço: 150
```

Dessa forma, o jogador precisa continuar acumulando pontos para conseguir comprar melhorias cada vez mais caras.

## Tecnologias Utilizadas

* Python
* Tkinter
* Git
* GitHub

## Estrutura do Projeto

```text
Clicker-de-Pokebolas/
│
├── jogo.py
├── sprite1.png
├── sprite2.png
├── sprite3.png
├── sprite4.png
├── sprite5.png
└── README.md
```

## Como Executar

1. Instale o Python no computador.
2. Baixe ou clone o repositório.
3. Certifique-se de que os arquivos das imagens estejam na mesma pasta do arquivo `jogo.py`.
4. Execute o arquivo:

```bash
python jogo.py
```

5. A janela do jogo será aberta.
.




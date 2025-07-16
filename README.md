# Termo AI Solver

Este é um projeto de uma Inteligência Artificial desenvolvida em Python para resolver o jogo **Termo**. A IA utiliza uma abordagem heurística para maximizar suas chances de acertar a palavra secreta em menos de 6 tentativas.

## - Funcionalidades Principais

* **Resolvedor Automático**: A IA joga o jogo de forma autônoma, fazendo escolhas inteligentes a cada rodada.
* **Decisão Baseada em Heurística**: Utiliza uma heurística de frequência de letras para escolher a palavra que provavelmente fornecerá mais informações, reduzindo drasticamente o número de possibilidades. Pode também utilizar o método guloso, para tentar acertar as palavras diretamente.
* **Análise de Desempenho**: O script `loop.py` executa uma simulação (por padrão, 100 jogos) e calcula a taxa de acerto da IA, permitindo avaliar a eficácia do algoritmo.
* **Código Modular**: O projeto é organizado em módulos com responsabilidades claras (lógica da IA, sorteio de palavras, laço do jogo).

## - Como a IA Funciona?

A IA implementa um **algoritmo de busca com poda e uma heurística inteligente** para tomar suas decisões. O processo a cada rodada é o seguinte:

1.  **Primeira Tentativa**: A IA começa com uma palavra inicial otimizada (como "áureo"), que contém letras comuns e vogais para maximizar a chance de obter dicas logo de cara.

2.  **Poda do Espaço de Busca**: Após cada tentativa, a IA recebe o feedback do jogo:
    * `!` (letra certa no lugar certo)
    * `?` (letra certa no lugar errado)
    * `#` (letra não existe na palavra)

    Com base nesse feedback, ela filtra sua lista de várias de palavras (`palavras_possiveis`), **eliminando todas aquelas que não se encaixam mais nas dicas obtidas**. Esse processo é chamado de **poda**.

3.  **Escolha Heurística**: Com a lista de palavras possíveis já reduzida, a IA precisa decidir qual será a próxima jogada. Em vez de simplesmente chutar a primeira palavra da lista, ela aplica uma **heurística de frequência de letras**:
    * Ela analisa todas as palavras que ainda são candidatas a resposta e calcula a frequência de cada letra do alfabeto dentro dessa lista.
    * Em seguida, ela pontua palavras (candidatas ao chute) com base nas letras que elas contêm. Palavras com letras de alta frequência recebem uma pontuação maior.
    * A palavra com a maior pontuação é escolhida como a próxima tentativa. Essa abordagem garante que o chute tenha a maior probabilidade de revelar novas informações e reduzir ao máximo a lista de possibilidades para a rodada seguinte.

## - Como Usar

Para executar a simulação e ver a IA em ação, siga os passos abaixo.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Aliragm/termo_AI.git](https://github.com/Aliragm/termo_AI.git)
    ```

2.  **Navegue até o diretório:**
    ```bash
    cd termo_AI
    ```

3.  **Prepare o dicionário:**
    Certifique-se de que o arquivo `palavras_comuns.txt` ou `palavras_5letras.txt` está no mesmo diretório. Ele deve conter uma lista de palavras de 5 letras válidas em português, uma por linha.

4.  **Execute a simulação:**
    ```bash
    python loop.py
    ```

O script executará 100 jogos com a IA e, ao final, imprimirá a taxa de acertos e outras informações sobre o desempenho.

## - Estrutura do Projeto

* **`loop.py`**: O arquivo principal que executa o laço do jogo. Ele controla as rodadas, chama a IA para fazer uma jogada e calcula as estatísticas de vitória no final.
* **`IA.py`**: O cérebro do projeto. Contém toda a lógica de decisão da IA, incluindo a implementação da poda e decisão gulosa (greedy) de escolha de palavras.
* **`IAH.py`**: Mesma coisa, porém, com heurística implementada, ao invés do método guloso.
* **`sorteio.py`**: Utilitário responsável por sortear a palavra secreta do arquivo `palavras_comuns.txt` e por verificar se uma palavra existe no dicionário.
* **`palavra.py`**: Gerencia a entrada de palavras e sua normalização (como a remoção de acentos).
* **`palavras_comuns.txt`**: O dicionário de palavras utilizado tanto para sortear a palavra secreta quanto para a IA consultar as palavras possíveis.
* **`palavras_5letras.txt`**: Mesma coisa, porém com muito mais instâncias e palavras quase nunca utilizadas. Muito maior que o comum.
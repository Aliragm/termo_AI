# Termo AI Solver

Este é um projeto de uma Inteligência Artificial desenvolvida em Python para resolver o jogo **Termo** (semelhante ao Wordle). A IA utiliza estratégias baseadas em **busca com heurística** para maximizar as chances de acertar a palavra secreta em menos de 6 tentativas.

---

## ✅ Objetivos e Aplicações do Modelo e Dataset

**Objetivo do modelo:**  
Desenvolver um agente inteligente capaz de jogar o jogo Termo de forma autônoma, utilizando estratégias que minimizem o número de tentativas.

**Aplicações:**  
- Desenvolvimento de algoritmos de IA aplicados a jogos de palavras.  
- Demonstração prática de heurísticas e poda em problemas combinatórios.  
- Ferramenta para analisar estratégias ótimas em jogos com espaço de busca limitado.

**Dataset:**  
- O agente utiliza os arquivos `palavras_comuns.txt` e `palavras_5letras.txt`, contendo listas de palavras válidas em português.  
- Esses datasets são usados tanto para sortear a palavra secreta quanto para gerar a lista de candidatos que a IA utilizará durante o jogo.

---

## ✅ Algoritmos Utilizados

- **Busca com Poda:**  
  Após cada tentativa, a IA filtra a lista de palavras com base no feedback (`!`, `?`, `#`), eliminando palavras incompatíveis.

- **Heurística de Frequência de Letras:**  
  A IA calcula a frequência das letras nas palavras candidatas restantes e seleciona a palavra com maior pontuação para a próxima tentativa.

- **Método Guloso (Greedy):**  
  Alternativa à heurística, tenta acertar diretamente uma das palavras restantes com base nas dicas.

---

## ✅ Modelagem PEAS

- **P (Performance):** Taxa de acerto, número médio de tentativas.  
- **E (Environment):** Jogo Termo, com conjunto fixo de palavras e feedback por tentativa.  
- **A (Actuators):** Envio de palavras como tentativas.  
- **S (Sensors):** Feedback recebido após cada tentativa (!, ?, #).

---

## ✅ Arquitetura do Agente

- **Tipo de Agente:** Agente orientado a objetivos com busca heurística.

- **Componentes:**
  - **Base de Conhecimento:** Lista de palavras possíveis.
  - **Módulo de Percepção:** Interpreta o feedback do jogo.
  - **Módulo de Decisão:** Escolhe a próxima palavra com base em heurística ou estratégia gulosa.
  - **Executor:** Envia a palavra e coleta o feedback.

---

## ✅ Métricas de Avaliação, Desempenho e Validação

- **Taxa de acerto:** Percentual de jogos vencidos em até 6 tentativas.  
- **Número médio de tentativas:** Média das tentativas por jogo.  
- **Validação:** Executada com o script `loop.py`, que realiza 100 simulações automáticas e calcula estatísticas de desempenho.

---

## ✅ Limitações e Dificuldades

- **Dependência do dataset:** A IA não pode acertar palavras ausentes no dicionário.  
- **Falta de contexto linguístico:** A estratégia é puramente estatística.  
- **Complexidade com grandes volumes:** Dicionários maiores impactam o desempenho de execução.

---

## ✅ Limitações da Arquitetura

- **Não adaptativa:** O agente não aprende com erros passados.  
- **Heurística simples:** Baseada apenas na frequência de letras, sem análise semântica ou fonológica.

---

## ✅ Sugestões de Melhorias

- Aplicar **aprendizado de máquina supervisionado** ou **reforçado**.  
- Usar **modelos probabilísticos** para refinar a escolha de palavras.  
- Melhorar a performance com **estruturas de dados otimizadas**.  
- Criar uma **interface gráfica** para visualização do processo da IA.

---

## ✅ Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Aliragm/termo_AI.git
   cd termo_AI

2. Prepare o dicionário:
Certifique-se de que palavras_comuns.txt ou palavras_5letras.txt está no mesmo diretório.

3. Execute a simulação:

```bash
   python loop.py

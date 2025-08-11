## 📅 Day 49 - Implementando uma pilha de dados (stack)

### 🧩 Desafio 
- Implementar uma stack

#### `O que é uma stack?`
Uma stack é uma estrutura de dados que segue o princípio LIFO (Last In, First Out) — ou seja, o último elemento que entra é o primeiro que sai.
Pense numa pilha de pratos: você coloca um prato em cima (push) e tira sempre o de cima (pop).

📌 Operações principais:

- push(item) → adiciona um elemento no topo da pilha
- pop() → remove e retorna o elemento do topo
- peek() → retorna o elemento do topo sem remover
- is_empty() → verifica se a pilha está vazia
- size() → retorna o tamanho da pilha

Como isso funciona internamente?
1. Estamos usando uma lista (self.items) como estrutura base.
2. O append adiciona no final da lista (topo da pilha).
3. O pop remove do final da lista (último inserido).


## 📅 Day 52 - Linked Lists  

### 🧩 Desafio  
Implementar uma **lista ligada (Linked List)** em Python, com operações básicas como inserir, exibir e remover nós.  

### 📚 Aprendizados  
- **O que é uma Linked List**:  
  Uma lista ligada é uma estrutura de dados linear onde cada elemento (nó) contém:  
  - Um **valor** (dado).  
  - Uma **referência (ponteiro)** para o próximo nó da lista.  

- **Diferença de listas comuns em Python**:  
  - Listas (`list`) são armazenadas de forma **contígua** na memória.  
  - Linked Lists são **dinâmicas**, cada nó aponta para o próximo, e não exigem memória contínua.  

- **Tipos**:  
  - **Singly Linked List** → cada nó aponta apenas para o próximo.  
  - **Doubly Linked List** → cada nó aponta para o próximo **e** para o anterior.  

- **Vantagens**:  
  - Inserções e remoções são rápidas (O(1)) se tivermos a referência do nó.  
- **Desvantagens**:  
  - Acesso é mais lento, pois precisamos percorrer os nós sequencialmente (O(n)). 

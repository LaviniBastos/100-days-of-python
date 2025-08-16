from collections import deque 

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        # Adiciona um elemento ao final da fila.
        self.items.append(item)
        print (f"Adicionado: {item}")

    def dequeue(self):
        # "Vai remover o primeiro elemento da fila"
        if not self.is_empty():
            item = self.items.popleft()
            print(f"Item removido: {item}")
            return item
        print("A Fila está vazia!")
        return None

    def peek(self):
        #Irá retornar o primeiro elemento sem remover
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        #Irá retornar o tamanho da fila
        return len(self.items)



fila = Queue()
fila.enqueue("amada 1")
fila.enqueue("amada 2")
fila.enqueue("amada 3")


print("Primeiro da fila: ", fila.peek())
fila.dequeue()
fila.dequeue()
print("Tamanho da fila:", fila.size())
fila.dequeue()

fila.dequeue()

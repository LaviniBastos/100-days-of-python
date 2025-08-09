class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        # Essa função adiciona um item no topo da pilha
        self.items.append(item)
        
    def pop(self):
        # Essa função remove e retorna o item do topo da pilha
        if self.is_empty():
            raise IndexError("Pop da pilha está vazio")
        return self.items.pop()
    
    def peek(self):
        # Essa função retorna o item do topo sem revove-lo
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        # Essa função irá verificar se a pilha está vazia
        return len(self.items) == 0
    
    def size(self):
        # Essa função retornará a quantidade de elementos na pilha
        return len(self.items)
    
    
    
    
stack = Stack()

stack.push(20)
stack.push(90)
stack.push(50)     

print("Topo da pilha: ", stack.peek())
print("Tamanho: ", stack.size())


print("Removendo: ", stack.pop())
print("Topo novo: ", stack.peek())
print("A pilha se encontra vazia no momento? ", stack.is_empty())
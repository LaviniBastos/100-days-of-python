class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

#Definindo a Linked List

class LinkedLi:
    def __init__(self):
        self.head = None

    #Insere no final
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    #exibir a lista
    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def remover(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current:
            prev.next = current.next



lista = LinkedLi()
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(90)

print(" Primeira lista: ")
lista.show()

print("\nRemovendo 30...")
lista.remover(30)

print("Lista atual")
lista.show()
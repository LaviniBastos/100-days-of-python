class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Irá inserir um vlor na árvore
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def search(self, value):
        #Busca um valor na árvore
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True 
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def inorder(self):
        # Percorre a árvore em ordem crescente
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.value)
            self._inorder(current.right, result)

bst = BinarySearchTree()
valores = [50, 10, 20, 40, 90, 100, 150]
for v in valores:
    bst.insert(v)

print("Busca 90: ", bst.search(90))
print("Busca 80: ", bst.search(80))
print("In-order traversal:", bst.inorder())
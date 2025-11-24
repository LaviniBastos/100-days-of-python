class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        #verificando se a chavejá existe
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return v
            
        bucket.append((key, value))


    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
            return None
        
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
            return False
        

hashT = HashTable()


hashT.put("nome", "Alex")
hashT.put("idade", "32")
hashT.put("Profissão", "Professor")

print(hashT.get("nome"))
print(hashT.get("Profissão"))
print(hashT.get("idade"))

hashT.remove("Profissão")

print(hashT.get("Profissão"))
import hashlib

class HashTable:
    def __init__(self):
        self.hash_table = [0 for i in range(8)]
        
    def get_key(self, data):
        hash_convert = hashlib.sha256()
        hash_convert.update(data.encode())
        return int(hash_convert.hexdigest(), 16)
    
    def hash_function(self, key):
        return key % len(self.hash_table)
    
    def save(self, data, value):
        key = self.get_key(data)
        hash_value = self.hash_function(key)
        
        if self.hash_table[hash_value] != 0:
            for index in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][index][0] == key:
                    self.hash_table[hash_value][index][1] == value
                    return
                
            self.hash_table[hash_value].append([key, value])
        else:
            self.hash_table[hash_value] = [[key, value]]
            
    def read(self, data):
        key = self.get_key(data)
        hash_value = self.hash_function(key)
        
        if self.hash_table[hash_value] != 0:
            for index in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][index][0] == key:
                    self.hash_table[hash_value][index][1]
            return None
        
        else:
            return None
                
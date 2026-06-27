class MyHashMap:

    def __init__(self):
        self.tableSize = 1000
        self.buckets = [[]* i for i in range(self.tableSize)]
    
    def _hash_calc(self , key):
        return key % self.tableSize

    def put(self, key: int, value: int) -> None:
        index = self._hash_calc(key)
        bucket = self.buckets[index]

        for  i , (k , v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key , value)
                return None
        bucket.append((key , value))
        return None


    def get(self, key: int) -> int:
        index = self._hash_calc(key)
        bucket = self.buckets[index]
        for  i , (k , v) in enumerate(bucket):
            if k == key:
                return v
        return -1 

    def remove(self, key: int) -> None:
        index = self._hash_calc(key)
        bucket = self.buckets[index]
        for  i , (k , v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                print(bucket)
        return None
            

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
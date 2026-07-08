class MyHashSet:

    def __init__(self):
        self.size = 100
        self.buckets = [[0] * i for i in range(self.size)]

    def __hash_calc__(self , key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.__hash_calc__(key)
        bucket = self.buckets[index]
        for num in bucket:
            if num == key:
                return None
        bucket.append(key)

    def remove(self, key: int) -> None:
        index = self.__hash_calc__(key)
        bucket = self.buckets[index]
        for num in bucket:
            if num == key:
                bucket.remove(num)
        return None
        
    def contains(self, key: int) -> bool:
        index = self.__hash_calc__(key)
        bucket = self.buckets[index]
        for num in bucket:
            if num == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
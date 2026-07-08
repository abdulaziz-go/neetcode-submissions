class ListNode:
    def __init__(self , key):
        self.key = key 
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [ListNode(0) for i in range(self.size)]
    
    def __hash_calc__(self , key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self.__hash_calc__(key)
        dummy = self.buckets[idx]

        while dummy.next:
            if dummy.next.key == key:
                return
            dummy = dummy.next
        dummy.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = self.__hash_calc__(key)
        dummy = self.buckets[idx]

        while dummy.next:
            if dummy.next.key == key:
                dummy.next=dummy.next.next
                return 
            dummy = dummy.next
        

    def contains(self, key: int) -> bool:
        idx = self.__hash_calc__(key)
        dummy = self.buckets[idx]

        while dummy.next:
            if dummy.next.key == key:
                return True
            dummy = dummy.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
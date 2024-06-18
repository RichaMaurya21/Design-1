# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
'''Initiallised a List 'result', Checked if Key is not present, then add that Key in (add method)
if Key is present, then remove it for (remove method), 
similary return True when Key is present otherwise return False in (contains method)'''
class MyHashSet:

    def __init__(self):
        self.result = []

    def add(self, key: int) -> None:
        if key not in self.result:
            self.result.append(key)

    def remove(self, key: int) -> None:
        if key in self.result:
            self.result.remove(key)
    
    def contains(self, key: int) -> bool:
        if key in self.result:
            return True
        return False
        



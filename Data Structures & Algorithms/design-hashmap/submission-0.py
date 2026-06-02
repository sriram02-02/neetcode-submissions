class MyHashMap:

    def __init__(self):
        self.data=[]
        self.val=[]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.val[self.data.index(key)]=value
        else:
            self.val.append(value)
            self.data.append(key)

    def get(self, key: int) -> int:
        if key in self.data:
            return self.val[self.data.index(key)]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.data:
            if self.val[self.data.index(key)] in self.val:
                self.val.remove(self.val[self.data.index(key)])
            self.data.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
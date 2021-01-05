class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.map_counter = 0
        self.recent_key_stack = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            return self.map[key]
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value
        self.recent_key_stack.append(key)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
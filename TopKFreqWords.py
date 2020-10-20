from heapq import *

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        class MaxHeapObj(object):
            def __init__(self, val, word): 
                self.val = val
                self.word = word; 
            def __lt__(self, other): 
                if self.word == other.word:
                    self.val +=1
                if self.val > other.val:
                    return True
                elif  self.val == other.val:
                    return self.word > other.word
                return False
            def __eq__(self, other): 
                return self.word == other.word
            def __str__(self): return self.word + str(self.val)
            def __repr__(self): return self.word + str(self.val)
        h = []
        for word in words:
            if MaxHeapObj(val=1,word=word) not in h:
                heappush(h,MaxHeapObj(val=1,word=word))
            else:
                
        print(h)

s = Solution()
print(s.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],k=2))
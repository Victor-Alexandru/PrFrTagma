class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {}
        count = 1
        for char in order:
            order_map[char] = count
            count+=1

        def compare_strings(s1,s2):
            s1_len = len(s1)
            s2_len = len(s2)
            for i in range(0,min(s1_len,s2_len)):
                if order_map[s1[i]] < order_map[s2[i]]:
                    return 1
                elif order_map[s1[i]] == order_map[s2[i]]:
                    continue
                elif order_map[s1[i]] > order_map[s2[i]]:
                    return -1
            
            if s1_len > s2_len:
                return -1

            return 1

        for i in range(0,len(words)-1):
            if compare_strings(words[i],words[i+1])  == -1:
                return False

        return True
        







words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

s = Solution()
print(s.isAlienSorted(words,order))
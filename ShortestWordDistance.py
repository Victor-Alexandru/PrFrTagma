class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minDist = 9999999
        currentDist = 0
        weHaveWord = False
        
        for word in words:
            if word == word1:    
                weHaveWord = True
                currentDist = 1
                continue
            if word == word2 and weHaveWord:
                if currentDist < minDist:
                    minDist = currentDist
            currentDist += 1

        weHaveWord = False
        for word in words:
            if word == word2:
                weHaveWord = True
                currentDist = 1
                continue

            if word == word1 and weHaveWord:
                if currentDist < minDist:
                    minDist = currentDist

            currentDist += 1


            
            
        return minDist

S = Solution()

S.shortestDistance(words = ["practice", "makes", "perfect", "coding", "makes"],word1="makes",word2="coding")
class Solution(object):
    def wordBreak(self, s, wordDict):
        print(s,wordDict)
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        global_solution = []

        def segmentation(word,partial_sentence):
            if word == "":
                global_solution.append(partial_sentence[:len(partial_sentence)])

            for elem in wordDict:
                if word.startswith(elem): 
                    segmentation(word[len(elem):],partial_sentence + elem + " ")

        
        segmentation(s,"")
        return global_solution


s = Solution()
print(s.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
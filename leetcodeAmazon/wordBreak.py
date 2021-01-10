class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
        def break_the_word(s):
            if s in memo:
                return memo[s]

            if s == "":
                return True
            

            ret = False
            for word in wordDict:
                if s.startswith(word):
                    ret = break_the_word(s[len(word):])
                    if ret:
                        return True

            memo[s] = ret


        return break_the_word(s)
#13 time limit exceeded
S = Solution()
print(S.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
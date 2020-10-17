class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_dict = {}

        def clean_word(word):
            rez = ""
            for s in word:
                if s.isalpha():
                    rez +=s
            return rez

        for word in paragraph.replace(","," ").split():
            t = clean_word(word.lower())
            if t not in banned:
                if t not in word_dict.keys():
                    word_dict[t] = 0
                else:
                    word_dict[t] += 1

        maxWord = ""
        maxOc = -1

        for key in word_dict.keys():
            if word_dict[key] > maxOc:
                maxWord = key
                maxOc = word_dict[key]

        return maxWord


s= Solution()
print(s.mostCommonWord(paragraph="a, a, a, a, b,b,b,c, c",banned=["a"]))
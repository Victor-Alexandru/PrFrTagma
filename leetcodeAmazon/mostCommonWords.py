class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = {}

        for banned_words in banned:
            words[banned_words] = -1

        paragraph.replace(","," ")
        paragraph.replace("."," ")
        paragraph = paragraph.lower()

        max_counter = 0
        max_word = ""
        for word in paragraph.split():
            if word in words.keys():
                if words[word]!=[-1]:
                    words[word]+=1
                    if words[word] > max_counter:
                        max_counter = words[word]
                        max_word = word
            else:
                words[word] = 0 


        

        return max_word
class Solution:
    def reorderLogFiles(self, logs):
        letterList = []
        digitList = []

        for i in logs:
            if i[-1].isalpha():
                letterList.append(i)
            else:
                digitList.append(i)

        letterList.sort(key=lambda x: tuple(x.split(" ", 1)[i] for i in [1, 0]))
        return letterList + digitList

s = Solution()
print(s.reorderLogFiles(logs=["j mo","5 m w","t q h","g 07","o 2 0"]))
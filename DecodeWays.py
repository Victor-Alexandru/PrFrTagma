'''
ewiqioe.py
awewq.py
kqkwdkwqkw.py
woqodqwoiqwoiwdqowdq.py
wqkklqwkdwqklwdklsdkldwklklwdq'wk
wdqkwdklwqklwqklwklqklwkwdkqw
klwklwkqkwkwdkmwdmwsmkdqmdwqkdwqlkd,dqwwqlklkq
dqlkdwlkwqlkwqklwmkwqmqkkrdweepokewmfkwemdlxkloiqwklkmefw.py
klfor i in range(0,len())
ewqwqe.py
'''

class Rez:
    def __init__(self):
        self.memoization = {}

    def split_the_number(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s)-1:
            return 1

        # Memoization is needed since we might encounter the same sub-string.
        if index in self.memoization:
            return self.memoization[index]

        ans = self.split_the_number(index+1, s) + (self.split_the_number(index+2, s) if (int(s[index : index+2]) <= 26) else 0)
        # Save for memoization
        self.memoization[index] = ans
        return ans

    def decode_routes(self, s: str) -> int:
        if not s:
            return 0
        return self.split_the_number(0, s)

            




s =  Rez()
print(s.decode_routes(s='123'))
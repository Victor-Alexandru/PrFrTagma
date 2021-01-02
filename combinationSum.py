class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    
        tabs = []
        for i in range (max(target+1,max(candidates)+1)):
            tabs.append([])

        for candidate in candidates:
            tabs[candidate].append([candidate])


        for i in range(1,len(tabs)):
            if tabs[i] !=[]:
                for tab in tabs[i]:
                    for candidate in candidates:
                        if i+candidate < len(tabs) and candidate >= tab[-1]:
                            tabs[i+candidate].append(tab+[candidate])

        return tabs[target]
        

s = Solution()
print(s.combinationSum(candidates=[2,3,6,7],target=7))
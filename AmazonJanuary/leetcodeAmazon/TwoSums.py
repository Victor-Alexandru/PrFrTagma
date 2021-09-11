class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_map = {}
        
        rez = []
        
        for i  in range(len(nums)):
            if nums[i] in numbers_map:
                numbers_map[nums[i]].append(i)
            else:
                numbers_map[nums[i]] = [i]


        for i  in range(len(nums)):
            if target-nums[i]==nums[i] and nums[i] in numbers_map.keys():
                if len(numbers_map[nums[i]]) >= 2:
                    rez.append(numbers_map[nums[i]][0])
                    rez.append(numbers_map[nums[i]][1])
                    break     
            
            elif target-nums[i]  in numbers_map.keys():
                rez.append(i)
                rez.append(numbers_map[target-nums[i]][0])
                break
    

        return rez

s = Solution()
print(s.twoSum(nums = [3,2,4], target = 6))

# 14 minute



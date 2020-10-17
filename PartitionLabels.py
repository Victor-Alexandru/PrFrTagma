class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        word_dict = {}
        index = 0 
        def are_two_intervals_intersectable(int1,int2):
            if int2[0] < int1[1] and int2[1] > int1[1]:
                return True
            
            if int1[0] < int2[1] and int1[1] > int2[1]:
                return True
            
            return False


        for s in S:
            if s not in word_dict.keys() :
                word_dict[s] = [index,index]
            else:
                word_dict[s][1] = index
            index += 1
        

        for key in word_dict.keys():
            for other_key in word_dict.keys():
                if key != other_key :
                    if word_dict[key][0] < word_dict[other_key][0] and word_dict[key][1] > word_dict[other_key][1]:
                        word_dict[other_key] =  [-1000,-1000]
        
        for key in word_dict.keys():
            for other_key in word_dict.keys():
                if key != other_key and word_dict[key][0] != -1000 and  word_dict[other_key][0] != -1000 :
                    if are_two_intervals_intersectable(word_dict[key],word_dict[other_key]):
                        word_dict[key][0] = min(word_dict[key][0],word_dict[other_key][0])
                        word_dict[key][1] = max(word_dict[key][1],word_dict[other_key][1])
                        word_dict[other_key] =  [-1000,-1000]
        result = [ (word_dict[key][1] - word_dict[key][0] + 1) for key in word_dict.keys() if word_dict[key][0] != -1000]
        
   

        return  result 
        
                
s = Solution()
print(s.partitionLabels(S="caedbdedda"))
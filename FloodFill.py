
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldValue = image[sr][sc]
        image[sr][sc] = newColor
        if newColor == oldValue : return image
        def floodAll(image, sr, sc, newColor,oldValue):
            if sc + 1 < len(image[0]) and image[sr][sc+1] == oldValue:
                image[sr][sc+1] = newColor   
                floodAll(image,sr,sc+1,newColor,oldValue)

            if sc - 1 >=  0 and image[sr][sc-1] == oldValue:
                image[sr][sc-1] = newColor    
                floodAll(image,sr,sc-1,newColor,oldValue)

            if sr - 1  >=  0 and image[sr-1][sc] == oldValue:
                image[sr-1][sc] = newColor    
                floodAll(image,sr-1,sc,newColor,oldValue)

            if sr + 1  < len(image) and image[sr+1][sc] == oldValue:
                image[sr+1][sc] = newColor    
                floodAll(image,sr+1,sc,newColor,oldValue)
            
        floodAll(image,sr,sc,newColor,oldValue)
            
        return image
 
s=Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
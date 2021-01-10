class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def expand(r,c,newColor,old_color): 
            if r < 0 or c < 0 or r >= len(image) or c>= len(image[0]):
                pass
            else:
                if old_color == image[r][c]:
                    image[r][c] = newColor
                    for offset_r,offset_c in [(1,0),(0,1),(-1,0),(0,-1)]:
                        expand(r+offset_r,c+offset_c,newColor,old_color) 

                    

        old_color = image[sr][sc]
        if old_color != newColor:
            expand(sr,sc,newColor,old_color)

        return image

# 17min
# Time: O(n)
# Space: O(n)
s = Solution()
print(s.floodFill(image =[[0,0,0],[0,1,1]],sr = 1, sc = 1, newColor = 1))
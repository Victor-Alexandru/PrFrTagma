The intuition behind this approach is that the area formed between the 
lines will always be limited by the height of the shorter line. Further, the farther the lines, 
the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a 
variable \text{maxarea}maxarea to store the maximum area obtained till now.
 At every step, we find out the area formed between them,
 update \text{maxarea}maxarea and move the pointer pointing to the shorter line towards the other end by one step.

The algorithm can be better understood by looking at the example below:

public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxarea;
    }
}
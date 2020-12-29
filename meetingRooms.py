class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms

#Time Complexity: O(N\log N)O(NlogN).

# There are two major portions that take up time here. One is sorting of the array that takes O(N\log N)O(NlogN) considering
#  that the array consists of NN elements.
# Then we have the min-heap. In the worst case, all NN meetings will collide with each other. In any case we have NN add operations on the heap. 
# In the worst case we will have NN extract-min operations as well.
#  Overall complexity being (NlogN)(NlogN) since extract-min operation on a heap takes O(\log N)O(logN).
# Space Complexity: O(N)O(N) because we construct the min-heap and that
#  can contain NN elements in the worst case as described above in the time complexity section. Hence, the space complexity is O(N)O(N).


# COmplexity Analysis

# Time Complexity: O(N\log N)O(NlogN) because all we are doing is sorting the two arrays for start timings and end timings individually and each of them would contain NN elements considering there are NN intervals.

# Space Complexity: O(N)O(N) because we create two separate arrays of size NN, one for recording the start times and one for the end times.
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        newnum = []

        for num in nums:

            heapq.heappush(newnum, num)

            if len(newnum) > k:
                heapq.heappop(newnum)

        return newnum[0]
            
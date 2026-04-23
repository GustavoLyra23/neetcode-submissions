class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0;
        maxSeq = 0;
        for number in nums:
            if number != 1:
                maxSeq = max(count, maxSeq)   
                count = 0
            elif number == 1:
               count = count + 1
        maxSeq = max(count, maxSeq)        
        return maxSeq
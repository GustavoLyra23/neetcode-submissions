class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        ans = []
        numsIndx = 0;
        for _ in range(numsLength * 2):
            if numsIndx == (numsLength):
                numsIndx = 0
            ans.append(nums[numsIndx])
            numsIndx += 1
        return ans       
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        arrLength = len(arr)
        for i in range(arrLength):
        #   if i == arrLength - 1:
        #     ans.append(-1)
        #     break 
          maxNumber = -1; 
          for j in range(i + 1,arrLength):
              maxNumber = max(maxNumber, arr[j])
          ans.append(maxNumber)        
        return ans
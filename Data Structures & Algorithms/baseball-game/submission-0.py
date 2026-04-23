class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        recordIdx = 0;
        for op in operations:
            match op:
               case "+":                   
                   record.append(record[-1] + record[-2])   
                   recordIdx += 1          
               case "D":
                   record.append(record[recordIdx - 1] * 2)
                   recordIdx += 1 
               case "C":
                   record.pop()
                   recordIdx -= 1     
               case _:
                    record.append(int(op))
                    recordIdx += 1             
        sum = 0;
        for num in record:
            sum += num
        return sum

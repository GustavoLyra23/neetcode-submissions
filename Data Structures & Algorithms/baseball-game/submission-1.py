class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        recordIdx = 0;
        sum = 0;
        for op in operations:
            match op:
               case "+":                   
                   val = record[-1] + record[-2]
                   record.append(val)
                   sum += val           
               case "D":
                   val = record[recordIdx - 1] * 2
                   record.append(val)
                   sum += val
               case "C":
                   val = record.pop()
                   recordIdx -= 1  
                   sum -= val
                   continue     
               case _:
                    val = int(op)
                    record.append(val)
                    sum += val;
            recordIdx += 1                     
        return sum

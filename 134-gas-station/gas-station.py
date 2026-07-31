class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1 and gas[0] == cost[0]:
            return 0
        i = 0
        while i < len(gas):
            if gas[i] <= cost[i]:
                i += 1
                continue
            else:
                fuel = 0
                for j in range(i,i+len(gas)):
                    index = j % len(gas)
                    fuel += gas[index]
                    fuel -= cost[index]
                    if fuel < 0:
                        i = index if j < len(gas) else i+1
                        break
                else:
                    return i
        return -1


        
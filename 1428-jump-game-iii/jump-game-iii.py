class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visit = set()
        next = [start]
        while next:
            if next[0] in visit:
                next.pop(0)
                continue
            visit.add(next[0])
            index = next.pop(0)
            if arr[index] == 0:
                return True
            left = index - arr[index]
            right = index + arr[index]
            if left >= 0:
                next.append(left)
            if right < len(arr):
                next.append(right)
        return False



        
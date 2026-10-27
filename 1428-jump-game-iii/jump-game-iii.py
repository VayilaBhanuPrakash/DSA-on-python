class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        next = [start]
        visit = set()
        pointer = 0
        while pointer < len(next):
            index = next[pointer]
            pointer += 1
            if arr[index] == 0:
                return True
            if index in visit:
                continue
            visit.add(index)
            left = index - arr[index]
            right = index + arr[index]
            if left >= 0:
                next.append(left)
            if right < len(arr):
                next.append(right)
        return False

        
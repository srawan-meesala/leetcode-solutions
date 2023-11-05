from collections import deque

class Solution:
    def getWinner(self, arr, k: int) -> int:
        max_element = max(arr)
        if k >= len(arr):
            return max_element
        arr = deque(arr)
        max_count = 0
        current_max = arr.popleft()
        while max_count < k:
            next_element = arr.popleft()
            if next_element > current_max:
                current_max = next_element
                max_count = 1
            else:
                max_count += 1
            arr.append(current_max)
        return current_max
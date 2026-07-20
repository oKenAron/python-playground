from typing import List
from collections import deque

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        tmp = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tmp.append(grid[i][j])
        for _ in range(k):
            tmp.appendleft(tmp.pop())
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = tmp.popleft()
        return grid

if __name__ == "__main__":
    solution = Solution()

    result_a =  solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1)
    result_b =  solution.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4)
    result_c =  solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],9)

    assert result_a == [[9,1,2],[3,4,5],[6,7,8]] , f"Error In Test Case A: {result_a}"
    assert result_b == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]] , f"Error In Test Case B: {result_b}"
    assert result_c == [[1,2,3],[4,5,6],[7,8,9]] , f"Error In Test Case C: {result_c}"

    print("All test cases passed!")

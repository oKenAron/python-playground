from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [round(celsius + 273.15, 5), round(celsius * 1.80 + 32.00, 5)]


if __name__ == "__main__":
    solution = Solution()

    assert solution.convertTemperature(36.50) == [309.65000, 97.70000]
    assert solution.convertTemperature(122.11) == [395.26000, 251.79800]
    print("All test cases passed!")

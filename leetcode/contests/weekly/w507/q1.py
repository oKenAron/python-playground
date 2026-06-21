class Solution:
    def maxDistance(self, moves: str) -> int:
        count_U = moves.count("U")
        count_D = moves.count("D")
        count_L = moves.count("L")
        count_R = moves.count("R")
        count_under = moves.count("_")

        confirmed_manhattan = abs(count_U - count_D) + abs(count_L - count_R)
        return count_under + confirmed_manhattan

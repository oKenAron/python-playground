class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        if m == 1 and n == 1:
            return []
        elif m == 1 or n == 1:
            if k != 1:
                return []
            elif m == 1:
                ans = ""
                for _ in range(n):
                    ans += "."
                return [ans]
            elif n == 1:
                ans = [[] for _ in range(m)]
                for _ in range(m):
                    ans.append(".")
                return ans
        elif k == 2:
            map = [[0 for _ in range(n)] for _ in range(m)]
            map[m - 1][n - 1] = 1
            map[m - 2][n - 1] = 1
            map[m - 1][n - 2] = 1
            map[m - 2][n - 2] = 1
            map[0][0] = 1
            if m - 2 > 0:
                for i in range(m - 2):
                    map[i][n - 2] = 1
                if n - 2 > 0:
                    for i in range(n - 2):
                        map[0][i] = 1
            else:
                for i in range(n - 2):
                    map[0][i] = 1
            ans = [[] for _ in range(m)]
            for i in range(m):
                ans[i] = ""
                for j in range(n):
                    ans[i] += "." if map[i][j] == 1 else "#"
            return ans
        elif k == 3 and m >= 3:
            map = [[0 for _ in range(n)] for _ in range(m)]
            map[m - 1][n - 1] = 1
            map[m - 2][n - 1] = 1
            map[m - 3][n - 1] = 1
            map[m - 1][n - 2] = 1
            map[m - 2][n - 2] = 1
            map[m - 3][n - 2] = 1
            map[0][0] = 1
            for i in range(m - 3):
                map[i][n - 2] = 1
            if n - 2 > 0:
                for i in range(n - 2):
                    map[0][i] = 1
            ans = [[] for _ in range(m)]
            for i in range(m):
                ans[i] = ""
                for j in range(n):
                    ans[i] += "." if map[i][j] == 1 else "#"
            return ans
        elif k == 3 and n >= 3:
            map = [[0 for _ in range(n)] for _ in range(m)]
            map[m - 1][n - 1] = 1
            map[m - 2][n - 1] = 1
            map[m - 1][n - 2] = 1
            map[m - 2][n - 2] = 1
            map[m - 1][n - 3] = 1
            map[m - 2][n - 3] = 1
            map[0][0] = 1
            for i in range(n - 3):
                map[0][i] = 1
            ans = [[] for _ in range(m)]
            for i in range(m):
                ans[i] = ""
                for j in range(n):
                    ans[i] += "." if map[i][j] == 1 else "#"
            return ans
        elif k == 4 and n >= 3 and m >= 3:
            map = [[0 for _ in range(n)] for _ in range(m)]
            map[m - 1][n - 1] = 1
            map[m - 2][n - 1] = 1
            map[m - 1][n - 2] = 1
            map[m - 2][n - 2] = 1
            map[m - 3][n - 2] = 1
            map[m - 2][n - 3] = 1
            map[m - 2][n - 3] = 1
            map[0][0] = 1
            for i in range(m - 3):
                map[i][n - 3] = 1
            if n - 3 > 0:
                for i in range(n - 3):
                    map[0][i] = 1
            ans = [[] for _ in range(m)]
            for i in range(m):
                ans[i] = ""
                for j in range(n):
                    ans[i] += "." if map[i][j] == 1 else "#"
            return ans
        elif k == 4 and n >= 3 and m == 2:
            map = [[0 for _ in range(n)] for _ in range(m)]
            map[m - 1][n - 1] = 1
            map[m - 2][n - 1] = 1
            map[m - 1][n - 2] = 1
            map[m - 2][n - 2] = 1
            map[m - 1][n - 3] = 1
            map[m - 2][n - 3] = 1
            map[m - 1][n - 4] = 1
            map[m - 2][n - 4] = 1
            map[0][0] = 1
            for i in range(n - 4):
                map[0][i] = 1
            ans = [[] for _ in range(m)]
            for i in range(m):
                ans[i] = ""
                for j in range(n):
                    ans[i] += "." if map[i][j] == 1 else "#"
            return ans
        elif k == 4 and n == 2:
            map = [[0 for _ in range(n)] for _ in range(m)]
            map[m - 1][n - 1] = 1
            map[m - 2][n - 1] = 1
            map[m - 3][n - 1] = 1
            map[m - 4][n - 1] = 1
            map[m - 1][n - 2] = 1
            map[m - 2][n - 2] = 1
            map[m - 3][n - 2] = 1
            map[m - 4][n - 2] = 1
            map[0][0] = 1
            for i in range(m - 4):
                map[i][0] = 1
            ans = [[] for _ in range(m)]
            for i in range(m):
                ans[i] = ""
                for j in range(n):
                    ans[i] += "." if map[i][j] == 1 else "#"
            return ans
        return []

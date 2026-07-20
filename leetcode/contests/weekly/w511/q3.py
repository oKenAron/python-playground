from typing import List

class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        length = len(s)
        count_0 = s.count("0")
        count_1 = length - count_0
        ans = [False for _ in strs]
        for i in range(len(strs)):
            counti_0 = strs[i].count("0")
            counti_1 = strs[i].count("1")
            mitei = length - counti_0 - counti_1
            if count_0 - counti_0 > mitei or count_1 - counti_0 > mitei:
                continue
            replace_count = 0
            for j in range(length):
                if s[j] != strs[i][j]:
                    if s[j] == "1" and strs[i][j] == "0":
                        replace_count += 1
                    if s[j] == "0" and strs[i][j] in :
                        replace_count -= 1
                    if replace_count < 0:
                        continue
            ans[i] = True

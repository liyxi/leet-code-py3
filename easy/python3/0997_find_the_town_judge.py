"""997. Find the Town Judge

Test case:
2
[[1,2]]
3
[[1,3],[2,3]]
3
[[1,3],[2,3],[3,1]]
3
[[1,2],[2,3]]
4
[[1,3],[1,4],[2,3],[2,4],[4,3]]

Retuls:
2
3
-1
-1
3
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = {}
        out_degree = {}
        for start, end in trust:
            in_degree[end] = in_degree.get(end, 0) + 1
            out_degree[start] = out_degree.get(start, 0) + 1
        cand = []
        for i in range(1, N+1):
            if in_degree.get(i, 0) == N - 1 and out_degree.get(i, 0) == 0:
                cand.append(i)
        return cand[0] if len(cand) == 1 else -1

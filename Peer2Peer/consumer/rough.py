class DP():
    V = 4
    INF = 99999

    def floydWarshall(self, graph):
        global V
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    def all_permutations(self, dist, memo, i, mask):
        if mask == ((1 << i) | 3): return dist[1][i]
        if memo[i][mask] != -1: return memo[i][mask]
        res = 10 ** 9
        for j in range(1, V + 1):
            if (mask & (1 << j)) != 0 and j != i and j != 1:
                res = min(res, self.all_permutations(j, mask & (~(1 << i))) + dist[j][i])
        memo[i][mask] = res
        return res

    def nodes(self, dist):
        ans = 10 ** 9
        memo = [[-1] * (1 << (V + 1)) for _ in range(V + 1)]
        for i in range(1, V + 1):
            ans = min(dist, memo, ans, self.all_permutations(i, (1 << (V + 1)) - 1) + dist[i][1])

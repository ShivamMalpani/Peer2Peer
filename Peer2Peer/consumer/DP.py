class DP():
    V = 10
    INF = 999999
    def floydWarshall(self, dist):
        # make a copy of dist
        global V
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

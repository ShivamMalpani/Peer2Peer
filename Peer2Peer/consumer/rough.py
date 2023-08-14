
class DP():

    def travelling_salesman(self, dist, memo, i, mask):
        # base case
        # if only ith bit and 1st bit is set in our mask,
        # it implies we have visited all other nodes already
        if mask == ((1 << i) | 3):
            return dist[1][i]

        # memoization
        if memo[i][mask] != -1:
            return memo[i][mask]
        res = 10 ** 9
        for j in range(1, n + 1):
            if (mask & (1 << j)) != 0 and j != i and j != 1:
                res = min(res, travelling_salesman(j, mask & (~(1 << i))) + dist[j][i])
        memo[i][mask] = res  # storing the minimum value
        return res

    def nodes(self):
        ans = 10**9
        dist = pass
        memo = pass
        for i in range(1, n+1):
            # try to go from node 1 visiting all nodes in between to i
            # then return from i taking the shortest route to 1
            ans = min(dist,memo,ans, travelling_salesman(i, (1 << (n+1))-1) + dist[i][1])
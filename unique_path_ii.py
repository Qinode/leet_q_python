class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

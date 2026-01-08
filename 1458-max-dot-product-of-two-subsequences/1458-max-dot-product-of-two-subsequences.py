class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18

        dp = [[NEG_INF] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]

                
                take = prod
                if i > 0 and j > 0:
                    take += max(0, dp[i-1][j-1])

                
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])

                dp[i][j] = max(dp[i][j], take)

        return dp[n-1][m-1]

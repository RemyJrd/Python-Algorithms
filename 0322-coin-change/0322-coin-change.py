class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(remain):
            if remain < 0:
                return float('inf')
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]

            min_count = float('inf')
            for coin in coins:
                count = dp(remain - coin)
                min_count = min(min_count, count + 1)

            memo[remain] = min_count
            return min_count

        result = dp(amount)
        return result if result != float('inf') else -1
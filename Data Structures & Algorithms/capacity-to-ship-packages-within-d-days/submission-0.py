class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            ships = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    ships += 1
                    current_load = 0
                current_load += w
            return ships <= days

        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_ship(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

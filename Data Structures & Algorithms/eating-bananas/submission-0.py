class Solution:

  def minEatingSpeed(self, piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right

    while left <= right:
      mid = (left + right) // 2

      total_hours = sum((p + mid - 1) // mid for p in piles)

      if total_hours <= h:
        res = mid
        right = mid - 1
      else:
        left = mid + 1

    return res

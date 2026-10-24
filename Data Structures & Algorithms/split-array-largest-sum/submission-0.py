class Solution:
  def splitArray(self, nums: List[int], k: int) -> int:
    def canSplit(largest: int) -> bool:
      subarray = 1
      curSum = 0
      for num in nums:
        if curSum + num > largest:
          subarray += 1
          curSum = num
          if subarray > k:
            return False
        else:
          curSum += num
      return True

    l, r = max(nums), sum(nums)
    res = r
    while l <= r:
      mid = l + (r - l) // 2
      if canSplit(mid):
        res = mid
        r = mid - 1
      else:
        l = mid + 1
    return res

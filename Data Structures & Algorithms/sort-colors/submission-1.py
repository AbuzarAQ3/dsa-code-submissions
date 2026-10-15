class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    # heap sort
    # T O(nlogn) S O(1)

        n = len(nums)
        def heapify(size: int, root: int) -> None:
            while True:
                largest = root
                left = 2 * root + 1
                right = 2 * root + 2

                if left < size and nums[left] > nums[largest]:
                    largest = left

                if right < size and nums[right] > nums[largest]:
                    largest = right

                if largest == root:
                    break

                nums[root], nums[largest] = nums[largest], nums[root]
                root = largest

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)

        return nums

    # bubble sort
    # T O(n^2) S O(1)

        n = len(nums)
        
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        
        return nums
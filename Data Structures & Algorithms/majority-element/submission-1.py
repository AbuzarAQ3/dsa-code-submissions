class Solution:
    def majorityElement(self, nums: List[int]) -> int:

    # oprimized Boore Moyer Algo
    # T O(n)
    # S O(1)    
        max_element = 0
        max_element_frequency = 0

        for num in nums:
            if max_element_frequency == 0:
                max_element = num
            max_element_frequency += 1 if max_element == num else -1
        return max_element


    # optimized hashmap approach
        max_element = 0
        max_elemement_frequency = 0
        element_by_frequency_hashmap = dict()
        
        for num in nums:
            element_by_frequency_hashmap[num] = 1 + element_by_frequency_hashmap.get(num, 0)
            if element_by_frequency_hashmap[num] > max_elemement_frequency:
                max_element = num
            else:
                max_element = max_element
            max_elemement_frequency = max(max_elemement_frequency, element_by_frequency_hashmap[num])
        return max_element

    # bruteforce
    # T O(n*2)
    # S O(1)
        n = len(nums)
        count = 0
        max_element_count = 0
        max_element = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
            if count > n/2:
                return nums[i]
            if count > max_element_count:
                max_element_count = count
                max_element = nums[i]
            count = 0
        return max_element

    # optimized package usage
        mx = Counter(nums).most_common(1)
        return mx[0][0]

    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    

    # optimized bucket sort approach
    # T O(n) S O(n)
        frequency_hashmap = {}
        hashmap_elements = [[] for i in range(len(nums)+1)]

        for num in nums:
            frequency_hashmap[num] = 1 + frequency_hashmap.get(num, 0)

        for num, count in frequency_hashmap.items():
            hashmap_elements[count].append(nums)

        max_freq_elements = []
        for i in range(len(hashmap_elements)-1, 0, -1):
            for num in hashmap_elements[i]:
                max_freq_elements.append(num)
                if len(max_freq_elements) == k:
                    break
                    
    # custom hashmap by frequency approach, slower
    # T O(m+k*n) S O(n)
        n = len(nums)
        frequency_hashmap = {}
        for num in nums:
            if num in frequency_hashmap:
                frequency_hashmap[num] += 1
            else:
                frequency_hashmap[num] = 1

        max_elements = []        
        for i in range(k):
            max_element = max(frequency_hashmap, key=frequency_hashmap.get)
            del frequency_hashmap[max_element]
            max_elements.append(max_element)
        return max_elements
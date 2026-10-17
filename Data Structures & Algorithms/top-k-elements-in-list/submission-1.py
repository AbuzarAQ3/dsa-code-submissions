class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    # 
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
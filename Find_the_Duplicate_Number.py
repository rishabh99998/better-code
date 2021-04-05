def findDuplicate(self, nums: List[int]) -> int:
        a = {}
        
        for j in nums:
            if j not in a:
                a[j] = 1
            else:
                return j
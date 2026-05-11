class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org_len = len(nums)
        #print(org_len)
        nums = set(nums)
        mod_len = len(nums)
        #print(mod_len)
        if org_len != mod_len:
            return True
        else:
            return False
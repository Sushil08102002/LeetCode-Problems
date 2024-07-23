
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Our target is the last index of the array
        our max_index is that index upto which we can reach from current index
        check weather current index able to reach to target or not if yes then
        return true else check other condition to get max_index
        '''
        target=len(nums)-1
        max_index=-1
        for i in range(len(nums)):
            if nums[i]+i>=target:
                return True
            max_index=max(max_index,nums[i]+i)
            if max_index==i:
                return False
        
def main():
    nums=list(map(int,input().split()))
    solution=Solution()
    jump=solution.canJump(nums)
    print(jump)

if __name__=="__main__":
    main()

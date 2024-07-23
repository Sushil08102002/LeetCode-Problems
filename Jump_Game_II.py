from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''We took three variables i.e 
        farthest = the maximum distance we can reach from visited indexes
        current = current farthest index or say the range upto which we
        visited
        jump = this is our final result means the minimum value of jump'''
        farthest=0
        current=0
        jump=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if(i==current):
                current=farthest
                jump+=1 
        return jump

def main():
    num=list(map(int,input().split()))
    solution=Solution()
    res=solution.jump(num)
    print(res)

if __name__=="__main__":
    main()


        
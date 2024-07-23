from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums=nums[::-1]
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1

        res=[]
        while dic:
            new_key=0
            new_value=1000000000
            for key,value in dic.items():
                if value<new_value:
                    new_value=value
                    new_key=key
            while new_value>0:
                res.append(new_key)
                new_value-=1
            del dic[new_key]
        return res
        
def main():
    nums = list(map(int,input().split()))
    solution=Solution()
    sorted_nums = solution.frequencySort(nums)
    print(sorted_nums)

if __name__ == "__main__":
    main()
    
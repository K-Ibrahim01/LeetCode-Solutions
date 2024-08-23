class Solution:
    def twoSum(self,array,target):
         num_to_index = {}
         for i , num in enumerate(array):
           complement = target-num
           if complement in num_to_index:
            return [num_to_index[complement],i]
           else:
            num_to_index[num]=i 
if __name__ == "__main__": 
    solution = Solution()           
    array=[1,2,3,4,5]
    target=9   
    result = solution.twoSum(array,target)
    print(result)        

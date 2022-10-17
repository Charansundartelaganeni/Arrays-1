#TC: O(n) 
#SC: O(n)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        
        result = [1]  #initialize result with value 1
        
        for i in range(1, len(nums)):  
            result.append(nums[i-1]*result[-1])  #append the values in nums by multiplying it with last value of result
            
           
            
        RP = 1  #initializze your running product as 1
        
        for i in range(len(result)-2,-1,-1):  #start from last second
            result[i] *= nums[i+1]*RP   # current result index is multiplied with nums val and running product
            RP *= nums[i+1]  #now running product is multiplied with next value of nums
            
        return result #return the result
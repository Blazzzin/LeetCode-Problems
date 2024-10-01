class Solution(object):
    def twoSum(self, nums, target): 

        foundSolution = False

        solutionIndices = []

        i = 0
        
        while i < len(nums) and not foundSolution:
            j = i + 1
            while j < len(nums) and not foundSolution:
                if nums[i] + nums[j] == target:
                    foundSolution = True
                    solutionIndices.append(i)
                    solutionIndices.append(j)
                i+=1
            j+=1
        return solutionIndices
    
# Test Case 1:
nums_1 = [2, 7, 11, 5]
target_1 = 9

solution = Solution()
result_1 = solution.twoSum(nums_1, target_1)
print("1:", result_1)

# Test Case 2:
nums_2 = [3, 2, 4]
target_2 = 6
result_2 = solution.twoSum(nums_2, target_2)
print("2:", result_2) 

# Test Case 3:
nums_3 = [3, 3]
target_3 = 6
result_3 = solution.twoSum(nums_3, target_3)
print("2:", result_3)
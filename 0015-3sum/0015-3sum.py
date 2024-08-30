from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to facilitate the two-pointer approach
        nums.sort()
        result = []
        
        # Iterate through the array, considering each number as a potential first element of a triplet
        for i in range(len(nums) - 2):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            # Use the two-pointer technique to find the other two numbers
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer to the right, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left, skipping duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after processing the current pair
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    # If the sum is less than zero, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left
                    right -= 1
        
        return result
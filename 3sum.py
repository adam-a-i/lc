class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()  
        # Example: nums = [-1, 0, 1, 2, -1, -4] → after sort: [-4, -1, -1, 0, 1, 2]

        triplets = []  # This will hold the result (list of valid triplets)

        # Outer loop: choose each number as the "fixed" value
        for i in range(len(nums) - 2):  
            # -2 because we need at least 2 more numbers after i

            if i > 0 and nums[i] == nums[i - 1]:
                continue  
                # Skip duplicate fixed values to avoid repeating triplets
                # Example: when i=2 (nums[2] = -1 same as nums[1]), skip it.

            fixed_val = nums[i]  
            # Example iteration 1: i=0 → fixed_val = -4
            # Example iteration 2: i=1 → fixed_val = -1

            left, right = i + 1, len(nums) - 1  
            # Two-pointer setup:
            # left starts just after fixed_val
            # right starts at the end of the list

            while left < right:  
                # Run until the two pointers cross

                total = fixed_val + nums[left] + nums[right]  
                # Compute sum of triplet candidate

                if total == 0:
                    # Found a valid triplet
                    triplets.append([fixed_val, nums[left], nums[right]])

                    # Example: fixed_val = -1, left=2 (nums[2]=-1), right=4 (nums[4]=2)
                    # total = -1 + -1 + 2 = 0 → triplet = [-1, -1, 2]

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward to look for next candidates
                    left += 1
                    right -= 1

                elif total < 0:
                    # If sum is too small, increase it by moving left pointer
                    left += 1

                else:
                    # If sum is too big, decrease it by moving right pointer
                    right -= 1

        return triplets

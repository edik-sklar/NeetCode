from collections import defaultdict


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = defaultdict(int)
        for i, n in enumerate(numbers):
            comp = target - n
            if comp in seen:
                return [seen[comp] + 1, i + 1]
            seen[n] = i

    def two_sum_two_point(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            sum = nums[l] + nums [r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else: return[l+1,r+1]
        return []

# numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]

# numbers = [2, 3, 4], target = 6
# Output: [1, 3]

# numbers = [-1, 0], target = -1
# Output: [1, 2]

s = Solution()
print(s.two_sum_two_point([2, 7, 11, 15],9))
print(s.two_sum_two_point([2, 3, 4],6))
print(s.two_sum_two_point([-1, 0],-1))
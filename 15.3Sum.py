# mine with AI and didnt worked
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        triplets = set()

        # Ensure there is at least one element between left and right
        while left < right - 1:
            sum_lr = sorted_nums[left] + sorted_nums[right]

            if sum_lr < 0:
                # 1. Scan backwards for a matching middle element
                pointer = right - 1
                while pointer > left and sum_lr + sorted_nums[pointer] > 0:
                    pointer -= 1

                if pointer > left and sum_lr + sorted_nums[pointer] == 0:
                    triplets.add(
                        (sorted_nums[left], sorted_nums[pointer], sorted_nums[right])
                    )
                
                # 2. Since sum_lr is negative, increment 'left' to increase future sums
                c_left = sorted_nums[left]
                left += 1
                while left < right and sorted_nums[left] == c_left:
                    left += 1

            else:  # sum_lr >= 0
                # 1. Scan forwards for a matching middle element
                pointer = left + 1
                while pointer < right and sum_lr + sorted_nums[pointer] < 0:
                    pointer += 1

                if pointer < right and sum_lr + sorted_nums[pointer] == 0:
                    triplets.add(
                        (sorted_nums[left], sorted_nums[pointer], sorted_nums[right])
                    )

                # 2. Since sum_lr is non-negative, decrement 'right' to decrease future sums
                c_right = sorted_nums[right]
                right -= 1
                while left < right and sorted_nums[right] == c_right:
                    right -= 1

        # Return outside the while loop, converting tuples back to lists
        return [list(t) for t in triplets]


# AI
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            # Skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets

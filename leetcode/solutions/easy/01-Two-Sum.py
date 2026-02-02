"""
LeetCode #1: Two Sum
Date: Feb 2, 2026
Difficulty: Easy
Pattern: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)

Problem:
Given an array of integers nums and target,
return indices of two numbers that add to target.

Approach:
Use hash map to store {number: index}.
For each number, check if (target - number) exists in map.
"""
• explanation
• code

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        notebook = {}
        for position, number in enumerate(nums):
            needed = target - number
            if needed in notebook:
                return [notebook[needed], position]
            notebook[number] = position
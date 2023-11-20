class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # gna eliminate the indicies
        longest = 0 # to keep track of the longest sequence

        for n in numSet:
        # check if its the start of a sequence
            if (n - 1) not in numSet: # Check if the current number n is the start
                                      # of a consecutive sequence by verifying that
                                      # the previous number (n - 1) is not in the set.
                length = 1 # Initialize a variable length to 1, as we have already found 
                           # one element in the sequence.

                while (n + length) in numSet: # Enter a while loop to increment the length while the next
                                              # number in the sequence is present in the set.
                    length += 1 # Increment the length for each consecutive number in the sequence.
                longest = max(length, longest) # Update the longest variable with the maximum value between
                                               # the current length and the previously stored longest length.
        return longest # After iterating through all numbers, return the length of the 
                       # longest consecutive sequence found.
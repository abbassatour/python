#my solution 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 :
            return True
        cleanString = ''
        s = s.lower()
        for i in s :
            if i.isalnum():
                cleanString += i 
        left , right   = 0 , len(cleanString )  - 1 
        while left < right : 
            if cleanString[left ] == cleanString[right ] :
                left += 1 
                right -= 1 
            else :
                return False 

        return True 


#AI 
'''
Your solution is functionally correct, and it is great that you used the
two-pointer approach! However, in a Google STEP interview, this code would
likely receive solid partial credit rather than full marks.

Google interviewers evaluate not only whether your code works, but also its
space efficiency, code quality, and your adherence to language-specific
conventions.

Here is how you can elevate (improve to a higher level) this solution to get
full marks:

1. Optimize Space Complexity to O(1)

  - Current code: You create a new string cleanString and duplicate the input
    with s.lower(), which uses O(N) extra space.
  - Interview expectation: The standard follow-up question for this problem is:
    "Can you do this without allocating additional memory?"
  - The fix: Apply the two pointers directly on the original string s, skipping
    non-alphanumeric characters dynamically using a loop.

2. Follow Python Conventions (PEP 8)

  - In Python, standard style uses snake_case instead of camelCase for variable
    names (e.g., clean_string or simply left / right).
  - String concatenation inside a loop (cleanString += i) can be suboptimal
    (less than ideal) in terms of memory reallocations, although skipping the
    extra string entirely avoids this issue altogether.

3. Remove Redundant (unnecessary) Base Cases

  - The check if len(s) == 1: return True is not needed because the two-pointer
    condition while left < right: naturally handles strings of length 0 and 1
    without executing the loop.

Ideal Solution for the Interview

Here is the version that demonstrates strong algorithmic awareness and clean
Python style:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

Why Interviewers Love This Approach:

1.  Time Complexity: O(N) — you still scan the string in a single pass.
2.  Space Complexity: O(1) — you use only two pointers and no extra data
    structures.
3.  Robustness: It effortlessly handles edge cases like empty strings, strings
    with only spaces/punctuation, and single characters.

Are you actively preparing for an upcoming STEP interview, or are you practicing
LeetCode patterns in general?

[Feedback]

  - Spelling:
      - "do you thing" \rightarrow "do you think"
      - "this code while be" \rightarrow "this code will be"
      - "ful mark" \rightarrow "full marks"
  - Word Choice:
      - "the variables's name" \rightarrow "the variable names"

'''
#AI
class Solution:
    def fib(self, n: int, memo=None) -> int:
        # Initialize the dictionary on the first call
        if memo is None:
            memo = {}

        # 1. Base Case
        if n <= 1:
            return n

        # 2. Check cache
        if n in memo:
            return memo[n]

        # 3. Recursive step + store in cache
        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n]

#AI inner helper 
class Solution:
    def fib(self, n: int) -> int:
        # Initialize the cache in the enclosing scope
        memo = {}

        def helper(x: int) -> int:
            # 1. Base Case / Guard Clause
            if x <= 1:
                return x

            # 2. Check Cache
            if x in memo:
                return memo[x]

            # 3. Recursive Step + Store Result
            memo[x] = helper(x - 1) + helper(x - 2)
            return memo[x]

        # Trigger the recursion starting from n
        return helper(n)

#simple AI
class Solution:
    def fib(self, n: int) -> int:
        # 1. Guard Clause: Handles base cases F(0)=0 and F(1)=1 in O(1) time
        if n <= 1:
            return n

        # 2. State Initialization: Seed values for F(0) and F(1)
        prev, curr = 0, 1

        # 3. State Transition: Advance the rolling window (n - 1) times
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        # 4. Result: 'curr' now holds F(n)
        return curr

#Normal recursion
class Solution:
    def fib(self, n: int) -> int:
        # Base case: if n is 0 or 1, return n directly
        if n <= 1:
            return n

        # Recursive call: F(n) = F(n - 1) + F(n - 2)
        return self.fib(n - 1) + self.fib(n - 2)


#mine 
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1 :
            return n
        
        return self.fib(n-1) + self.fib(n-2)


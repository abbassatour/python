class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if not idx :
            return word
        firstSlice = word[:idx + 1] [::-1]
        secondSlice = word[idx +1 :]
        return firstSlice + secondSlice


'''
This is one of the most elegant aspects of Python's design, and it comes down to
how Python handles slice boundaries as half-open intervals [start, stop).

Here is why idx + 1 is used in both places:

1. The Left Slice: text[: idx + 1]

In Python, the stop index of a slice is exclusive (meaning Python stops right
before that index).

  - If the target character is at idx = 5, writing text[:5] would only capture
    indices 0, 1, 2, 3, 4—it would leave out the target character itself!
  - To demarcate (set the boundary of) a slice that includes index 5, we must
    tell Python to stop at index 6 (idx + 1).

2. The Right Slice: text[idx + 1 :]

The start index of a slice is inclusive (Python begins exactly at that index).

  - Because the character at idx is already included in our reversed prefix, the
    remaining part of the string should begin at the very next character.
  - Therefore, the remainder starts at idx + 1 and continues to the end.

🎨 Visualizing the Split

Let's look at "hello#world" where idx = 5 (the # character):

Index:   0   1   2   3   4   5   6   7   8   9  10
Char:    h   e   l   l   o   #   w   o   r   l   d
                         ▲   ▲
                       idx  idx + 1 (boundary = 6)

1.  Prefix text[:6]: takes indices 0 through 5 \rightarrow "hello#"
2.  Suffix text[6:]: takes indices 6 through 10 \rightarrow "world"

💡 The Pythonic Symmetry

In Python, for any integer k, splitting a string s at k guarantees contiguous
(unbroken and adjacent in sequence) parts without gaps or duplicates:

\text{s}[:k] + \text{s}[k:] == \text{s}

By choosing k = \text{idx} + 1, we split the string right after the target
character, perfectly partitioning it into two halves.

Does this make the indexing intuition clearer? When you feel ready, how would
you write the solution for the LeetCode method?



Here is a complete, runnable script using our analogous example so you can see
how all the pieces function together cohesively (in a unified way):

def transform_until_symbol(text: str, symbol: str) -> str:
    # 1. Locate the position of the target character
    idx = text.find(symbol)

    # 2. Guard clause: Return early if the character does not exist
    if idx == -1:
        return text

    # 3. Slice and reverse up to idx (inclusive)
    reversed_part = text[: idx + 1][::-1]

    # 4. Slice the remaining suffix
    remainder = text[idx + 1 :]

    # 5. Combine both parts
    return reversed_part + remainder


# --- Test Run ---
sample_text = "hello#world"
delimiter = "#"

final_result = transform_until_symbol(sample_text, delimiter)
print(f"Original : {sample_text}")
print(f"Result   : {final_result}")

Output:

Original : hello#world
Result   : #ollehworld

Why the Guard Clause Matters

Notice how step 2 immediately handles the non-matching case and returns early.
This pattern minimizes indentation and helps keep your logic flat and readable.

Now, could you synthesize (combine into a coherent whole) this structure and
adapt it into the Solution class for your LeetCode problem?

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # What would your implementation look like here?

Give it a try and paste your code here!

[Feedback]

  - Polite Requesting & Professional Phrasing: In collaborative software
    engineering or pair programming, using direct imperatives like "put them in
    the example code" can sound overly abrupt. More natural and professional
    alternatives include:
      - "Could you show this within a complete, runnable script?"
      - "Could you put that into a full example function?"

'''
"""
Approach: We converted the string to a list of words and then the length of pattern with len of words list.
Created a dictionary to store the mapping from characters in s to characters in t.
created a set to track which characters in t have already been mapped.
We iterate through both strings simultaneously. If a character from s is already mapped and checks whether it is mapping to the corresponding character in t or not. 
If it is a new mapping, we verify that the character in t has not been used before, then we do the mapping.
If no conflicts, we return true. else false
Time Complexity: O(n)

Space Complexity: O(1)

Accepted in leetcode: Yes

Any difficulties: No

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")  # Converting string to list of words
        
        if len(pattern) != len(words):  # Ensureing pattern and words have the same length
            return False 

        pattern_to_t = {}  # Dictionary to store character-to-word mapping
        t_to_pattern = set()  # Set to track already mapped words

        for p_char, word in zip(pattern, words):  # Iterate through pattern and words together
            if p_char in pattern_to_t:
                if pattern_to_t[p_char] != word:  # Check if previous mapping is same or not
                    return False
            else:
                if word in t_to_pattern:  # Ensuring no duplicate mappings
                    return False
                pattern_to_t[p_char] = word  # Create new mapping
                t_to_pattern.add(word)  # adding word to set
        
        return True  # If no conflicts found, return True


sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))  # True
print(sol.wordPattern("abba", "dog cat cat fish"))  # False
print(sol.wordPattern("aaaa", "dog cat cat dog"))  # False
print(sol.wordPattern("abba", "dog dog dog dog"))  # False

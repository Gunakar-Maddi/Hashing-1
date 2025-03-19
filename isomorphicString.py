"""
Approach: Created a dictionary to store the mapping from characters in s to characters in t.
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
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {} # Dictionary to map characters from s to t
        t_to_s = set() # Set to track mapped characters in t

        for s_char, t_char in zip(s,t): # Iterate through both strings together
            if s_to_t[s_char] != t_char:  # Checking if previous mapping is same or not
                return False

            else:
                if t_char in t_to_s: # Ensuring no duplicate mappings
                    return False
                s_to_t[s_char] = t_char # Create new mapping
                t_to_s.add(t_char) # adding t_char to set
        return True # If no conflicts found, return True


sol = Solution()
print(sol.isIsomorphic("egg", "add"))  # True
print(sol.isIsomorphic("foo", "bar"))  # False
print(sol.isIsomorphic("paper", "title"))  # True
print(sol.isIsomorphic("badc", "baba"))  # False
"""
Approach: For the the input list, we sort the each word alphabetically and the sorted word is used as a key for the word.
if the sorted word in the dictionary, we append to its list or we create a new list. 
we return all the grouped anagrams as a list of values

Time Complexity: Iterating for n words -> O(n). Sorting each word -> O( k logk) where k is the length of the word
O(n * k logk)

Space Complexity: o(nk)

Accepted in leetcode: Yes

Any difficulties: No


"""
class Solution:
    def groupAnagrams(self, strs):
        anagrams = {} # dict to store anagrams
        for word in strs:
            sorted_key = ''.join(sorted(word)) #sorting word to use it as a key
            if sorted_key not in anagrams:
                anagrams[sorted_key] = [word] #create new group if key doesnt exist
            else:
                anagrams[sorted_key].append(word) # append to existing group
        return list(anagrams.values()) 

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
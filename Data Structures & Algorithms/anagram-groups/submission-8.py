class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            s_sorted = tuple(sorted(s))
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
        ans = [] 
        for anagram in anagrams.keys():
            ans.append(anagrams[anagram])
        return ans
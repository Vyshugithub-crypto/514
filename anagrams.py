from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> list[list[str]]:
        anagrams=defaultdict(list)
        for String in strs:
            String1="".join(sorted(String))
            anagrams[String1].append(String)
        return list(anagrams.values())
        

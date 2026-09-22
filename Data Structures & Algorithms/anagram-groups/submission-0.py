class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fun = collections.defaultdict(list)
        for t in strs:
            count = [0] * 26
            for a in t:
                count[ord(a) - ord("a")] += 1
            fun[tuple(count)].append(t)
        return list(fun.values())
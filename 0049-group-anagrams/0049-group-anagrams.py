class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        new_str = {}

        for word in strs:

            key = "".join(sorted(word))

            if key not in new_str:
                new_str[key] = []

            new_str[key].append(word)

        return list(new_str.values())
            
        
        


            





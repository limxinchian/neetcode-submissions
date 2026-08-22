class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # for index, string in enumerate(strs):
            # print(strs[index + 1])
            # if(len(strs[index + 1]) != len(string)):

        # for i in range (len(strs)):
        #     if strs[i] not in anagram_dict:
        #         anagram_dict[strs[i]] = anagram_dict.get(strs[i],[]) + [strs[i]]
            
        #     for char in strs[i]
        #         if len


            # if(len(strs[i + 1]) == len(string)):
            # print(anagram_dict)
            # return
        ord_list = []
        key = ()
        anagram_dict = {}

        for string in strs:
            # print(sorted(string))
            key = tuple(sorted(string))

            if key not in anagram_dict:
                anagram_dict[key] = anagram_dict.get(key,[]) + [string]

            else:
                anagram_dict[key] = anagram_dict.get(key,[]) + [string]
        # print(anagram_dict)
        # print(anagram_dict.values())

        return list(anagram_dict.values())
               
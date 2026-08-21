class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = []
        check = []

        for string in strs:
            length.append(len(string))

        min_length = min(length) 
        min_pos = length.index(min_length)
        shortest = strs[min_pos]
        # print("shortest",shortest)
        # print("min_pos",min_pos)
        # print("min_length",min_length)

        for i in range (min_length):
            # print(i,strs[i])
            for string in strs:
                # print("charsssss", string)
                if string[i] != shortest[i]:
                    # print("char", string)
                    return shortest[:i]
        
        return shortest
                # print(strs[i][j])
        

              
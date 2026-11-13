class Solution : 

    def longestCommonPrefix(self, strs:list[str]) -> str:
        if not strs : 
            return ""
        

        count = ""


        min_len = len(min(strs, key = len))

        for i in range(min_len) : 

            for j in range(len(strs)) : 
                if(strs[j][i] != strs[0][i]) : 
                    return count
            count += strs[0][i]
        return count
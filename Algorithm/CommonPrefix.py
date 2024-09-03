def longestCommonPrefix(strs: list[str]) -> str:
    if (len(strs)) == 0 :
        return ""
    elif (len(strs)) == 1:
        return strs[0]
    
    length_strs = [len(i) for i in strs]

    # Sorted
    for i in range(len(length_strs)):
        for j in range(0, len(length_strs) - i -1):
            if length_strs[j] > length_strs[j+1] : 
                length_strs[j],length_strs[j+1] = length_strs[j+1] , length_strs[j]
                strs[j] , strs[j+1] = strs[j+1].lower() , strs[j].lower()
    # print(length_strs)
    # print(strs)
    prefix = strs[0]
    for x in range(1 , len(strs)):
        while strs[x].find(prefix) != 0 :
            prefix = prefix[:-1]
            if not prefix : 
                return ""
    return prefix
    

print(longestCommonPrefix(["flower","flow","flight"]))
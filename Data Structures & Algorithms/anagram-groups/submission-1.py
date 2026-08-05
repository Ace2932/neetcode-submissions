class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordMap = {}
        wordlist = []
        finalList = []
        for index, word in enumerate(strs):

            alpha = "".join(sorted(word))
            if alpha not in wordMap:
                wordMap[alpha] = []
            wordMap[alpha].append(index)


        for indexes in wordMap.values():
            sublist = []
            for index in indexes:
                
                sublist.append(strs[index])
            
            finalList.append(sublist)

        return finalList












        




            



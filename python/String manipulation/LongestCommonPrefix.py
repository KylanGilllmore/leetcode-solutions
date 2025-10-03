
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # shortest_word = min([len(word) for word in strs])
        # list_size = len(strs)
        # prefix =''
        # for i in range(shortest_word):
        #     current_letter = strs[0][i]
        #     counter = 0
        #     for j in range(list_size):
        #         if strs[j][i] == current_letter:
        #             counter += 1
        #         if counter == list_size:
        #             prefix += current_letter
        #     if counter != list_size:
        #         return prefix
        # return prefix

        if not strs:
            return ''
        shortest_word = min([len(word) for word in strs])
        prefix = ''
        for i in range(shortest_word):
            current_letter = strs[0][i]
            if all(word[i] == current_letter for word in strs):
                prefix += current_letter
            else:
                break
        return prefix

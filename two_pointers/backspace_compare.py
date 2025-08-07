class Solution:

    def backspaceCompare(self, s: str, t:str) -> bool:
        '''
        LeetCode 844: backspace compare
        Pattern: Two Pointers
        Difficulty: Easy
        Link: https://leetcode.com/problems/backspace-string-compare/
        '''
        #Helper function to get valid indexes
        def get_valid_index(string, index):
            '''
            Gets valid indexes that aren't backspaced
            '''
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_valid_index(s, i)
            j = get_valid_index(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                    
            elif i > 0 or j > 0:
                return False

            i -= 1
            j -= 1

        return True

ins = Solution()

print(ins.backspaceCompare("ab#c", "b#ag#c"))
print(ins.backspaceCompare("ab#c", "b#cg#a"))

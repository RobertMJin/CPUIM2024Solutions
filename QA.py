class Solution:
    def twoSum(s):
        s = s.lower()
        temp1 = ''.join(sorted(s))
        temp2 = ''.join(sorted(s, reverse=False))[::-1]
        if s==temp1 or s==temp2:
            print('yes')
        else: print('no')
    
    val = input()
    twoSum(val)
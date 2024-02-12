
class Solution:
    def total(str):
        ### list: String
        prev = ''
        curr = ''
        capsMode = False
        accum = 0
        for element in range(0, len(str)):
            curr = str[element]
            if curr.islower():
                capsMode = False
            if curr.isspace() and not prev.isspace():
                accum+=1
                #print("accum from space at index: %d", element)
            else:
                if curr.lower() != prev.lower():
                    accum+=1
                    #print("accum from samechar at index: %d", element)
                if curr.isupper() and not prev.isupper() and not capsMode:
                    capsMode = True
                    accum+=1
                    #print("accum from caps at index: %d", element)
                    
            prev = curr
            
            
        print(accum)

    stringX = input()
    total(stringX)
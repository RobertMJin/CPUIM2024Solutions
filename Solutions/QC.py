class Solution:
    def closest_nonzero_index(self, lst, target_index):
        nonzero_indices = [i for i, value in enumerate(lst) if value > 0]
        closest_index = min(nonzero_indices, key=lambda x: abs(x - target_index))
        return closest_index
    
    def findMins(self, k, x):
        ###k: List[Int]
        ###x: int for recursion
        ###rtype: enumerated List
        updatedList = k.copy()
        if (x > 0):
            currMin = updatedList.index(min(i for i in updatedList if i > -1))
            #print("minimum: " + str(currMin))
            updatedList[currMin] = -1
            nextMin = self.closest_nonzero_index(updatedList, currMin)
            #print("closestmin: " + str(nextMin))
            updatedList[currMin] = updatedList[nextMin] - 1
            updatedList[nextMin] = -1
            print(str(nextMin+1) + " " + str(currMin+1))
            self.findMins(updatedList, x-1)

    def possible(self, k):
        ### k: List[Int]
        ### rtype: Boolean
        numNodes=0
        accum = 0
        for i in k:
            if i >= 0:
                numNodes+=1
                accum+=i
        if (accum+1 <= numNodes):
            print("impossible")
        else:
            print("possible")
            print(numNodes - 1)
            self.findMins(k, numNodes - 1)

sol = Solution()
val = int(input())
arr = [int(x) for x in input().split()]
sol.possible(arr)

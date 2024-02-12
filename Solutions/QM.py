from collections import Counter
class Solution:
    def possible(arr, val):
        ### val: List[Int]
        ### array: List[Int]
        numPerRow = val[1]
        if arr.count(Counter(arr).most_common(1)[0][0]) > numPerRow:
            print("no")
            return
        print("yes")

    val = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    possible(arr, val)

class Solution:
    def smallest_difference(arr, x, y, length):
        
        temp_y = 2**32
        temp_x = 2**32
        for i in range(0, length):
            x = abs(x - arr[i][0])
            y = abs(y - arr[i][1])

            if x < temp_x and y < temp_y:
                temp_x, temp_y = x, y
                
            #print(temp_x, temp_y)
                
        return temp_x + temp_y
        
    def track_length(distance_to_track, length):
        return (0.25 * ((distance_to_track * (distance_to_track + 1))/2 - 1))/length
        
    length = [int(x) for x in input().split()]
    arr = []

    for i in range(length[2]):
        arr.append([int(x) for x in input().split()])
    a = smallest_difference(arr, length[0], length[1], length[2])
    b = track_length(length[0], length[2])
    print(a + b)

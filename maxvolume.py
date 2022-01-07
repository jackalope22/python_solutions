def maxArea(height):
    loop = 0
    length = len(height)
    volume = 0 
    start = height[0]
    end = height[length - 1]
    while loop < length:
        while start < end:
            cvolume = start * start
            if cvolume > volume:
                volume = cvolume
            start += 1
            print(volume)
        loop += 1

        while start > end:
            cvolume = end * end
            if cvolume > volume:
                volume = cvolume
            end += 1
            print(volume)
        loop += 1
            
    return volume

my_list = [8,6,5,2,4,6,7]        
maxArea(my_list)

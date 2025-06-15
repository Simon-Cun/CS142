def main():

    n = int(input()) # takes in the number of stairs

    heights = [] # array for the stair heights
    height_differences = [] # array for the stair height differences

    for i in range(n): # gets all the inputs into heights array
        heights.append(int(input()))

    for i in range(n - 1): # calculates all the differences into the height_differences array
        height_differences.append(heights[i] - heights[i + 1])

    for i in range(n - 2): # checks if the differences are the same, if not then print where it breaks and exit
        if(height_differences[i] != height_differences[i + 1]):
            print(i + 3)
            break
        
main()
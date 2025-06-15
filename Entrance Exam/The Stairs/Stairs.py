def main():

    n = int(input()) # takes in the number of stairs

    heights = [] # array for the stair heights
    height_differences = [] # array for the stair height differences

    for i in range(n):
        heights.append(int(input()))

    for i in range(n - 1):
        height_differences.append(heights[i] - heights[i + 1])

    for i in range(n - 2):
        if(height_differences[i] != height_differences[i + 1]):
            print(i + 3)
            break
        
main()
def main():
    number_of_shots = int(input()) # gets the number of shots
    score = 0
    for i in range(number_of_shots):
        x, y = map(float, input().split()) # maps x and y to the inputs of each line by splitting input into two floats

        score += points(x, y) 
    print(str(score)) # prints out the total score of the shots

def points(x, y): # function to calculate the points for each shot
    sum_of_powers = x**2 + y**2
    if sum_of_powers <= 0.01:
        return 10
    elif sum_of_powers <= 0.04:
        return 9
    elif sum_of_powers <= 0.09:
        return 8
    elif sum_of_powers <= 0.16:
        return 7
    elif sum_of_powers <= 0.25:
        return 6
    elif sum_of_powers <= 0.36:
        return 5
    elif sum_of_powers <= 0.49:
        return 4
    elif sum_of_powers <= 0.64:
        return 3
    elif sum_of_powers <= 0.81:
        return 2
    elif sum_of_powers <= 1:
        return 1
    else:
        return 0

main()
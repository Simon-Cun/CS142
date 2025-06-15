def main():
    team = input().split() # split the first input into two teams [team0, team1]

    sentinel = " caught the Golden Snitch" # sentinel string to know when to end while loop

    # score counter for each team
    team0 = 0
    team1 = 0

    # gets the first score of the match
    point = input()

    if point == team[0]:
        team0 += 10
    else:
        team1 += 10

    while sentinel not in point: # contrinue to get points until we see the sentinel string to exit

        point = input()

        if point == team[0]:
            team0 += 10
        elif point == team[1]:
            team1 += 10

    # add the final point of whoever got the Golden Snitch
    if team[0] + sentinel in point:
        team0 += 150
    elif team[1] + sentinel in point:
        team1 += 150

    # print out the result of the match
    if team0 > team1:
        print(team[0] + " wins")
        print(str(team0) + '-' + str(team1))
    elif team1 > team0:
        print(team[1] + " wins")
        print(str(team1) + '-' + str(team0))
    else:
        print(team[0] + " and " + team[1] + " draw")
        print(str(team1) + '-' + str(team0))

main()
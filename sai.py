import random
sai = [[0]*3 for i in range(3)]
# print(sai)


def board1(sai):
    for i in range(3):
        for j in range(3):
            print(sai[i][j], end=" ")
        print()


def place(sai, player, x):
    if x == 1:
        sai[0][0] = player
    elif x == 2:
        sai[0][1] = player
    elif x == 3:
        sai[0][2] = player
    elif x == 4:
        sai[1][0] = player
    elif x == 5:
        sai[1][1] = player
    elif x == 6:
        sai[1][2] = player
    elif x == 7:
        sai[2][0] = player
    elif x == 8:
        sai[2][1] = player
    else:
        sai[2][2] = player


def check(sai, x):
    if x == 1:
        if sai[0][0] == 0:
            return True
    elif x == 2:
        if sai[0][1] == 0:
            return True
    elif x == 3:
        if sai[0][2] == 0:
            return True
    elif x == 4:
        if sai[1][0] == 0:
            return True
    elif x == 5:
        if sai[1][1] == 0:
            return True
    elif x == 6:
        if sai[1][2] == 0:
            return True
    elif x == 7:
        if sai[2][0] == 0:
            return True
    elif x == 8:
        if sai[2][1] == 0:
            return True
    elif x == 9:
        if sai[2][2] == 0:
            return True
    return False


def checkhorizantal(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 0:
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != 0:
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != 0:
        return True


def checkrow(board):
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != 0:
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
        return True


def checkdiag(board):
    if board[0][0] == board[1][1] == board[2][2] and board[2][2] != 0:
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != 0:
        return True


def run_the_game():
    for i in range(9):
        if i % 2 == 0:
            flag = False
            while True:
                user = int(input(" enter a number from 1 t0 9:"))
                if check(sai, user) == True:
                    print("-----------------------")
                    print(user)
                    print("------------------------")
                    place(sai, "x", user)
                    print(board1(sai))
                    if checkrow(sai) == True:
                        print("the user have win the Came")
                        return True
                    elif checkhorizantal(sai) == True:
                        print("the user have win the Came")
                        return True
                    elif checkdiag(sai) == True:
                        print("the user have win the Came")
                        return True
                    else:
                        flag = True
                else:
                    print("Please enter the valid number")
                if flag == True:
                    break

        else:
            flag = False
            while True:
                computer = random.randint(0, 8)
                if check(sai, computer) == True:
                    print("-----------------------")
                    print(computer)
                    print("------------------------")
                    place(sai, "Y", computer)
                    print(board1(sai))
                    if checkrow(sai) == True:
                        print("the computer have win the Came")
                        return True
                    elif checkhorizantal(sai) == True:
                        print("the computer have win the Came")
                        return True
                    elif checkdiag(sai) == True:
                        print("the computer have win the Came")
                        return True
                    else:
                        flag = True
                else:
                    print("Please enter the valid number")
                if flag == True:
                    break
    else:
        print("match draw")
        return True


run_the_game()

import random

def OXsetting():
    while True:
        x = input("O 또는 X를 선택해주세요.").upper()
        if x == "O":
            UserOX = "O"
            ComOX = "X"
            return UserOX,ComOX
        elif x == "X":
            UserOX = "X"
            ComOX = "O"
            return UserOX,ComOX
        else:
            print("O 또는 X 로 입력해주세요.")

def UserInput(OX,board):
    while True:
        x = int(input("둘곳을 숫자로 입력해주세요."))
        if board[x] == " ":
            board[x] = OX
            return x
        else:
            print("빈칸을 입력해주세요.")

def CompInput(board,ComOX): #Idiot LEVEL
    while True:
        x = random.randint(1,9)
        if board[x] == " ":
            board[x] = ComOX
            return x

def drawBoard(board):
    print(
    """
    {} | {} | {}
    {} | {} | {}
    {} | {} | {}
    """.format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))

def checkwin(OX,winlist):
    for i in winlist:
        if OX == "O":
            if i == ["O","O","O"]:
                print("User Win!")
                return True
            elif i == ["X","X","X"]:
                print("Comp Win!")
                return True
            else:
                pass
        else:
            if i == ["X","X","X"]:
                print("User Win!")
                return True
            elif i == ["O","O","O"]:
                print("Comp Win!")
                return True
            else:
                pass

def changeWL(winlist,board,x):
    for i in winlist:
        for v,l in enumerate(i):
            if l == x:
                i[v] = board[x]
            else:
                pass

def Attack(i,COX,board):
    for v,l in enumerate(i):
        if not(l == COX or l == OX):
            board[l] = COX
            return l
        else:
            pass

def Guard(i,COX,board):
    for v,l in enumerate(i):
        if not(l == COX or l == OX):
            board[l] = COX
            return l
        else:
            pass

def randATK(COX):
    while True:
        x = random.randint(1,9)
        if board[x] == " ":
            board[x] = COX
            return x

def AILevel(winlist,OX,COX,board):
    for i in winlist:
        if i.count(OX) == 2 and i.count(COX) != 1:
            x = Attack(i,COX,board)
            return x
        elif i.count(COX) == 2 and i.count(OX) != 1:
            x = Guard(i,COX,board)
            return x
        return randATK(COX)

winlist = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[2,5,8],[1,4,7],[3,6,9],[3,5,7]]

board = [""," "," "," "," "," "," "," "," "," "]
OX,COX = OXsetting()
while True:
    a = UserInput(OX,board)
    changeWL(winlist,board,a)
    b = AILevel(winlist,OX,COX,board)
    changeWL(winlist,board,b)
    drawBoard(board)
    print(winlist)
    print(board)
    if checkwin(OX,winlist):
        break



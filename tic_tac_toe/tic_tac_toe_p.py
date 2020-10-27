def winTest(OX,COX,winlist):
    for i in winlist:
        if i == [OX,OX,OX]:
        print("User Win!")
        break
    elif i == [COX,COX,COX]:
        print("Com Win!")
        break
    else:
        pass
'''
winlist는 게임에서 이길수있는 경우의 수를 모아놓은 리스트
ex) [1,2,3],[1,5,9],[1,4,7]....
OX와 COX는 유저가 선택한 OX와 컴퓨터의 OX
'''

def moveTest(board):
    for i in range(1,len(board)):
        if i == " ":
            return True

def user(board,OX):
    while True:
        x = input("놓을곳을 입력해주세요.")
        if board[x] == " ":
            board[x] = OX
            break
        else:
            print("빈칸에 입력해주세요.")

import random
def computerRandom(board,COX):
    while True:
        x = random.randint(1,9)
        if board[x] == " ":
            board[x] = COX
            break

def computerAI(board,winlist,OX,COX):
    for i in winlist:
        if i.count(OX) == 2 and i.count(COX) != 1:
            AI(board,i,OX,COX)
        elif i.count(COX) == 2 and i.count(OX) != 1:
            AI(board,i,OX,COX)
        else:
            computerRandom()

def AI(board,i,OX,COX):
    for l in i:
        if not (l == OX or l == COX):
            board[l] == COX
        else:
            pass
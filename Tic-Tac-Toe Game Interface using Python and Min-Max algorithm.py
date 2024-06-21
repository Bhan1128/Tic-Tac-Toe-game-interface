
def Current_State(board):
  print("Current State of the board: \n\n")
  for i in range(0, 9):
    if((i>0) and (i%3==0)):
      print("\n")
    if(board[i]==0):
      print("_", end=" ")
    if(board[i]==-1):
      print("X", end=" ")
    if(board[i]==1):
      print("O", end=" ")
  print("\n\n")

def user1_turn(board):
  Position = input("Enter X's Position: ")
  Position = int(Position)
  if(board[Position-1]!=0):
    print("Wrong Move")
    exit(0)
  board[Position-1]=-1

def user2_turn(board):
  Position = input("Enter O's Position: ")
  Position = int(Position)
  if(board[Position-1]!=0):
    print("Wrong Move")
    exit(0)
  board[Position-1]=1

def minmax(board, player):
  x = analyze_board(board)
  if(x!=0):
    return (x*player)
  Position = -1
  value = -2
  for i in range(0, 9):
    if(board[i]==0):
      board[i]=player
      score=-minmax(board, player*-1)
      board[i] = 0
      if(score>value):
        value=score
        Position=i
  if(Position==-1):
    return 0
  return value

def computer_turn(board):
  Position = -1
  value = -2
  for i in range(0, 9):
    if(board[i]==0):
      board[i]=1
      score=-minmax(board, -1)
      board[i] = 0
      if(score>value):
        value=score
        Position=i
  board[Position]=1

def analyze_board(board):
  cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  for i in range(0, 8):
    if(board[cb[i][0]]!=0 and
       board[cb[i][0]]==board[cb[i][1]] and
       board[cb[i][0]]==board[cb[i][2]]):
      return board[cb[i][0]]

  return 0


def main():
  option = input("Choose an option: 1 for Single player, 2 for Multiplayer: ")
  option = int( option)
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  if( option==1):
    print("Computer: O Vs. You: X")
    player = input("Enter to play 1(st) or 2(nd): ")
    player = int(player)
    for i in range(0, 9):
      if(analyze_board(board)!=0):
        break
      if((i+player)%2==0):
        computer_turn(board)
      else:
        Current_State(board)
        user1_turn(board)

  else:
    for i in range(0, 9):
      if(analyze_board(board)!=0):
        break
      if(i%2==0):
        Current_State(board)
        user1_turn(board)
      else:
        Current_State(board)
        user2_turn(board)

  x = analyze_board(board)
  if(x==0):
    Current_State(board)
    print("Draw!")
  if(x==-1):
    Current_State(board)
    print("Player X wins!!!! O Looses!")
  if(x==1):
    Current_State(board)
    print("Player O wins!!!! X Looses!!")
    
main()


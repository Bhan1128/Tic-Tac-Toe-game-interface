def ConstBoard(Board):
  print("Current State of the Board: \n\n");
  for i in range(0, 9):
    if((i>0) and (i%3==0)):
      print("\n");
    if(Board[i]==0):
      print("_", end=" ");
    if(Board[i]==-1):
      print("X", end=" ");
    if(Board[i]==1):
      print("O", end=" ");
  print("\n\n");

def User1Turn(Board):
  position = input("Enter X's position from [1,2,3....,9]");
  position = int(position);
  if(Board[position-1]!=0):
    print("Wrong Move");
    exit(0);
  Board[position-1]=-1;

def User2Turn(Board):
  position = input("Enter O's position from [1,2,3....,9]");
  position = int(position);
  if(Board[position-1]!=0):
    print("Wrong Move");
    exit(0);
  Board[position-1]=1;

def minmax(Board, Player):
  x = Analyze_Board(Board);
  if(x!=0):
    return (x*Player);
  position = -1;
  Value = -2;
  for i in range(0, 9):
    if(Board[i]==0):
      Board[i]=Player;
      Score=-minmax(Board, Player*-1);
      Board[i] = 0;
      if(Score>Value):
        Value=Score;
        position=i;
  if(position==-1):
    return 0;
  return Value;

def Computer_Turn(Board):
  position = -1;
  Value = -2;
  for i in range(0, 9):
    if(Board[i]==0):
      Board[i]=1;
      Score=-minmax(Board, -1);
      Board[i] = 0;
      if(Score>Value):
        Value=Score;
        position=i;
  Board[position]=1

def Analyze_Board(Board):
  cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

  for i in range(0, 8):
    if(Board[cb[i][0]]!=0 and
       Board[cb[i][0]]==Board[cb[i][1]] and
       Board[cb[i][0]]==Board[cb[i][2]]):
      return Board[cb[i][0]];

  return 0;


def main():
  Choice = input("Enter 1 for Single Player, 2 for Multiplayer:");
  Choice = int(Choice);
  Board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(Choice==1):
    print("Computer: O Vs. You: X");
    Player = input("Enter to play 1(st) or 2(nd): ");
    Player = int(Player);
    for i in range(0, 9):
      if(Analyze_Board(Board)!=0):
        break;
      if((i+Player)%2==0):
        Computer_Turn(Board);
      else:
        ConstBoard(Board);
        User1Turn(Board);

  else:
    for i in range(0, 9):
      if(Analyze_Board(Board)!=0):
        break;
      if(i%2==0):
        ConstBoard(Board);
        User1Turn(Board);
      else:
        ConstBoard(Board);
        User2Turn(Board);

  x = Analyze_Board(Board);
  if(x==0):
    ConstBoard(Board);
    print("Draw!");
  if(x==-1):
    ConstBoard(Board);
    print("Player X wins!!!! O Looses!");
  if(x==1):
    ConstBoard(Board);
    print("Player O wins!!!! X Looses!!");

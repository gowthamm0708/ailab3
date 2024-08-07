1)
graph = {'A': ['B','C'],
	'B': ['D','E'],'C': ['F'],
	'D': [],
	'E': ['F'], 'F': []}
visited=[]
queue=[]
def bfs (visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print (s,end=" ")
        for i in graph [s] :
            if i not in visited:
                visited.append(i)
                queue.append(i)
bfs(visited,graph,'A')

2)


graph = {'A': ['B','C'],'B': ['D','E'],
	'C': ['F'],'D': [],'E': ['F'], 'F': [] }
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')

3)

board = ["-", "-", "-","-", "-", "-","-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True
# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
# Player input
def playerInput(board):
    global currentPlayer
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Invalid move. Try again.")
        playerInput(board)
# Check for win or tie
def checkHor(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False
def checkDia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        global gameRunning
        gameRunning = False
# Switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
def checkWin(board):
    if checkDia(board) or checkRow(board) or checkHor(board):
        printBoard(board)
        print(f"The winner is {winner}")
        global gameRunning
        gameRunning = False
# Game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()

    4)

    class Solution:
   def solve(self, board):
      dict = {}
      flatten = []
      for i in range(len(board)):
         flatten += board[i]
      flatten = tuple(flatten)
      dict[flatten] = 0
      if flatten == (0, 1, 2, 3, 4, 5, 6, 7, 8):
         return 0
      return self.get_paths(dict)
   def get_paths(self, dict):
      cnt = 0
      while True:
         current_nodes = [x for x in dict if dict[x] == cnt]
         if len(current_nodes) == 0:
            return -1
         for node in current_nodes:
            next_moves = self.find_next(node)
            for move in next_moves:
               if move not in dict:
                  dict[move] = cnt + 1
               if move == (0, 1, 2, 3, 4, 5, 6, 7, 8):
                  return cnt + 1
         cnt += 1
   def find_next(self, node):
      moves = {0: [1, 3],1: [0, 2, 4],2: [1, 5],3: [0, 4, 6],4: [1, 3, 5, 7],
               5: [2, 4, 8],6: [3, 7],7: [4, 6, 8],8: [5, 7],}
      results = []
      pos_0 = node.index(0)
      for move in moves[pos_0]:
         new_node = list(node)
         new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]
         results.append(tuple(new_node))
      return results
ob = Solution()
matrix = [[3, 1, 2],[4, 7, 5],[6, 8, 0]]
print(ob.solve(matrix))   

5)

x=int(input("Enter x:"))
y=int(input("Enter y:"))
while True:
    rno=int(input("Enter the ruleno:"))
    if rno==1:
        if x<4:
            x=4
    if rno==2:
        if y<3:
            y=3
    if rno==5:
        if x>0:
            x=0
    if rno==6:
        if y>0:
            y=0
    if rno==7:
        if x+y>=0 and y>0:
            x,y=4,y-(4-x)
    if rno==8:
        if x+y>=3 and x>0:
            x,y=x-(3-y),3
    if rno==9:
        if x+y<=4 and y>0:
            x,y=x+y,0
    if rno==10:
        if x+y<=3 and x>0:
            x,y=0,x+y
    print("X=",x)
    print("Y=",y)
    if(x==2):
        print("The result is a goal state")
        break

    6}

    import random
from itertools import permutations
def tsp(distance):
    n=len(distance)
    best_route=[]
    cost=float("inf")
    for route in permutations(range(n)):
        c=0
        for i in range(n-1):
            c+=distance[route[i]][route[i+1]]
            c+=distance[route[-1]][route[0]]
            if c<cost:
                best_route=route
                cost=c
    return best_route,cost
distance=[[0,10,15,20],[10,0,30,5],[15,30,0,25],[20,5,25,0]]
route,c=tsp(distance)
print("The best route is ",route)
print("The total cost is ",c)

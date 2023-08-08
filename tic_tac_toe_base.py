import pygame

#this is some test code using VS Code running in python 2
#lets make a tictactoe board
class Board:
    def __init__(self):
        #print("We have created a new board")
        self.x =" X "
        self.o = " O "
        symbols = [self.x,self.o]
        self.mt = "   "
        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(None)
            self.board.append(row)
        
    def display_board(self):     
        print(" ",end ="")
        for i in range(3):print(" ",i,"  ",sep ="",end="")
        print()
        for i in range(3):
            print(i,end="")
            for j in range(3):
                item = self.board[i][j]
                if(item is None): print(self.mt,end="")
                else: print(self.board[i][j],end="")
                if(j<2):print("|",end = "")
            print()
    

    def place(self,pos):
        row = int(pos[0])
        col = int(pos[1])
        symb = pos[2]
        self.board[row][col] = " "+symb.upper()+" "
    
    #returns True if valid place
    def is_valid_place(self,pos):
        row = int(pos[0])
        col = int(pos[1])
        if (self.board[row][col] is None): return True
        return False

    def win_check(self):
        xs = [self.x] * 3
        os = [self.o] * 3
        rdiag = []
        ldiag = []
        for i in range(3):
            row = []
            col = []
            rdiag.append(self.board[i][i])
            ldiag.append(self.board[i][2-i])       
            for j in range(3):
                row.append(self.board[i][j])
                col.append(self.board[j][i])
            if(row == xs or row == os or col == xs or col == os): return True
        if(rdiag == xs or rdiag == os or ldiag == xs or ldiag == os): return True

    def draw_check(self):
        #checks if all Rows don't have any Nones left i.e filled up
        if (all([None not in self.board[i] for i in range(0,3)])): return True


class Player:
    def __init__(self,name,symb):
        self.name = name
        self.symb = symb

    def move(self):
        result = input("What position would you like your token in rowcol format e.g 01 \n")
        return result + self.symb
    
    def get_name(self):
        return self.name
        

class TTTGame:
    def __init__(self):
        print("Tic Tac Toe Game")        
        self.MyBoard = Board()
        self.MyBoard.display_board()
        self.players = []
        self.pc = 0
            
    
    # this function interfaces between the board and the player to make sure the move is valid
    def coord_player_move(self): 
        curr_player =self.players[self.pc]
        pos = curr_player.move()
        while(True):
            if(self.MyBoard.is_valid_place(pos)):break
            print("That is an invalid move %s! Try again" % curr_player.get_name())
            self.MyBoard.display_board()
            pos = self.players[self.pc].move()
        self.MyBoard.place(pos)
    
    def is_done(self):
        if(self.MyBoard.win_check()):
            print("The game is won by",self.players[self.pc].get_name())
            return True
        if(self.MyBoard.draw_check()):
            print("The game is a draw")
            return True
    
    def pvp(self):
        
        print("This is a PVP Game")
        p1 = input("Player 1, Enter your name: ")
        p2 = input("Player 2, Enter your name: ")
        self.players.append(Player(p1,"X"))
        self.players.append(Player(p2,"O"))
        fin = False
        while(not fin):     
            curr_player = self.players[self.pc]
            print("%s's Turn"% curr_player.get_name())
            self.coord_player_move()
            self.MyBoard.display_board()
            if(self.is_done()): 
                break
            fin = self.MyBoard.win_check()
            self.pc=(self.pc+1)%2 #this causes the player counter to alternate between 0 and 1

if __name__ == '__main__':
    #print("this is my first few tests in VS Code")
    TTTGame().pvp()


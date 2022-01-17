class TicTacToe: 
    def __init__(self):
        self.list = []

    def create_board(self):
        for i in range(3):
            rows = []
            for j in range(3):
                rows.append("")
            self.list.append(rows) 

    def print_board(self):
        for items in self.list: 
            print(items) 

    def go_first(self):
        from random import randint
        flip = randint(1,2)
        return flip

    def swap_func(self , player):
        if player == 1 :
            return 2 
        else: 
            return 1      

    def isFull(self):
        for i in range(3):
            for j in range(3):
                if self.list[i][j] != "":
                    return False 

        else:
            return True             


    def isfull(self , row , column):
        if self.list[row][column] == "":
            return False 
        else: 
            return True

    def win_check(self):
        win = None 

        if (self.list[0][0] == self.list[0][1] == self.list[0][2] == "X" or
        self.list[1][0] == self.list[1][1] == self.list[1][2] == "X"or 
        self.list[2][0] == self.list[2][1] == self.list[2][2] == "X"or
        self.list[0][1] == self.list[1][0] == self.list[2][0] == "X"or 
        self.list[0][1] == self.list[1][1] == self.list[2][1] == "X"or 
        self.list[0][2] == self.list[1][2] == self.list[2][2] == "X"or 
        self.list[0][0] == self.list[1][1] == self.list[2][2] == "X"or 
        self.list[0][0] == self.list[0][1] == self.list[0][2] == "O"or
        self.list[1][0] == self.list[1][1] == self.list[1][2] == "O"or 
        self.list[2][0] == self.list[2][1] == self.list[2][2] == "O"or
        self.list[0][1] == self.list[1][0] == self.list[2][0] == "O"or 
        self.list[0][1] == self.list[1][1] == self.list[2][1] == "O"or 
        self.list[0][2] == self.list[1][2] == self.list[2][2] == "O"or 
        self.list[0][0] == self.list[1][1] == self.list[2][2] == "O"):
            win = True 
        else:
            win = False  

        return win   
         

    def func(self):
        print("Welcome to the game of Tic Tac Toe ")
        game_on = input("Shall we begin the game ? (y or n) :").lower()
        if game_on == "n":
            return  
        else: 
            print("Rules : Player 1 will be 'X' while player 2 will be 'O'")
            player = self.go_first()
            print("Player {} will go first !".format(player))
            self.create_board()
            self.print_board()
            while (self.isFull != True ):
                indexi = int(input("In which row would you like to place your marker ? : "))
                indexj = int(input("In which column would you like to place your marker ? : "))
                if self.isfull(indexi , indexj) == False :    
                    if player == 1 : 
                        self.list[indexi][indexj] = "X"
                    else:       
                        self.list[indexi][indexj] = "O"    
                    self.print_board()
                else: 
                    while (self.isfull[indexi , indexj] == True):
                        print("The position is already occupied , enter a new position")
                        if self.isfull(indexi , indexj) == True : 
                            indexi = int(input("In which row would you like to place your marker ? : "))
                            indexj = int(input("In which column would you like to place your marker ? : "))

                if self.win_check() == True : 
                    print("player {} wins !".format(player))
                    break
                else: 
                    if self.isFull() == True :
                        print("The game is draw !")
                        break 
                    else: 
                        player = self.swap_func(player)
                        print("Player {} turn ".format(player))



tt = TicTacToe()
tt.func()
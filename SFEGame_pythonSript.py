# %%
import chess
import chess.svg
from stockfish import Stockfish
from IPython.display import display, SVG







class GameSettings:
  
  stockfish = Stockfish(path=r"C:\Users\aw11c\OneDrive\Desktop\coding\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern") 
  recorded_moves = [] # this is needed to store all the moves in the game so the stockfish engine can pixk the best moves 
  board = chess.Board() #board where moves of both players are placed


        

  def display_board(self): 
     visual_board = chess.svg.board(board=self.board, size=350)
     return display(SVG(visual_board)) #SVG board
  
  
  def undo_move(self):
     
     user_move_removed = GameSettings.board.pop()
     sfe_move_removed = GameSettings.board.pop()
     del GameSettings.recorded_moves [-2:]
     self.display_board() 

     return(f'{user_move_removed , sfe_move_removed }move removed')
     
  









           
       
   
      
   
       
class UserMove (GameSettings):
         

    @staticmethod

    def get_user_input():  # flexible user unput

        global user_input
        user_input = input('Make a move!: ')

    
          



    def user_validated_move(self):
       


        while True:


            self.get_user_input()  # Get user input before the move

            if user_input == 'esc':
               break

            elif user_input == 'Undo':
               GameSettings().undo_move()

            try:
                
                
                san_validated_move = GameSettings.board.push_san(user_input)
                GameSettings.recorded_moves.append(str(san_validated_move))
                self.display_board() 
                print(san_validated_move)
                break

            
    
        
            except ValueError:
             print ('Invalid move mate')

       

            
               
           
        
               
    





    


class SfeMoves(UserMove):
   
   def fish_suggestions():
      
      
      GameSettings.stockfish.set_position(GameSettings.recorded_moves)
      SFE = GameSettings.stockfish.get_best_move()
      best_move_string = str(SFE)
      SFE_san_move= GameSettings.board.push_san(best_move_string)
      GameSettings.recorded_moves.append(best_move_string)



      return SFE_san_move
    
    
   
   def scholar_1st_move(self):
      
      SFE = GameSettings.board.push_san('e4')  #Scholar mate defaoult move
      GameSettings.recorded_moves.append(str(SFE))
     

      self.display_board()
      return SFE

   
    
   def queen_move(self):
       
       global user_input

       if user_input != 'Nf6' and user_input != 'g6':
          queen_move=GameSettings.board.push_san('Qh5')
          GameSettings.recorded_moves.append(str(queen_move))
          self.display_board()
          return  f'It responds with {queen_move}'
       
       else: 
           alternative_move=SfeMoves.fish_suggestions()
           self.display_board()

           return f'It responds with {alternative_move}'
       

       
   def bishop_move (self):
       
       global user_input
       
       dangerous_moves = ['b5','d5','g6','Nf6'] 

       if user_input in dangerous_moves:
           
        alternative_move2 = SfeMoves.fish_suggestions()
        self.display_board()

        return f'It responds with {alternative_move2}'
       
       else:
            bishop_move=GameSettings.board.push_san('Bc4')
            GameSettings.recorded_moves.append(str(bishop_move))
            self.display_board()
             
            return f'Bishop out!!! {bishop_move}'


    
      
      
   
          

#-------------------------------------------------------------GAME------------------------------------------------------------------------------------------------------- 
   
      


class ScholarFreakGame(SfeMoves):

    print( 'Hello , Before starting the game mind this instructions.')
          
    print( "1. By typing 'esc' you resign the game")
    print( "2. 'Undo' is for removing your last move")
    print( "3. Sometimes move may not appear so it is suggested to type a random STRING  to trigger the previous display (make sure is not another valid move")
    print( "4. moves can be only accepted in SAN format")
    print( "5. 0-0 for catling king side , 0-0-0 for the queen side ")
    print( "6. for capturing pieces the letter required is 'x' for example 'if a pawn on d4 captures a piece on e5, it would be represented as dxe5.if a knight on f3 captures a piece on e5, it would be represented as Nxe5 (assuming no other knights can move to e5")
    print( "7. if pieces can make the same move you just need to specify the position ex:If there are rooks on d4 and g4, and both can move to e4, you can specify the move of the rook from the d-file as Rde4 or from the g-file as Rge4.")
    print( "8. Unfortunately you will only play with black. new versions of the Game will be imolemented in the future")  
     
    print( "That should do for the game. I apologise in advance for any inconveniences ")
              
    print( "Have fun 😉♟️")

    # FIRST MOVE

    scholar_first_move = SfeMoves().scholar_1st_move()
    print(f'scholar plays  {scholar_first_move}')

      

    


    def board_turns(self):

    # OPENINNG PHASE

        user_plays = UserMove().user_validated_move()
        print(user_plays)
        print(GameSettings.recorded_moves)

        

        second_sfe_move=SfeMoves().queen_move()
        print(second_sfe_move)


         
        user_plays2 = UserMove().user_validated_move()
        print(user_plays2)

        Third_sfe_move=SfeMoves().bishop_move()
        print(Third_sfe_move)

        if GameSettings.board.is_check():
            print('YOUR KING IS IN CHECK!!!') 


    # EARLY MIDDLE GAME
        

        while True:
           
            user_plays = UserMove().user_validated_move()
            print(user_plays)
            print(GameSettings.recorded_moves)
           

            if GameSettings.board.is_check():
              print('YOUR KING IS IN CHECK!!!') 

            elif user_input == 'Undo':
               GameSettings().undo_move()
              

            elif user_input == 'esc':
               break

            elif GameSettings.board.is_checkmate():
                print('Game Over , You have lost')
                self.display_board()
                break




            self.display_board()
            




            scholar_chess = SfeMoves.fish_suggestions()
            print(f'scholar plays {scholar_chess}')


            if GameSettings.board.is_checkmate():
                print('Game Over , You have lost')
                self.display_board()
                break

            elif GameSettings.board.is_check():
                print('YOUR KING IS IN CHECK!!!') 
            
            self.display_board()
            print(GameSettings.recorded_moves)




        
shall_the_game_begin = ScholarFreakGame()
shall_the_game_begin.board_turns()







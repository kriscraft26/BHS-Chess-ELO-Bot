import math
from chessPlayer import Player
class elo:
    @staticmethod
    def elo_updater(winner=Player,loser=Player, score=float):
        #Calculate the difference and find the ratio
        winner_ratio = ((loser.getElo() - winner.getElo())/400)
        loser_ratio = ((winner.getElo() - loser.getElo())/400)
        
        #Calculates the expected score based on FIDE ELO equation
        def expect_score(player=Player,ratio=float):
            x = 1 + pow(10,ratio)        
            return pow(x,-1)
        #Elo Change using the FIDE ELO equation
        def elo_change(player=Player, ratio=float, score=float):
            return 40*(score-expect_score(player,ratio))
        
        #If the score is 1, which is a win, apply the proper score to the elo_change function
        if(score == 1):
            winner_change = elo_change(winner,winner_ratio,1) 
            loser_change = elo_change(loser,loser_ratio,0)
            
        #If the score is 0.5, which is a draft, apply the proper score to the elo_change function
        elif(score == 0.5):
            winner_change = elo_change(winner,winner_ratio,0.5) 
            loser_change = elo_change(loser,loser_ratio,0.5)
            
        #Update the elo of each player
        winner.updateElo(winner_change)
        loser.updateElo(loser_change)
        
        
        
        

    
        
           
            
    

            
        
        
        
        
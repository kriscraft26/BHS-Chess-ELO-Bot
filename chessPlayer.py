class Player:
    
    #Sets the player's name and default elo

    def __init__(self, *args):
            if(isinstance(args[0],str)):
                self.name = args[0]
                if(len(args) > 1):
                    self.elo = args[1]
                else:    
                    self.elo = 400


    #Updates the players elo, and increase the games played by one.
    def updateElo(self,elo_change):
        self.elo += elo_change
     
    #Returns the player elo    
    def getElo(self):
        return self.elo
    
    
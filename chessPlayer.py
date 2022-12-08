class Player:
    
    #Sets the player's name and default elo
    def __init__(self, name):
        self.name = name
        self.elo = 400
        self.games_played = 0
    

    #Updates the players elo, and increase the games played by one.
    def updateElo(self,elo_change):
        self.elo += elo_change
        self.games_played += 1
     
    #Returns the player elo    
    def getElo(self):
        return self.elo
    
    
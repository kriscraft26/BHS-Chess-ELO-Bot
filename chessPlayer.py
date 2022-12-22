class Player:

    """
    This is a class for chess players
    """
    #Sets the player's name and elo, if no elo is given, default to 400
    def __init__(self, *args):
            if(isinstance(args[0],str)):
                self.name = args[0]
                if(len(args) > 1):
                    self.elo = args[1]
                else:    
                    self.elo = 400
        
                    
    

    def updateElo(self,elo_change):
        """
        Based on given input, add or subtract from the original ELO of the player.

        Args:
            elo_change (float):  The amount that will be added/subtracted to the elo
        """
        self.elo += elo_change
     
    #Returns the player elo    
    def getElo(self):
        """
        Returns the rounded elo of the player

        Returns:
            int: The elo of the player rounded to a int, truncating the decimals
        """
        return int(self.elo)
    
    def get_name(self):
        """
        Returns the name of the player

        Returns:
            str: The name of the player 
        """
        return self.name
    
 
    
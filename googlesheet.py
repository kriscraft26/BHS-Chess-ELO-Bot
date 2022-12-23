from chessPlayer import Player
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class elo_sheet:

    def __init__(self):
        scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scopes)

        file = gspread.authorize(creds)
        chesssheet = file.open("chess")
        self.sheet = chesssheet.sheet1
    
    
    
    
    
    def add_player(self, player=Player):
        list = self.sheet.col_values(1)
        pos = len(list) + 1
        self.sheet.update_acell("A" + str(pos), player.get_name())
        self.sheet.update_acell("B" + str(pos), str(player.getElo()))

        
    
    def get_player_list(self):
        return self.sheet.col_values(1)
    
    def player_exist(self, name=str):
        for player in self.get_player_list():
            if player == name:
                return True 
        return False
    
    
    def get_position(self, name=str):
        list = self.sheet.col_values(1)
        for i in range(len(list)):
            if list[i] == name:
                return i + 1

    
    
    def get_elo(self, pos=int):
        elo = self.sheet.acell("B" + str(pos)).value
        return float(elo)       
         
    def update_sheet(self, player=Player):
        pos = self.get_position(player.get_name())
        self.sheet.update_acell("B" + str(pos), str(player.getElo()))
        
    
        
        
        
            
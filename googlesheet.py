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
    
    
    
    
    

        
    
    def get_position(self, name=str):
        list = self.sheet.col_values(1)
        for i in range(len(list)):
            if list[i] == name:
                return i + 1
    def update_sheet(self, player=Player):
        pos = self.get_position(player.get_name())
        self.sheet.update_acell("B" + str(pos), str(player.getElo()))
        
        
            
from chessPlayer import Player
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class elo_sheet:

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scopes)

    file = gspread.authorize(creds)
    chesssheet = file.open("chess")
    sheet = chesssheet.sheet1
    
    @staticmethod
    def updateSheet(player=Player):
        
        pass
        
        
from chessPlayer import Player
from chessCalculator import elo
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scopes)

file = gspread.authorize(creds)
chesssheet = file.open("chess")
sheet = chesssheet.sheet1
print(sheet.range("A2:A3"))

sheet.update_acell("A3", "Anisha")
print(sheet.acell("A2").value)
for name in sheet.range("A2:A3"):
    test = name.value
    print(test)
krishna = Player("Krishna")
kaleb = Player("Luka",1500)

print(kaleb.getElo())
print(krishna.getElo())
elo.elo_updater(kaleb,krishna,True)
print(kaleb.getElo())
print(krishna.getElo())
elo.elo_updater(krishna, kaleb, True)
print(kaleb.getElo())
print(krishna.getElo()) 





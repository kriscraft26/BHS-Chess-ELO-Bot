from chessPlayer import Player
from chessCalculator import elo
import gspread
from googlesheet import elo_sheet
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scopes)

file = gspread.authorize(creds)
chesssheet = file.open("chess")
sheet = chesssheet.sheet1




test = elo_sheet()

flag = True

while flag == True:
    
    
    flag_two = True
    win_type = True
    
        
    while flag_two == True:
        condition = input("Was it a draw? Type Y for Yes and N for No: ")
        if condition == "Y" or condition == "N":
            flag_two = False
            if condition == "Y":
                win_type = False  
    
    if win_type == True:
        print("Winner!")
    else:
        print("Player One")
        
    valid = False
    while valid == False:
        
        player_one_name = input("Please enter your name: ")
        if test.player_exist(player_one_name):
            valid = True
            pos = test.get_position(player_one_name)
            player_one = Player(player_one_name, test.get_elo(pos))
        
        else:
            confirmation = input("If you are a new member, enter Y. If you mistyped your name, enter N: ")
            
            if confirmation == "Y":
                player_one = Player(player_one_name)
                test.add_player(player_one)
                valid = True
    
    
    
    if win_type == True:
        print("Loser!")
    else:
        print("Player Two")
        
        
    valid = False
    while valid == False:
        player_two_name = input("Please enter your name: ")
        if test.player_exist(player_two_name):
            valid = True
            pos = test.get_position(player_two_name)
            player_two = Player(player_two_name, test.get_elo(pos))
        
        else:
            confirmation = input("If you are a new member, enter Y. If you mistyped your name, enter N: ")
            
            if confirmation == "Y":
                player_two = Player(player_two_name)
                test.add_player(player_two)
                valid = True
    
    elo.elo_updater(player_one, player_two, win_type)
    
    print("ELO and Match was successfully entered!")
    print("New ELO of " + player_one.get_name() + ": " + str(player_one.getElo()))
    print("New ELO of " + player_two.get_name() + ": " + str(player_two.getElo()))

    flag_three = True
    while flag_three == True:    
        cont = input("Type Y to enter another match or Type N to quit: ")
        if cont == "Y":
            flag_three = False
            print()
        elif cont == "N":
            flag_three = False
            flag = False
        
        
    



"""
print(kaleb.getElo())
print(krishna.getElo())
elo.elo_updater(kaleb,krishna,True)
print(kaleb.getElo())
print(krishna.getElo())
elo.elo_updater(krishna, kaleb, True)
print(kaleb.getElo())
print(krishna.getElo()) 

print(krishna.getElo()) 
"""




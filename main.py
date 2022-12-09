from chessPlayer import Player
from chessCalculator import elo
krishna = Player("Krishna")
kaleb = Player("Luka",1000)

print(kaleb.getElo())
print(krishna.getElo())
elo.elo_updater(kaleb,krishna,True)
print(kaleb.getElo())
print(krishna.getElo())
elo.elo_updater(krishna, kaleb, True)
print(kaleb.getElo())
print(krishna.getElo())





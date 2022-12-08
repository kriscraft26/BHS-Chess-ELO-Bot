from chessPlayer import Player
from chessCalculator import elo
krishna = Player("Krishna")
kaleb = Player("Kaleb")

elo.elo_updater(kaleb,krishna,1)
print(kaleb.getElo())
print(krishna.getElo())





import sys

sys.path.append("..")

#
#		main()
#
def main():
	from fireplace import cards
	cards.db.initialize()
	from utils import Agent,play_set_of_games,play_MechaHunterGames
	from hearthstone.enums import CardClass
	Human=Agent("Human",None,myClass=CardClass.MAGE)
	StandardRandom=Agent("Maya",None)
    play_set_of_games(Human, StandardRandom, gameNumber=1, debugLog=True) 
    pass
if __name__ == "__main__":
	main()
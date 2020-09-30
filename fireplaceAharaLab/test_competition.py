def play_MechaHunterGames(P1: Agent, P2: Agent, gameNumber=15, debugLog=True):
	if P1.myClass != CardClass.HUNTER or P2.myClass != CardClass.HUNTER:
		print("In MechaHunterGames, Player is expected to be of HUNTER.")
	if debugLog:
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
	Count1 = 0
	Count2 = 0
	for i in range(gameNumber):
		winner = play_one_game(P1,P2,deck1=BigDeck.MechaHunter, deck2=BigDeck.MechaHunter,debugLog=debugLog)
		print("winner is %r"%winner)
		if winner == P1.name:
			Count1+=1
		elif winner == P2.name:
			Count2+=1
	print(" %r (%s) wins: %d"%(P1.name, P1.myClass, Count1))
	print(" %r (%s) wins: %d"%(P2.name, P2.myClass, Count2))
	print(" Draw: %d"%(gameNumber-Count1-Count2))

class BigDeck:
	testHunter = ['BOT_445','BOT_445','BOT_035','BOT_035','BOT_038',\
		'BOT_038','BOT_309','BOT_309','BOT_907','BOT_907',\
		'BOT_033','BOT_033','DAL_604','DAL_604','BOT_251',\
		'BOT_251','BOT_700','EX1_556','EX1_556','BOT_532',\
		'BOT_532','BOT_312','BOT_312','BOT_563','BOT_563',\
		'BOT_548','EX1_116','BOT_107','BOT_107','BOT_034']

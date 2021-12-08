from .simulate_game import PresetGame, Preset_Play
from hearthstone.enums import Zone,CardType, Rarity

#Alterac_Warrior=['AV_108','AV_109','AV_109e','AV_119','AV_119e','AV_145','AV_145e','AV_202','AV_202p','AV_202t2','AV_321','AV_322','AV_323','AV_323t','AV_565','AV_660',]

def SimulateGames_Alterac_Warrior():
	""" simulate games  """
	#PresetGame(pp_AV_108)####OK
	#PresetGame(pp_AV_109)####OK
	#PresetGame(pp_AV_119)####OK
	#PresetGame(pp_AV_145)####OK
	#PresetGame(pp_AV_202)###################
	#PresetGame(pp_AV_321)####OK
	#PresetGame(pp_AV_322)####OK
	#PresetGame(pp_AV_323)####OK
	#PresetGame(pp_AV_565)####OK
	#PresetGame(pp_AV_660)####OK
	pass

#######################

class pp_AV_108(Preset_Play):
	"""Shield Shatter (10) frost
	Deal 5 damage to all minions. Costs (1) less for each Armor you have. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_108',controller)
		self.mark2=self.exchange_card('armor',controller)
		self.mark3=self.exchange_card('minionH6',opponent)
		self.mark4=self.exchange_card('vanillaH3',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		########## controller
		self.msg1 = "the cost of %s is %d"%(self.mark1, self.mark1.cost)
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# コストを☑
		print("%s <- %d - %d"%(self.msg1, self.mark1.cost, self.player.hero.armor))
		pass
	pass

#######################

class pp_AV_109(Preset_Play):
	""" Frozen Buckler (2) frost
	Gain 10 Armor. At the start of your next turn, lose 5 Armor. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_109',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.msg1 = "Armor of %s is %d:"%(self.mark1, controller.hero.armor)
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		pass
	def result_inspection(self):
		super().result_inspection()
		# check armor
		print("%s -> %d (10->5)"%(self.msg1, self.player.hero.armor))
		#最終ターン、AV_109eが破壊されることを目視。
		if not self.contains_buff(self.player,'AV_109e'):
			print("check OK")

		pass
	pass

#######################

class pp_AV_119(Preset_Play):
	""" To the Front! (2) 
	Your minions cost (2) less this turn (but not less than 1). """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_119',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check costs
		for card in self.player.hand:
			print("cost of %s = %d <- %d - 2"%(card, card.cost, card.data.cost), end=':')
			if self.contains_buff(card,'AV_119e'):
				print("check OK")

		pass
	pass

#######################

class pp_AV_145(Preset_Play):
	""" Captain Galvangar (6/6/6)
	Battlecry: If you have gained 15 or more Armor this game, gain +3/+3 and Charge. (#1 left!) (Ready!) """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_145',controller)
		super().preset_deck()
		controller.hero.armor=16# 16 or 14
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check stats
		print("stats of %s is (%d/%d) (=9/9)"%(self.mark1, self.mark1.atk, self.mark1.health))
		if self.mark1.charge:
			print("check 2 OK")
		pass
	pass

######################
#######################

class pp_AV_321(Preset_Play):
	""" Glory Chaser (3/4/3)
	After you play a Taunt minion, draw a card. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_321',controller)
		self.mark2=self.exchange_card('taunt',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check whether a card drawn
		print ("カードをドローしたかどうかを目視")
		pass
	pass

#######################

class pp_AV_322(Preset_Play):
	""" Snowed In (3) frost
	Destroy a damaged minion. Freeze all other minions. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_322',controller)
		self.mark2=self.exchange_card('vanillaA3',controller)
		self.mark3=self.exchange_card('minionH5',opponent)
		self.mark4=self.exchange_card('vanillaH2',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		########## controller
		self.attack_card(self.mark2, self.mark3, controller)
		self.play_card(self.mark1, controller, target=self.mark3)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check whether a card drawn
		print ("self.mark2が破壊されていることを目視")
		print ("ミニオンたちがfreezeされていることを目視")
		pass
	pass

#######################


class pp_AV_323(Preset_Play):
	""" Scrapsmith (3/2/4)
	Taunt Battlecry: Add two 2/4 Grunts with Taunt to your hand. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_323',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark3, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check whether a card drawn
		print ("ハンドのカードを確認")
		card1 = self.player.hand[-1]
		card2 = self.player.hand[-2]
		if card1.id=='AV_323t' and card1.taunt:
			print("check 1 OK %s STATS(%d/%d)"%(card1,card1.atk, card1.health))
		if card2.id=='AV_323t' and card2.taunt:
			print("check 2 OK %s STATS(%d/%d)"%(card2,card2.atk, card2.health))
		pass
	pass

#######################

class pp_AV_565(Preset_Play):
	""" Axe Berserker (4/3/5)
	Rush. Honorable Kill: Draw a weapon. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_565',controller)
		self.mark2=self.exchange_card('vanillaH3',opponent)## 3 or 2
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check whether a card drawn
		print ("ハンドのカードを確認")
		card1 = self.player.hand[-1]
		if card1.type==CardType.WEAPON:
			print("check 1 OK %s STATS(%d/%d)"%(card1,card1.atk, card1.durability))
		pass
	pass

#######################

class pp_AV_660(Preset_Play):
	""" Iceblood Garrison (2)
	At the end of your turn, deal 1 damage to all minions. Lasts 3 turns. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_660',controller)
		self.mark2=self.exchange_card('minionH5',controller)##
		self.mark3=self.exchange_card('vanillaH3',opponent)##
		self.mark4=self.exchange_card('minionH6',opponent)##
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		########## controller
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check whether a card drawn
		print ("プレイの詳細を確認")
		print ("「全てのミニオンにターン開始ごとに１ダメ」を3回行うかどうかを☑。")
	pass

#######################